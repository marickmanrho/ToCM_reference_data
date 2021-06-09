from .utilities import create_reference, import_metadata_from_json

import pkg_resources

for folder in pkg_resources.resource_listdir(__name__, "lib/"):
    if folder == "__init__.py":
        continue
    else:
        reference_files = pkg_resources.resource_listdir(__name__, f"lib/{folder}/")
        for ref_file in reference_files:
            if ref_file.endswith("info.json"):
                info = import_metadata_from_json(f"lib/{folder}/{ref_file}")
                exec(f"{folder} = create_reference({info})")
