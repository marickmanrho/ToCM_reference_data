from .base_class import Line, Figure, Reference

import pandas as pd
import numpy as np
import pandas as pd
import pkg_resources
import json
import os

import sys
import pathlib
from typing import Union, List, Tuple


def create_reference(info):
    metadata = import_metadata_from_json(info["metadata"]["file"])

    figs = []
    for figure in info["figures"]:
        figures_type = os.path.splitext(figure["file"])
        if ".csv" in figures_type:
            lines = import_figure_from_csv(figure["file"])

        figs.append(Figure(name=figure["name"], lines=lines))

    return Reference(metadata, figs)


def import_figure_from_csv(path):
    # Create a stream relative to package location
    stream = pkg_resources.resource_stream(__name__, path)

    data = pd.read_csv(stream)

    columns = data.columns.values.tolist()

    Nlines = int(data.shape[1] / 2)

    # Make sure array contains floats
    val = data.values[1:]
    val = np.array(val, dtype=np.float)

    lines = []
    for i in range(Nlines):
        lines.append(
            Line(val[:, 2 * i], val[:, 2 * i + 1], str(columns[2 * i]))
        )  # Each line consists of two columns in the dataframe (X,Y)

    return lines


def import_metadata_from_json(path):
    # Create a stream relative to package location
    stream = pkg_resources.resource_stream(__name__, path)

    metadata = json.load(stream)

    if isinstance(metadata, list):
        return metadata[0]
    else:
        return metadata


def save_metadata_to_json(data, path):
    stream = pkg_resources.resource_stream(__name__, path)
    json.dump(data, stream)


def get_user_data_dir(
    appending_paths: Union[str, List[str], Tuple[str, ...]] = None
) -> pathlib.Path:
    """
    Returns a parent directory path where persistent application data can be stored.
    Can also append additional paths to the return value automatically.

    Linux: ~/.local/share
    macOS: ~/Library/Application Support
    Windows: C:/Users/<USER>/AppData/Roaming

    :param appending_paths: Additional path (str) or paths (List[str], Tuple[str]) to append to return value
    :type appending_paths: Un

    :return: User Data Path
    :rtype: str
    """

    home = pathlib.Path.home()

    system_paths = {
        "win32": home / "AppData/Roaming",
        "linux": home / ".local/share",
        "darwin": home / "Library/Application Support",
    }

    if sys.platform not in system_paths:
        raise SystemError(
            f'Unknown System Platform: {sys.platform}. Only supports {", ".join(list(system_paths.keys()))}'
        )
    data_path = system_paths[sys.platform]

    if appending_paths:
        if isinstance(appending_paths, str):
            appending_paths = [appending_paths]
        for path in appending_paths:
            data_path = data_path / path

    return data_path


def get_user_settings_file():
    data_dir = get_user_data_dir()
    path = f"{data_dir}/tocm_reference_data/settings.json"

    if not os.path.isdir(f"{data_dir}/tocm_reference_data/"):
        os.makedirs(f"{data_dir}/tocm_reference_data/")

    if os.path.isfile(path):
        return path
    else:
        with open(path, "w") as file:
            json.dump({"libraries": []}, file)
