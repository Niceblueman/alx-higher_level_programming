#!/usr/bin/python3
"""_summary_
"""


class Student:
    """_summary_
    """

    def __init__(self, first_name, last_name, age):
        """_summary_

        Args:
            first_name (_type_): _description_
            last_name (_type_): _description_
            age (_type_): _description_
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__dict__.copy()
