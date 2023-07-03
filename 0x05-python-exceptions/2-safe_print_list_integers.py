#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """_summary_

    Args:
        my_list (list, optional): _description_. Defaults to [].
        x (int, optional): _description_. Defaults to 0.

    Returns:
        _type_: _description_
    """
    if my_list is None:
        return 0
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count = count + 1
        except (ValueError, TypeError):
            pass
    print()
    return count
