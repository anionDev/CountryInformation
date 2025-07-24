import sys
import os
from pathlib import Path
from ScriptCollection.GeneralUtilities import GeneralUtilities
from ScriptCollection.ScriptCollectionCore import ScriptCollectionCore
from ScriptCollection.TasksForCommonProjectStructure import TasksForCommonProjectStructure


@GeneralUtilities.check_arguments
def get_data_from_submodule(codeunit_folder: str) -> None:
    # it is ok to do that in this script and not in UpdateDependencies.py because after updating the submodule the codeunits will bebuilded and then this will be executed anyway. And without an updated submodule this function does not cause any change.
    repository_folder = GeneralUtilities.resolve_relative_path("..", codeunit_folder)
    upstream_folder = GeneralUtilities.resolve_relative_path("Other/Resources/Submodules/countries", repository_folder)
    GeneralUtilities.assert_folder_exists(upstream_folder)
    target_folder = GeneralUtilities.resolve_relative_path("./Other/Resources/Data", codeunit_folder)
    GeneralUtilities.ensure_folder_exists_and_is_empty(target_folder)
    # TODO copy required data from upstream_folder to target_folder


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


if __name__ == "__main__":
    common_tasks()
