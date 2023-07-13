#!/usr/bin/python3
"""_summary_
"""


class MyInt(int):
    """_summary_

    Args:
        int (_type_): _description_
    """
    def __init__(self, number):
        self.number = number

    def __ne__(self, value):
        return (self.number == value)

    def __eq__(self, value):
        return (self.number != value)

    def __str__(self):
        return (str(self.number))
