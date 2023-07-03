#!/usr/bin/python3
"""_summary_"""


def safe_print_list(my_list=[], x=0):
    """_summary_

    Args:
        my_list (list, optional): _description_. Defaults to [].
        x (int, optional): _description_. Defaults to 0.

    Returns:
        int: number of printed element of the list
    """
    try:
        pr = len([print(my_list[i], end="") for i in range(x) if my_list[i] != None])
        print()
        return pr
    except Exception as ex:
        pass