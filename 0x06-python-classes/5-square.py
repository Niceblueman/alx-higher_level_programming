#!/usr/bin/python3
"""_summary_
"""


class Square:
    """_summary_
    """
    def __init__(self, size=0):
        """_summary_

        Args:
            size (int, optional): _description_. Defaults to 0.

        Raises:
            TypeError: _description_
            ValueError: _description_
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__size

    @size.setter
    def size(self, value):
        """_summary_

        Args:
            value (_type_): _description_

        Raises:
            TypeError: _description_
            ValueError: _description_
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """_summary_
        """
        if self.__size == 0:
            print()
        else:
            [[print("#", end="") for i in range(self.__size)]
                for i in range(self.__size)]
            print()
