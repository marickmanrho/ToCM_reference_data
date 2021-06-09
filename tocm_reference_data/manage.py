from .utilities import get_user_settings_file

import argparse
import json


def add_library(paths):
    settings_file = get_user_settings_file()
    with open(settings_file, "r") as f:
        settings = json.load(f)

    for path in paths:
        settings["libraries"].append(path)

    with open(settings_file, "w") as f:
        json.dump(settings, f)


def remove_library(elements):
    settings_file = get_user_settings_file()
    with open(settings_file, "r") as f:
        settings = json.load(f)

    for element in elements:
        settings["libraries"].pop(element)

    with open(settings_file, "w") as f:
        json.dump(settings, f)


def list_libraries():
    settings_file = get_user_settings_file()
    with open(settings_file, "r") as f:
        settings = json.load(f)

    if len(settings["libraries"]) > 0:
        print("Available user defined libraries:")
        for i, lib in enumerate(settings["libraries"]):
            print(f"{i}\t {lib}")
    else:
        print("No user defined libraries available...")


def manage():
    parser = argparse.ArgumentParser(
        description="Reference data of the ToCM group in Groningen.",
        prog="tocm_reference_data",
        usage="python3 tocm_reference_data [options]",
    )
    parser.add_argument(
        "--add-library",
        nargs=1,
        type=str,
        help="Add a user defined absolute path to the library.",
    )
    parser.add_argument(
        "--list-libraries",
        help="Show all libraries known to the system.",
        action="store_true",
    )
    parser.add_argument(
        "--remove-library", nargs=1, type=int, help="Removes the n-th library path.",
    )
    args = parser.parse_args()

    if args.list_libraries:
        list_libraries()

    if args.add_library:
        add_library(args.add_library)

    if args.remove_library:
        remove_library(args.remove_library)
