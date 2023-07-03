#!/usr/bin/python3
def safe_print_integer_err(value):
    """_summary_

    Args:
        value (_type_): _description_

    Returns:
        _type_: _description_
    """
    import sys
    try:
        print("{:d}".format(value))
        return True
    except Exception as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return False
