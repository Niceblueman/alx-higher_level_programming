#!/usr/bin/python3
"""...."""


def append_write(filename="", text=""):
    """_summary_

    Args:
        filename (str, optional): _description_. Defaults to "".
        text (str, optional): _description_. Defaults to "".

    Returns:
        _type_: _description_
    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
