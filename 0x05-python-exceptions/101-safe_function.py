#!/usr/bin/python3
def safe_function(fct, *args):
    """_summary_

    Args:
        fct (_type_): _description_

    Returns:
        _type_: _description_
    """
    import sys
    try:
        return (fct(*args))
    except Exception as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return None
