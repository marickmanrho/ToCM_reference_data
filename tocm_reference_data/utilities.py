from .base_class import Line, Figure, Reference

import pandas as pd
import numpy as np
import pandas as pd
import pkg_resources
import json
import os


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
