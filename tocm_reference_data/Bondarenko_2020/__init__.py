from ..base_class import Figure, Reference
from ..utilities import import_metadata_from_json, import_figure_from_csv

import json

metadata = import_metadata_from_json(
    "Bondarenko_2020/Bondarenko_2020_ChemSci_reference.json"
)

fig1f_lines = import_figure_from_csv(
    "Bondarenko_2020/Bondarenko_2020_ChemSci_fig1f.csv"
)
Figure1f = Figure(name="figure1f", lines=fig1f_lines)

figures = [Figure1f]

Hestand_2015 = Reference(metadata, figures)
