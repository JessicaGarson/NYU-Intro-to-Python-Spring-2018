# Expressions, Operators, Strings, Conditionals

## The Interactive Shell
The interactive shell, allows you to play around and experiment. Much of testing I do I do from the interactive shell.

Our text editor Atom, is where we write complete code.

## Expressions
Expressions are most basic kind of programming instruction in the language. Expressions consist of values (such as 2) and operators (such as +), and they can always evaluate (that is, reduce) down to a single value.
```python
2 + 2
5 - 3
3 * 7
22 / 7
2 + 3 * 20
```

Exponents look like this:
```python
2 ** 3
```

% is for modulus/remainder:
```python
22 % 8
```

// is for integer division/floored quotient:
```python
22 // 8
```

## Data Types
There are three data types in Python
- Intergers such as 1, 23, -32, 24, 234
- Floating point numbers or floats such as 1.23, 23.23, -4.32, 22.6
- Strings such as 'rwewe', '2si', 'hello', 'anything really'

## Variables
Variables are containers for information you can store text, numbers, or any other type of thing!
```python
name = 'Jess'
print(name)
```

## What's going on with the print function
```python
print('Hello World!')
```
The print() function will display the string value inside the parentheses on the screen. We are using the built in function of print which takes in a string as an argument.

## What's the difference between these two?
```python
print(name)
print('name')
```
One displays the variable name and one displays the word name as a string.

## What's a string?
Strings are combinations of characters. They can be letters, numbers, punctuation. They are anything you can make on the keyboard and then some and can include special characters, like tabs and newlines.

## You can spot a string by the quotes around them.
```python
print('Jess')
print("Jess")
```
It is preferred to use the single quotes but you can use double quotes. You just can't mix the types of quotes.

## Triple quotes for long strings
```python
tale_of_two_cites = '''It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we ..'''
```

## New line
There is a special character to use for a new line in a string.
```python
print('Hi, my name is: \nJessica')
```

## Tabs
There is also a special character to use for tabs
```python
print('Hi, my name is: \tJessica')
```

## Slicing
Slicing allows us to segment part of the variable we're working with. We're going to play around with slicing an see what happens.
```python
name[0:]
name[0]
name[1]
name[2]
name[3]
name[4]
name[0:4]
name[0:]
name[0:1]
name[0:3]
name[-4]
name[-3]
name[-2]
name[-1]
name[-4:-1]
```

## String formatting
I like to think of this like mad libs where we are creating sentences that we can insert variables into.

```python
hi = 'Hi my name is {}'.format(name)
print(hi)
age = 32
hi_with_age = 'hi my name {} and I am {} years old.'.format(name, age)
print(hi_with_age)
```

You can also do math inside of string formatting.

```python
tweet = 'My python class is so fun with @JessicaGarson as my instructor'
print(len(tweet))
print('That tweet is {} characters and you have {} remaining characters'.format(len(tweet), 240- len(tweet)))
```

## String Math
Some fun thing happen when you do math with strings.
```python
print('Jess' + 'Class')
print('Jess' * 3)
```

## Built in Functions for Strings
Functions are take arguments/parameters tell a function or method how to do their action, or what to do it to. A list of built in functions can be found [here](https://docs.python.org/3/library/functions.html).

## How long is my string?
```python
len(tale_of_two_cites)
tale_length = len(tale_of_two_cites)
```
The built in len function tells you how long a string is. In this example the function/action is len() and the argument/parameter is tale_of_two_cites.

## Find
Works like Ctrl-F in most programs but you get back the index(slice) of where the thing you are looking for is located.
```python
email = 'jlg17@nyu.edu'
print(email.find('@'))
```

## Replace
Works like Find+Replace in most programs.
```python
twitter = '@JessicaGarson'
print(twitter.replace('@', '#'))
```

## Upper and Lower
Turns a string into upper or lower case letters.

```python
print(twitter.upper())
print(twitter.lower())
```

## Count
```python
upper_tale = tale_of_two_cites.upper()
print(upper_tale.count('IT'))
```

## Input
```python
question = input("What's your name? ")
print(question)
```

## Conditionals
We use conditionals to compare two things .

## Operators for Comparison
```
==   These two things are equal
!=	 NOT! equal to
>	   Greater than
<	   Less than
>=   Greater than or equal to
<=   Less than or equal to
```

```python
1 == 2
2 != 3
5 > 4
3 < 100
4 >= 92
4 <= 5
```

## If Statement
The if statement evaluates whether a statement is true or false, and run code only in the case that the statement is true.

```python
space = 15
if space < 20:
  print('We still have spaces left')
```

## Else
If none of the conditions meet. Than do this.
```python
space = 21

if space < 20:
  print('We still have spaces left')
else:
  print('Sorry, we are full')
```

## Elif
If there is another condition that is met than do something else.

```
if condition:
    do something
elif other_condition:
    do something else
else:
    do another thing
```

```python
space = 19
if space < 20:
  print('We still have space left')
elif space == 20:
  print('We are just a capacity')
elif space >= 15:
  print('We are almost at capacity but we have a few spaces left')
else:
  print('Sorry, we are full')
```
