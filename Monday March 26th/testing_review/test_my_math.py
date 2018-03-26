import my_math
import unittest


class TestAdd(unittest.TestCase):
    """
    Test the add function from the my_my_math.py program
    """

    def test_add_integers(self):
        """
        Test that the addition of two integers returns the correct total
        """
        result = my_math.add(1, 2)
        self.assertEqual(result, 3)

    def test_add_floats(self):
        """
        Test that the addition of two floats returns the correct result
        """
        result = my_math.add(10.5, 2)
        self.assertEqual(result, 12.5)

    def test_add_strings(self):
        """
        Test the addition of two strings returns the two string as one
        concatenated string
        """
        result = my_math.add('abc', 'def')
        self.assertEqual(result, 'abcdef')


class TestSubtract(unittest.TestCase):
    """
    Test the subtract function from the my_math.py program
    """
    def test_subtract_integers(self):
        result = my_math.subtract(3, 1)
        self.assertEqual(result, 2)

    def test_subtract_floats(self):
        result = my_math.subtract(1.0, 0.5)
        self.assertEqual(result, 0.5)

    def test_subtract_strings(self):
        self.assertRaises(TypeError, my_math.subtract, ('xyz', 'z'))

# Add a class for testing the multiply function


class TestMultiply(unittest.TestCase):
    """
    Test the multiply function from the my_math.py program
    """
    def test_multiply_integers(self):
        result = my_math.multiply(5, 2)
        self.assertEqual(result, 10)

    def test_multiply_floats(self):
        result = my_math.multiply(3.0, 1.5)
        self.assertEqual(result, 4.5)

    def test_multiply_strings_ints(self):
        result = my_math.multiply('trish', 3)
        self.assertEqual(result, 'trishtrishtrish')

    def test_multiply_strings(self):
        self.assertRaises(TypeError, my_math.multiply, ('yooo', 'hello'))


# Add a class for testing divide function
class TestDivide(unittest.TestCase):
    """
    Test the divide function from the my_math.py program
    """
    def test_divide_ints(self):
        result = my_math.divide(12, 6)
        self.assertEqual(result, 2)

    def test_divide_floats(self):
        result = my_math.divide(5, 2.5)
        self.assertEqual(result, 6)

    def test_divide_string(self):
        self.assertRaises(TypeError, my_math.divide, ('yooo', 'hello'))


if __name__ == '__main__':
    unittest.main()
