import os

package_location = "tocm_reference_data"
data_files = []
for root, dirs, files in os.walk(package_location + "/lib"):
    for file in files:
        if file.endswith(".json") or file.endswith(".csv"):
            data_files.append(
                os.path.relpath(os.path.join(root, file), package_location)
            )

