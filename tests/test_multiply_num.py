import unittest
from multiply_num import multiply


class TestMultiply(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(multiply(2, 4), 8)

    def test_negative_number(self):
        self.assertEqual(multiply(-3, 5), -15)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(7, 0), 0)


if __name__ == "__main__":
    unittest.main()
