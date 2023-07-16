import unittest
import json
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_size(self):  # Testing square size getter
        sq = Square(20)
        self.assertEqual(20, sq.size)

    def test_x(self):  # Testing the x getter
        sq = Square(20, 2)
        self.assertEqual(2, sq.x)
        self.assertEqual(0, sq.y)

    def test_y(self):  # Testing the y getter
        sq = Square(20, 0, 2)
        self.assertEqual(2, sq.y)
        self.assertEqual(0, sq.x)

    def test_square_id(self):  # Testing the id of the square
        sq1 = Square(1, 0, 0, 12)
        self.assertEqual(12, sq1.id)

    def test_wrong_size_type(self):  # Testing wrong type for size
        with self.assertRaises(TypeError):
            Square("s")

    def test_wrong_x_type(self):  # Testing wrong type for x
        with self.assertRaises(TypeError):
            Square(2, "x", 0)

    def test_wrong_y_type(self):  # Testing wrong type for y
        with self.assertRaises(TypeError):
            Square(2, 0, "y")

    def test_size_negative(self):  # Testing negative value for size
        with self.assertRaises(ValueError):
            Square(-2)

    def test_size_zero(self):  # Testing zero value for size
        with self.assertRaises(ValueError):
            Square(0)

    def test_x_negative(self):  # Testing negative value for x
        with self.assertRaises(ValueError):
            Square(2, -1, 0)

    def test_y_negative(self):  # Testing negative value for y
        with self.assertRaises(ValueError):
            Square(2, 4, -7)

    def test_area(self):  # Testing for area()
        sq1 = Square(20)
        self.assertEqual(sq1.area(), 20 * 20)

    def test_str_overload(self):  # Testing the str overload
        sq = Square(10, 2, 3, 9)
        self.assertEqual(sq.__str__(), "[Square] (9) 2/3 - 10")

    def test_update(self):  # Test update function with *args
        sq1 = Square(1)
        sq1.update(2, 4)
        self.assertEqual(sq1.__str__(), "[Square] (2) 0/0 - 4")

    def test_update_kwargs(self):  # Test update() function with **kwargs
        sq1 = Square(1)
        sq1.update(size=7, y=1, id=12)
        self.assertEqual(sq1.__str__(), "[Square] (12) 0/1 - 7")

    def test_update_both(self):  # Test update() with both args and kwargs
        sq1 = Square(1)
        sq1.update(2, 4, **{'x': 3, 'y': 4})
        self.assertEqual(sq1.__str__(), "[Square] (2) 0/0 - 4")

    def test_create_dict_equal(self):  # Testing creating square is not equal
        sq1 = Square(1, 3, 5, 6)
        sq1_dict = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dict)
        self.assertNotEqual(sq1, sq2)

    def test_create_dict_is(self):  # Testing create squaree is (sq1 is sq2)
        sq1 = Square(1, 3, 5, 6)
        sq1_dict = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dict)
        self.assertIsNot(sq1, sq2)

    def test_save_to_file_none(self):  # Testing save to file none
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            content = json.load(f)
            self.assertEqual(content, [])

    def test_save_to_file_empty(self):  # Testing save to file empty list
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            content = json.load(f)
            self.assertEqual(content, [])

    def test_save_to_file_rect(self):  # Testing save to file with proper input
        Square.save_to_file([Square(1, 3, 4, 5)])
        with open("Square.json", "r") as f:
            content = f.read()
            self.assertEqual(json.loads(content), [{"id": 5,
                                                    "size": 1,
                                                    "x": 3, "y": 4}])

    # Testing save to file with no arguments
    def test_save_to_file_noargs(self):
        with self.assertRaises(TypeError):
            Square.save_to_file()

    def test_save_to_file_type(self):  # Testing save to file , format saved in
        Square.save_to_file([Square(1, 3, 4, 5)])
        with open("Square.json", "r") as f:
            content = f.read()
            self.assertEqual(str, type(content))

    # Testing load from file that doesn't exist
    def test_load_from_file_noexist(self):
        sq1 = Square(1)
        Square.save_to_file([sq1])
        list_output = Square.load_from_file()
        self.assertEqual(sq1.size, list_output[0].size)
