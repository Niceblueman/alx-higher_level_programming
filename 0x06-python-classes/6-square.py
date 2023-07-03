#!/usr/bin/python3
"""_summary_
"""


class Square:
    """_summary_
    """
    def __init__(self, size=0, position=(0, 0)):
        """_summary_

        Args:
            size (int, optional): _description_. Defaults to 0.
            position (tuple, optional): _description_. Defaults to (0, 0).

        Raises:
            TypeError: _description_
            ValueError: _description_
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.position = position

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
            return
        [print() for j in range(self.__position[1])]
        [print(" " * self.__position[0], end="") or print("#" * self.__size)
            for i in range(self.__size)]

    @property
    def position(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__position

    @position.setter
    def position(self, value):
        """_summary_

        Args:
            value (_type_): _description_

        Raises:
            TypeError: _description_
            TypeError: _description_
            TypeError: _description_
            TypeError: _description_
            TypeError: _description_
        """
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif isinstance(value[0], int) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif isinstance(value[1], int) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def __str__(self):
        self.my_list = []
        if self.__size == 0:
            return ""
        [self.my_list.append("\n") for j in range(self.__position[1])]
        for i in range(self.__size):
            self.my_list.append(" " * self.__position[0])
            self.my_list.append("#" * self.__size)
            if (i < self.__size - 1):
                self.my_list.append("\n")
        return "".join(self.my_list)
