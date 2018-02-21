# Review of Functions

## What are Functions?
Functions are reusable bits of code. They allow us to repeat ourselves less and therefore prevent bugs.

Functions have the following:
- A def statement that allows us to define our function.
- A body of our code we can write our code in it.
- A return value - that gives us a value to save

Functions take in parameters/arguments. Parameters are the variables inside the function. Arguments are the value passed into the function.

Here is a program that finds the square of a number.
```python
# Define the function
def square(x):  # Define the function
    """Returns the square of a number""" # Docstring
    y = x ** 2  # Body
    return y  # Return Statement


result = square(x=3)  # Call the function
print(result)  # Print out the result
````
In this example x is the variable inside of the function and therefore the parameter. 3 is the argument.
