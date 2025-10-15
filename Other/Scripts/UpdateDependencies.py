from pathlib import Path
from ScriptCollection.ScriptCollectionCore import ScriptCollectionCore
from ScriptCollection.GeneralUtilities import GeneralUtilities
from ScriptCollection.TFCPS.TFCPS_Tools_General import TFCPS_Tools_General


def update_dependencies():
    current_file = str(Path(__file__).absolute())
    repository_folder = GeneralUtilities.resolve_relative_path("../../..", current_file)
    sc:ScriptCollectionCore=ScriptCollectionCore()
    t: TFCPS_Tools_General = TFCPS_Tools_General(sc) 
    t.update_submodule(repository_folder, "countries", "main", "master", "origin")


if __name__ == "__main__":
    update_dependencies()
