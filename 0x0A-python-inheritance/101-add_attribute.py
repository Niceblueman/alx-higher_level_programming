#!/usr/bin/python3
"""_summary_
"""


def add_attribute(cls, name, value):
    """_summary_

    Args:
        name (_type_): _description_
        value (_type_): _description_

    Raises:
        TypeError: _description_
    """
    if hasattr(cls, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(cls, name, value)
