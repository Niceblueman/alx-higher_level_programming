import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_width(self):  # Testing rectangle width getter
        r = Rectangle(20, 10)
        self.assertEqual(20, r.width)

    def test_height(self):  # Testing the height getter
        r = Rectangle(20, 10)
        self.assertEqual(10, r.height)

    def test_x(self):  # Testing the x getter
        r = Rectangle(20, 10, 2)
        self.assertEqual(2, r.x)

    def test_y(self):  # Testing the y getter
        r = Rectangle(20, 10, 0, 2)
        self.assertEqual(2, r.y)

    def test_rectangle_id(self):  # Testing the id of the rectangle
        r1 = Rectangle(1, 3, 0, 0, 12)
        self.assertEqual(12, r1.id)

    def test_wrong_width_type(self):  # Testing wrong type for width
        with self.assertRaises(TypeError):
            Rectangle("w", 5)

    def test_wrong_height_type(self):  # Testing wrong type for height
        with self.assertRaises(TypeError):
            Rectangle(1, "h")

    # Other test cases with changes...

    def test_area(self):  # Testing the rectangle area
        r1 = Rectangle(12, 2)
        self.assertEqual(r1.area(), 24)

    def test_update_id(self):  # Testing the update id
        r1 = Rectangle(10, 1)
        r1.update(id=12)
        self.assertEqual(12, r1.id)

    def test_update_width(self):  # Testing update width
        r1 = Rectangle(1, 2)
        r1.update(width=12)
        self.assertEqual(12, r1.width)

    def test_update_height(self):  # Testing update height
        r1 = Rectangle(1, 3)
        r1.update(height=4)
        self.assertEqual(4, r1.height)

    def test_update_x(self):  # Testing update x
        r1 = Rectangle(1, 2)
        r1.update(x=5)
        self.assertEqual(5, r1.x)

    def test_update_y(self):  # Testing update y
        r1 = Rectangle(1, 2)
        r1.update(y=6)
        self.assertEqual(6, r1.y)

    def test_to_dict(self):  # Testing to dict function return value
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.to_dictionary(),
                         {'height': 2, 'width': 1, 'id': r1.id, 'x': 0, 'y': 0})
