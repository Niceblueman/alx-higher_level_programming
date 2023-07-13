#!/usr/bin/python3
"""_summary_
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """_summary_

    Args:
        BaseGeometry (_type_): _description_
    """
    def __init__(self, width, height):
        """
            initialises Rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        area = self.__width * self.__height
        return area

    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return ("[{}] {}/{}".format(type(self).__name__,
                                    self.__width, self.__height))
