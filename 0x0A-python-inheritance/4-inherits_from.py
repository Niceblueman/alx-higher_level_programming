#!/usr/bin/python3
"""_summary_
"""


def inherits_from(obj, a_class):
    """_summary_

    Args:
        obj (_type_): _description_
        a_class (_type_): _description_

    Returns:
        _type_: _description_
    """
    if not type(obj) is a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
