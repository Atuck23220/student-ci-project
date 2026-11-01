import unittest
from multiply_num import multiply, subtract


class TestMultiply(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(multiply(2, 4), 8)

    def test_negative_number(self):
        self.assertEqual(multiply(-3, 5), -15)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(7, 0), 0)

class TestSubtract(unittest.TestCase):

    def test_positive_result(self):
           self.assertEqual(subtract(10, 4), 6)

    def test_negative_result(self):
           self.assertEqual(subtract(3, 8), -5)

    def test_subtract_zero(self):
           self.assertEqual(subtract(7, 0), 7)


if __name__ == "__main__":
    unittest.main()
