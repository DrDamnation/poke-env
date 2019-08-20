# -*- coding: utf-8 -*-
"""Constants file

This file contains constant values used in the repository.

Attributes:
    TYPE_CHART_PATH (str): Path to the json file containing type informations.
"""

import os


TYPE_CHART_PATH = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "data", "typeChart.json"
)
"str: Path to the json file containing type informations."