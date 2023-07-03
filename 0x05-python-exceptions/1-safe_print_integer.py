#!/usr/bin/python3
def safe_print_integer(value):
    """_summary_

    Args:
        value (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        print("{:d}".format(value))
        return True
    except:
        return False
