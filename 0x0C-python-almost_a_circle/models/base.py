#!/usr/local/python3
"""_summary_"""

import json
import csv


class Base:
    """
    Base class for the entire project.
    Attributes:
        __nb_objects (int): Number of objects created.
        id (int): Unique identifier for each instance.
    Methods:
        __init__(self, id=None)
        to_json_string(list_dictionaries)
        from_json_string(json_string)
        save_to_file(list_objs)
        create(**dictionary)
        load_from_file()
        save_to_file_csv(list_objs)
        load_from_file_csv()
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes the class attributes.
        Args:
            id (int): Unique identifier for the instance. 
            If not provided, it will be automatically assigned.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of a list of dictionaries.
        Args:
            list_dictionaries (list): List of dictionaries containing attributes of objects.

        Returns:
            str: JSON string representation of the input list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns a list of dictionaries from its JSON string representation.
        Args:
            json_string (str): JSON string representation of a list of dictionaries.

        Returns:
            list: List of dictionaries containing attributes of objects.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of a list of objects to a file.
        Args:
            list_objs (list): List of objects to be serialized and saved to the file.

        Raises:
            TypeError: If list_objs is not a list.
        """
        if not isinstance(list_objs, list):
            raise TypeError("list_objs must be a list")
        fname = cls.__name__ + ".json"
        content = [obj.to_dictionary() for obj in list_objs]

        with open(fname, "w") as jfile:
            jfile.write(cls.to_json_string(content))

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.
        Args:
            **dictionary: Double asterisk (**) indicates that any number 
            of keyword arguments can be passed.

        Returns:
            object: Instance of the class with attributes set according to 
            the provided dictionary.
        """
        if cls.__name__ == "Rectangle":
            mod = Rectangle(1, 1)  # Default values, width=1, height=1
        elif cls.__name__ == "Square":
            mod = Square(1)  # Default value, size=1
        mod.update(**dictionary)
        return mod

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances from a JSON file.
        Returns:
            list: List of instances created from the data stored in 
            the JSON file.

        Raises:
            FileNotFoundError: If the file with the class name + ".json"
            does not exist.
        """
        fname = cls.__name__ + ".json"

        try:
            with open(fname, encoding='utf8') as jfile:
                content = cls.from_json_string(jfile.read())
        except FileNotFoundError:
            return []

        instances = [cls.create(**instance) for instance in content]
        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes a list of objects in CSV format and saves them to a file.
        Args:
            list_objs (list): List of objects to be serialized and saved 
            to the CSV file.

        Raises:
            TypeError: If list_objs is not a list.
        """
        if not isinstance(list_objs, list):
            raise TypeError("list_objs must be a list")
        fname = cls.__name__ + ".csv"

        with open(fname, "w", newline='') as cfile:
            writer = csv.writer(cfile)
            if list_objs is None:
                return
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow(
                        [obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes objects from a CSV file and returns a list 
        of instances.
        Returns:
            list: List of instances created from the data stored 
            in the CSV file.
        """
        fname = cls.__name__ + ".csv"

        with open(fname, "r") as cfile:
            if cls.__name__ == "Rectangle":
                reader = csv.DictReader(
                    cfile, fieldnames=['id', 'width', 'height', 'x', 'y'])
            elif cls.__name__ == "Square":
                reader = csv.DictReader(
                    cfile, fieldnames=['id', 'size', 'x', 'y'])

            instances = []
            for instance in reader:
                instance = {x: int(y) for x, y in instance.items()}
                temp = cls.create(**instance)
                instances.append(temp)

        return instances
