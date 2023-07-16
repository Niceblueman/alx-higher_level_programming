#!/usr/bin/python3

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square, which implements Rectangle.
    Attributes:
        size (int): Size of the square (width and height are the same).
        x (int): X-coordinate of the square's position.
        y (int): Y-coordinate of the square's position.
        id (int): Unique identifier for the instance.
    Methods:
        __init__(self, size, x=0, y=0, id=None)
        size (property)
        size (setter)
        update(self, *args, **kwargs)
        __str__(self)
        to_dictionary(self)
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes the Square instance.
        Args:
            size (int): Size of the square (width and height are the same).
            x (int): X-coordinate of the square's position. Default is 0.
            y (int): Y-coordinate of the square's position. Default is 0.
            id (int): Unique identifier for the instance. If not provided, it will be automatically assigned.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter function for size (width and height are the same).
        Returns:
            int: Size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter function for size (width and height are the same).
        Args:
            value (int): Value to be set as the size.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not greater than 0.
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Assigns key/value arguments to attributes. If args is not empty, kwargs is skipped.
        Args:
            *args: Variable number of non-keyword arguments.
            **kwargs: Variable number of keyword arguments.
        """
        # Code to handle updating attributes based on args or kwargs

    def __str__(self):
        """
        Returns a string representation of the square.
        Returns:
            str: String representation of the square in the format:
                 "[Square] (id) x/y - size"
        """
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__,
                                             self.id, self.x, self.y,
                                             self.width)

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Square instance.
        Returns:
            dict: Dictionary representing the Square instance's attributes.
        """
        return {'id': getattr(self, "id"),
                'size': getattr(self, "width"),
                'x': getattr(self, "x"),
                'y': getattr(self, "y")}
