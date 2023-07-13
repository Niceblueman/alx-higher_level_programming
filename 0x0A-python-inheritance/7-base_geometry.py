#!/usr/bin/python3
"""_summary_
"""


class BaseGeometry:
    """_summary_
    """
    def area(self):
        """_summary_

        Raises:
            Exception: _description_
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """_summary_

        Args:
            name (_type_): _description_
            value (_type_): _description_

        Raises:
            TypeError: _description_
            ValueError: _description_
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
