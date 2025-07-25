import os
import unittest
from ScriptCollection.GeneralUtilities import GeneralUtilities
from ..CountryInformation.Language import Language
from ..CountryInformation.Country import Country
from ..CountryInformation.CountryInformationCore import CountryInformationCore


class CountryInformation(unittest.TestCase):

    def test_get_all_countries(self) -> None:

        # arrange
        ci: CountryInformationCore = CountryInformationCore()

        # act
        all_countries = ci.get_all_countries()

        # assert
        assert 0 < len(all_countries)
        # TODO add more assertions

    def test_get_all_languages(self) -> None:

        # arrange
        ci: CountryInformationCore = CountryInformationCore()

        # act
        all_languages = ci.get_all_languages()

        # assert
        assert 0 < len(all_languages)
        # TODO add more assertions

    def test_get_all_common_culture_language_combinations(self) -> None:

        # arrange
        ci: CountryInformationCore = CountryInformationCore()

        # act
        all_common_culture_language_combinations = ci.get_all_common_culture_language_combinations()

        # assert
        assert 0 < len(all_common_culture_language_combinations)
        # TODO add more assertions

    def test_generate_artifacts(self) -> None:  # just to see in the artifacts which data are available in the library

        ci: CountryInformationCore = CountryInformationCore()
        current_folder: str = os.path.dirname(__file__)
        target_folder = GeneralUtilities.resolve_relative_path("../Other/Resources/Data", current_folder)
        GeneralUtilities.ensure_folder_exists_and_is_empty(target_folder)

        all_countries: list[Country] = ci.get_all_countries()
        countries_file = os.path.join(target_folder, "Countries.csv")
        GeneralUtilities.ensure_file_exists(countries_file)
        countries_lines = [f"{country.common_name_in_english};{country.country_code};{country.official_name_in_english}" for country in all_countries]
        GeneralUtilities.write_lines_to_file(countries_file, countries_lines)

        all_languages: list[Language] = ci.get_all_languages()
        languages_file = os.path.join(target_folder, "Languages.csv")
        GeneralUtilities.ensure_file_exists(languages_file)
        language_lines = [f"{language.name_in_english};{language.abbreviation_iso639_1};{language.abbreviation_iso639_3}" for language in all_languages]
        GeneralUtilities.write_lines_to_file(languages_file, language_lines)

        all_common_culture_language_combinations = ci.get_all_common_culture_language_combinations()
        common_culture_language_combinations_file = os.path.join(target_folder, "CommonCultureLanguageCombinations.csv")
        GeneralUtilities.ensure_file_exists(common_culture_language_combinations_file)
        common_culture_language_combinations_lines = [f"{common_culture_language_combination.get_abbreviation()}" for common_culture_language_combination in all_common_culture_language_combinations]
        GeneralUtilities.write_lines_to_file(common_culture_language_combinations_file, common_culture_language_combinations_lines)

        languages_with_fallback_language_file = os.path.join(target_folder, "LanguagesWithFallbackLanguage.csv")  # usual fallback-language for translations in it-systems (i18n)
        GeneralUtilities.ensure_file_exists(languages_with_fallback_language_file)
        base_language: str = "en"
        languages_with_fallback_language_entries: set[str] = set()
        for language in all_languages:
            entry: str = language.abbreviation_iso639_1+";"
            if language.abbreviation_iso639_1 != base_language:
                entry = entry+base_language
            languages_with_fallback_language_entries.add(entry)
        for common_culture_language_combination in all_common_culture_language_combinations:
            entry: str = f"{common_culture_language_combination.get_abbreviation()};{common_culture_language_combination.language.abbreviation_iso639_1}"
            languages_with_fallback_language_entries.add(entry)
        GeneralUtilities.write_lines_to_file(languages_with_fallback_language_file, sorted(languages_with_fallback_language_entries, key=lambda entry: entry))

        artefacts_folder = GeneralUtilities.resolve_relative_path("../Other/Artifacts/Data", current_folder)
        GeneralUtilities.ensure_folder_exists_and_is_empty(artefacts_folder)
        GeneralUtilities.copy_content_of_folder(target_folder, artefacts_folder)
