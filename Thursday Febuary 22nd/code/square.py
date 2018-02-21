def square(x):  # Define the function
    """Returns the square of a number"""  # Docstring
    y = x ** 2  # body
    return y  # return


result = square(x=3)  # Call the function
print('{} is the square of {}'.format(result, x))
