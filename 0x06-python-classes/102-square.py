#!/usr/bin/python3
import math


class MagicClass:
    """_summary_
    """
    def __init__(self, radius=0):
        """_summary_

        Args:
            radius (int, optional): _description_. Defaults to 0.

        Raises:
            TypeError: _description_
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return (2 * math.pi * self.__radius)
