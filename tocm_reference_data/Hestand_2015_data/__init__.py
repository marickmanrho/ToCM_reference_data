from ..base_class import Figure
from ..utilities import import_figure_from_csv

import pandas as pd

metadata = {
    "year": 2015,
    "authors": "N. Hestand et. al."
}

fig7_lines = import_figure_from_csv('Hestand_2015_data/Hestand_2015_fig7_monomer.csv')

Figure7 = Figure(name='figure7', lines=fig7_lines)

figures = [Figure7]