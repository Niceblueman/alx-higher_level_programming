#!/usr/bin/python3
"""class Rectangle with setters and getters of instances
"""


class Rectangle:
    """_summary_
    """

    def __init__(self, width=0, height=0):
        """_summary_

        Args:
            width (int, optional): _description_. Defaults to 0.
            height (int, optional): _description_. Defaults to 0.
        """
        if (type(width) != int):
            raise TypeError("width must be an integer")
        if (width < 0):
            raise ValueError("width must be >= 0")
        if (type(height) != int):
            raise TypeError("width must be an integer")
        if (height < 0):
            raise ValueError("width must be >= 0")
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """_summary_

        Returns:
            int: width
        """
        return self.__width

    @property
    def height(self):
        """_summary_

        Returns:
            int: height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """_summary_

        Args:
            value (int): value width

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if (type(value) != int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """_summary_

        Args:
            value (int): value height

        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if (type(value) != int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value
