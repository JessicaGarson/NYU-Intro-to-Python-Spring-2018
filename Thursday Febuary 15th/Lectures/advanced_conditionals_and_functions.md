# Advanced Conditionals and Functions

# Advanced Conditionals
We're going to dive into some advanced uses of conditionals

## In
The in keyword, when used with a conditional, tells you whether some text appears in a string.

```python
if 'Messica Arson' in article:
  print('It is so awesome Jess got her DJ project in this article')
```

## And  
Using the and keyword, both conditions must be true for the print statement to run.

```python
if homework_turned_in == 0 and homework_assigned == 1:
  print('Jess is sad')
```

## Or
Using the or keyword, either condition could be true for the print statement to run.
```python
if state == 'MD' or state == 'DC' or state == 'DE' or state == 'VA' or state == 'PA':
  print('You are from the Mid-Atlantic region')
```

## Nested Conditionals
```python
if state == 'NY':
  print('You are in NY')
elif state == 'NJ':
  print('You are in NJ')
elif state == ('CT')
  print('')
else:
  print('We only service the New York Region')

  if state == 'PA':
    print('You are welcome to visit us still')
  elif state == 'CA':
    print('Wow, that would be quite the drive')
```

## Comments
Comments are code that doesn't run.

```python
# I am a comment, I don't run
print('hello world!')
```

## General Advice
If you are repeating yourself, you are likely doing it wrong.

## Functions
We've already been working with them but we can create our own!

```python
tweet = 'My Professor @JessicaGarson is so awesome'
len(tweet)
tweet_length = len(tweet)
print(tweet)
input("What's your favorite video game? ")
```

## So What Are Functions
They are like a mini program inside of your program that contain inside reusable code. They are only run when they are called and they prevent errors and bugs in our code by avoiding duplication.

## Let's Write a Function
We can create a function for our hello world program:
```python
def hello_world():
  print('Hello World!')

hello_world()
```

All functions have what's know as a def statement that allows us to define our function. And inside of the body of our code we can write our code in it.

```python
def hello(name):
  print('Hello {}'.format(name))

hello('Jess')
hello('Michelle')

hello(name='Jess')
hello(name='Michelle')
```

```python
def profile_info(username, followers):
    print('Username: {}'.format(username))
    print('Followers:  {}'.format(followers))

# Call function with parameters assigned as above
profile_info('sammyshark', 945)

# Call function with keyword arguments
profile_info(username='sammyshark', followers=945)
profile_info(followers=945, username='sammyshark')
```

## Arguments/Parameters
Functions take in parameters/arguments. Parameters are the variables inside the function. Arguments are the value passed into the function.

```python
def add_numbers(x, y, z):
    a = x + y
    b = x + z
    c = y + z
    print(a, b, c)

add_numbers(1, 2, 3)
```

## Return Value
The return value is allows us to specify if your function should output a value.

You should end your function with a return statement if the function should output something. Without the return statement, your function will return an object None.

This is what was happening for the previous functions we wrote with the print statements. The None value represents a lack of a datatype.

We can have multiple return values for a function as well.

```python
def plus_one(number):
  return number + 1

plus_one(number=3)
```

```
def something(parameter):
    # your code goes here
    return value
```

```python
def square(x):
    y = x ** 2
    return y

result = square(3)
print(result)

```

## Docstrings
Docstrings help us document what the code does.
```python
def plus_one(number):
  """Adds one to the number"""
  return number + 1

print(plus_one(number=4))
```

## Local and Global Scope
Variables assigned in a function are only local to that function. Variables assigned outside of all functions exist in the global scope. You can have variables named the same thing in different functions that are different variables.

```python
import datetime

time = datetime.datetime.now() # global

def greeting(time):
  name = 'Jess' # local and temporary
  print('Hello {}, the time is {}'.format(name, time))

# print(name)
greeting(time=time)
```

```python
import datetime

time = datetime.datetime.now() # global
name = 'James'


def greeting(time):
  global name
  name = 'Jess'
  print('Hello {}, the time is {}'.format(name, time))

print(name)
greeting(time=time)
print(name)
```
## Why Not Have Everything Be Global

This allows us to separate out the code so that is easier for debugging. So if something is going wrong you can take a look at the function, instead of looking through the entire program.

## Main Functions
Many other programming languages require a main function in order to execute. Including a main() function, though not required, can structure our Python programs in a logical way that puts the most important components of the program into one function. It can also make our programs easier for non-Python programmers to read.

In Python, '__main__' is the name of the scope where top-level code will execute. When a program is run from standard input, a script, or from an interactive prompt, its __name__ is set equal to '__main__'.

```python
def hello():
    print('Hello, World!')

def main():
    print('This is the main function.')
    hello()

# main()

if __name__ == '__main__':
    main()

# if __name__ == '__main__':
  # hello()
```

## Your Functions They Do Too Much
To make your code more reusable and less error prone. Try to make it so your functions only do one thing at a time. This will allow your code to be more testable in the future.
