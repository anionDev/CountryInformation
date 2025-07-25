import sys
import os
import shutil
from pathlib import Path
import json
from ScriptCollection.GeneralUtilities import GeneralUtilities
from ScriptCollection.ScriptCollectionCore import ScriptCollectionCore
from ScriptCollection.TasksForCommonProjectStructure import TasksForCommonProjectStructure


def assert_not_none(obj) -> None:
    GeneralUtilities.assert_condition(obj is not None, "Object is none")


@GeneralUtilities.check_arguments
def format_json_file(json_file: str) -> None:
    content_plain = GeneralUtilities.read_text_from_file(json_file)
    content = json.loads(content_plain)
    content_formatted = json.dumps(content, indent=4)
    GeneralUtilities.write_text_to_file(json_file, content_formatted)


@GeneralUtilities.check_arguments
def generate_language_file(target_file: str, datasets) -> None:
    file_content = """# The content of this file is generated.
from .Language import Language
from .LanguageCodeConversionUtilities import LanguageCodeConversionUtilities

class LanguageData:
    def get_all_languages(self)->list[Language]:
        result:list[Language]=[]

"""
    languages: set[tuple[str, str]] = set()
    for dataset in datasets:
        if dataset["independent"]:
            for language_abbreviation, language_name in dataset["languages"].items():
                languages.add((language_abbreviation, language_name))
    for language in sorted(languages, key=lambda dataset: dataset):
        file_content = file_content+f'        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("{language[0]}"):\n            result.append(Language(LanguageCodeConversionUtilities().get_iso639_1_code_from_iso639_3("{language[0]}"), "{language[0]}", "{language[1]}"))\n'
    file_content = file_content+"\n        return result\n"
    GeneralUtilities.ensure_file_exists(target_file)
    GeneralUtilities.write_text_to_file(target_file, file_content)


@GeneralUtilities.check_arguments
def generate_countries_file(target_file: str, datasets) -> None:
    file_content = """# The content of this file is generated.
from .Country import Country
from .Language import Language
from .LanguageUtilities import LanguageUtilities
from .LanguageCodeConversionUtilities import LanguageCodeConversionUtilities


class CountryData:
    def get_all_countries(self) -> list[Country]:
        result:list[Country] = []
        language_utilities: LanguageUtilities = LanguageUtilities(None)

"""
    for dataset in sorted(datasets, key=lambda dataset: dataset["name"]["common"]):
        if dataset["independent"]:
            common_name_in_english: str = dataset["name"]["common"]
            assert_not_none(common_name_in_english)
            official_name_in_english: str = dataset["name"]["official"]
            assert_not_none(official_name_in_english)
            country_code: str = dataset["cca2"]
            assert_not_none(country_code)
            file_content = file_content+f'        languages_for_{country_code}: list[Language] = []\n'
            for language_abbreviation_iso639_3, language_name in dataset["languages"].items():  # pylint:disable=unused-variable
                file_content = file_content+f'        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("{language_abbreviation_iso639_3}"):\n            languages_for_{country_code}.append(language_utilities.get_language_from_code_iso639_3("{language_abbreviation_iso639_3}"))\n'
            file_content = file_content+f'        result.append(Country("{common_name_in_english}", "{official_name_in_english}", "{country_code}", languages_for_{country_code}))\n        \n'
    file_content = file_content+"\n        return result\n"
    GeneralUtilities.ensure_file_exists(target_file)
    GeneralUtilities.write_text_to_file(target_file, file_content)


@GeneralUtilities.check_arguments
def generate_python_data_files(codeunit_folder: str) -> None:
    source_folder = GeneralUtilities.resolve_relative_path("./Other/Resources/RawData", codeunit_folder)
    source_file = os.path.join(source_folder, "Countries.json")
    data = json.loads(GeneralUtilities.read_text_from_file(source_file))
    python_folder: str = os.path.join(codeunit_folder, "CountryInformation")
    generate_language_file(os.path.join(python_folder, "LanguageData.py"), data)
    generate_countries_file(os.path.join(python_folder, "CountryData.py"), data)


@GeneralUtilities.check_arguments
def get_data_from_submodule(codeunit_folder: str) -> None:
    # it is ok to do that in this script and not in UpdateDependencies.py because after updating the submodule the codeunits will bebuilded and then this will be executed anyway. And without an updated submodule this function does not cause any change.
    repository_folder = GeneralUtilities.resolve_relative_path("..", codeunit_folder)
    upstream_folder = GeneralUtilities.resolve_relative_path("Other/Resources/Submodules/countries", repository_folder)
    target_folder = GeneralUtilities.resolve_relative_path("./Other/Resources/RawData", codeunit_folder)
    GeneralUtilities.ensure_folder_exists_and_is_empty(target_folder)
    src_file = GeneralUtilities.resolve_relative_path("./dist/countries.json", upstream_folder)
    GeneralUtilities.assert_file_exists(src_file)
    target_file = os.path.join(target_folder, "Countries.json")
    shutil.copyfile(src_file, target_file)
    format_json_file(target_file)


def common_tasks():
    file = str(Path(__file__).absolute())
    folder_of_current_file = os.path.dirname(file)
    sc = ScriptCollectionCore()
    cmd_args = sys.argv
    t = TasksForCommonProjectStructure()
    codeunit_folder = GeneralUtilities.resolve_relative_path("..", os.path.dirname(file))
    codeunitname = os.path.basename(GeneralUtilities.resolve_relative_path("..", os.path.dirname(file)))
    verbosity = t.get_verbosity_from_commandline_arguments(cmd_args, 1)
    targetenvironmenttype = t.get_targetenvironmenttype_from_commandline_arguments(cmd_args, "QualityCheck")
    additional_arguments_file = t.get_additionalargumentsfile_from_commandline_arguments(cmd_args, None)
    codeunit_version = sc.get_semver_version_from_gitversion(GeneralUtilities.resolve_relative_path("../..", os.path.dirname(file)))  # Should always be the same as the project-version
    sc.replace_version_in_ini_file(GeneralUtilities.resolve_relative_path("../setup.cfg", folder_of_current_file), codeunit_version)
    sc.replace_version_in_python_file(GeneralUtilities.resolve_relative_path(f"../{codeunitname}/{codeunitname}Core.py", folder_of_current_file), codeunit_version)
    t.standardized_tasks_do_common_tasks(file, codeunit_version, verbosity, targetenvironmenttype, True, additional_arguments_file, False, cmd_args)
    get_data_from_submodule(codeunit_folder)
    generate_python_data_files(codeunit_folder)


if __name__ == "__main__":
    common_tasks()
