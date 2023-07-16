#!/usr/bin/python3

from models.base import Base
"""_summary_
Raises:
    TypeError: _description_
    ValueError: _description_
Returns:
    _type_: _description_
"""


class Rectangle(Base):
    """
    Class Rectangle, which implements Base.
    Attributes:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
        x (int): X-coordinate of the rectangle.
        y (int): Y-coordinate of the rectangle.
        id (int): Unique identifier for the instance.
    Methods:
        __init__(self, width, height, x=0, y=0, id=None)
        area(self)
        display(self)
        __str__(self)
        update(self, *args, **kwargs)
        to_dictionary(self)
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the instance of the class.
        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): X-coordinate of the rectangle. Default is 0.
            y (int): Y-coordinate of the rectangle. Default is 0.
            id (int): Unique identifier for the instance. 
            If not provided, it will be automatically assigned.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter function for width.
        Returns:
            int: Width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter function for width.
        Args:
            value (int): Value to be set as the width.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not greater than 0.
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    # (Similar comments for height, x, and y properties)

    def area(self):
        """
        Returns the area of the Rectangle instance.
        Returns:
            int: Area of the rectangle (width * height).
        """
        return (self.__width * self.__height)

    def display(self):
        """
        Prints the Rectangle instance with '#' to stdout.
        """
        rectangle = ""
        print_symbol = "#"

        # Code to generate the rectangle string

        print("\n" * self.y, end="")
        print(rectangle, end="")

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        Returns:
            str: String representation of the rectangle in the format:
                 "[Rectangle] (id) x/y - width/height"
        """
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
                                                self.__x, self.__y,
                                                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        Assigns key/value arguments to attributes. If args is 
        not empty, kwargs is skipped.
        Args:
            *args: Variable number of non-keyword arguments.
            **kwargs: Variable number of keyword arguments.
        """
        # Code to handle updating attributes based on args or kwargs

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Rectangle instance.
        Returns:
            dict: Dictionary representing the Rectangle instance's 
            attributes.
        """
        return {'x': getattr(self, "x"), 'y': getattr(self, "y"),
                'id': getattr(self, "id"), 'height': getattr(self, "height"),
                'width': getattr(self, "width")}
