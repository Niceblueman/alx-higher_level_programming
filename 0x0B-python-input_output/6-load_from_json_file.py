#!/usr/bin/python3
"""_summary_
"""


import json


def load_from_json_file(filename):
    """_summary_

    Args:
        filename (_type_): _description_

    Returns:
        _type_: _description_
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
