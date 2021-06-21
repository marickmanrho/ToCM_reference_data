from .utilities import (
    create_reference,
    import_metadata_from_json,
    get_user_settings_file,
    create_external_reference,
)

import pkg_resources
import os
import json

# Load data from package library
for folder in pkg_resources.resource_listdir(__name__, "lib/"):
    if folder == "__init__.py" or folder == "settings.json":
        continue
    else:
        reference_files = pkg_resources.resource_listdir(__name__, f"lib/{folder}/")
        for ref_file in reference_files:
            if ref_file.endswith("info.json"):
                info = import_metadata_from_json(f"lib/{folder}/{ref_file}")
                exec(f"{folder} = create_reference({info})")

# Load settings file
settings_file = get_user_settings_file()
with open(settings_file, "r") as file:
    settings = json.load(file)

# Import data from user defined libraries
for lib in settings["libraries"]:
    with os.scandir(lib) as l:
        for folder in l:
            if not folder.is_file():
                with os.scandir(f"{lib}/{folder.name}") as f:
                    for file in f:
                        if file.name.endswith("info.json"):
                            with open(
                                os.path.join(lib, folder.name, file.name), "r"
                            ) as q:
                                info = json.load(q)
                            path = os.path.join(lib, folder.name)
                            exec(
                                f"{folder.name} = create_external_reference(info, path)"
                            )
