import unittest
from models.base import Base
from models.square import Square
import json
""" unitest base """


class TestBase(unittest.TestCase):
    def test_id(self):  # initialise an instance of the base class with no id
        b = Base()
        self.assertEqual(1, b.id)

    def test_custom_id(self):  # initialise an instance with id > 0
        b = Base(12)
        self.assertEqual(12, b.id)

    def test_id_with_negative(self):  # initialise instance with id < 0
        b = Base(-2)
        self.assertEqual(-2, b.id)

    def test_id_with_string(self):  # initialise instance with id is string
        b = Base("Base")
        self.assertEqual("Base", b.id)

    def test_id_with_list(self):  # initialise instance with id is list
        b = Base([1, 3, 6])
        self.assertEqual([1, 3, 6], b.id)

    def test_id_with_tuple(self):  # initialise instance with id is tuple
        b = Base((1, 3))
        self.assertEqual((1, 3), b.id)

    def test_id_with_dict(self):  # initialise instance with id is dict
        b = Base({'id': 12})
        self.assertEqual({'id': 12}, b.id)

    def test_to_and_from_json(self):  # test to_json_string and from_json_string
        sq = Square(9)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(type(json_string), str)
        self.assertEqual(json.loads(json_string), [
                         {"id": 9, "y": 0, "size": 9, "x": 0}])
        json_list = Base.from_json_string(json_string)
        self.assertEqual(json_list, [{"id": 9, "y": 0, "size": 9, "x": 0}])

    def test_to_json_None(self):  # test to_json_string with None
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_empty(self):  # test to_json_string with an empty list
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")
