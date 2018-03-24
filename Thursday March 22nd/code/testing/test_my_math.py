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
        self.assertEqual(result, 'abc def')


class TestSubtract(unittest.TestCase):
    """
    Test the subtract function from the my_math.py program
    """
    def test_subtract_integers(self):
        result = my_math.subtract(3, 1)
        self.assertEqual(result, 0)

    def test_subtract_floats(self):
        result = my_math.subtract(1.0, 0.5)
        self.assertEqual(result, 0.5)

    def test_subtract_strings(self):
        self.assertRaises(TypeError, my_math.subtract, ("xyz", "z"))

# Add a class for testing the multiply function

# Add a class for testing divide function


if __name__ == '__main__':
    unittest.main()
