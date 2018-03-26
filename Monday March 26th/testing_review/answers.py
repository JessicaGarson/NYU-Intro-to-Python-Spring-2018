import my_math
import unittest


class TestMultiply(unittest.TestCase):
    """
    Test the multiply function from the my_math.py program
    """
    def test_multiply_int_and_string(self):
        result = my_math.multiply('trish', 3)
        self.assertEqual(result, 'trishtrishtrish')


class TestDivide(unittest.TestCase):
    """
    Test the divide function from the my_math.py program
    """

    def test_divide_strings(self):
        self.assertRaises(TypeError, my_math.divide, ('w4jlw', '2432j2'))


if __name__ == '__main__':
    unittest.main()
