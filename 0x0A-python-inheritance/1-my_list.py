#!/usr/bin/python3
"""
    1-my_list: class MyList
"""


class MyList(list):
    """_summary_

    Args:
        list (_type_): _description_
    """
    def print_sorted(self):
        """_summary_
        """
        print(sorted(self))
