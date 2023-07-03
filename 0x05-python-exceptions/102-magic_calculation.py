#!/usr/bin/python3
def magic_calculation(a, b):
    """_summary_

    Args:
        a (_type_): _description_
        b (_type_): _description_

    Raises:
        Exception: _description_

    Returns:
        _type_: _description_
    """
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                result += (a ** b) / i
        except:
            result = b + a
            break
    return result
