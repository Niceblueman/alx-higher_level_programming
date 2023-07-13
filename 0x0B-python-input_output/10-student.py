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

    def to_json(self, attrs=None):
        """_summary_

        Args:
            attrs (_type_, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        """
        obj = self.__dict__.copy()
        if type(attrs) is list:

            for item in attrs:
                if type(item) is not str:
                    return obj

            d_list = {}

            for iatr in range(len(attrs)):
                for satr in obj:
                    if attrs[iatr] == satr:
                        d_list[satr] = obj[satr]
            return d_list

        return obj
