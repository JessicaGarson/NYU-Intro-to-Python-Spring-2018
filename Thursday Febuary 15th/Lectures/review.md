# Review

## A note
Make sure we are working in groups for the group activity. This is a way we can all as a class get better.

## Variables
Variables are containers of information.

```python
name = 'Jessica'
age = 32
city = 'Brooklyn'
```

## Data Types
The three data types are as follows:
- strings
- integers
- floating point numbers

## Quotes on strings
You can use single or double quotes for strings. Triple quotes for long strings.

## Slicing
A few folks had issues because they weren't slicing a string.

```python
phone_number = '3017041328'
area_code = phone_number[0:3]
second_part = phone_number[3:6]
third_part = phone_number[6:]
format_num = '({})-{}-{}'.format(area_code, second_part, third_part)
print(format_num)
```

## Input
The input() function allows us to ask a question of a user. Keep in mind this always returns a string so if you need this to be another data type you will have to convert it.

## String Formatting
String formatting is like mad libs. You can insert in variables into strings.

```python
print('Hi {}, you are {} years old and you live in Brooklyn'.format(name, age, city))
```

## Conditionals
```
if condition:
    do something
elif other_condition:
    do something else
else:
    do another thing
```

```python
if raining == 'yes':
  print 'Better bring an umbrella!'
elif raining == 'maybe later today':
  print 'Better bring an umbrella, just in case'
else:
  print 'No umbrella today!'
```

## Python 2 instead of Python 3
Some students had issues of having trouble with needing to type python3.6 instead of python. To correct this [I recommend setting up alias for it](https://stackoverflow.com/questions/18425379/how-to-set-pythons-default-version-to-3-3-on-os-x).

## Breaking Up Long Lines
You can use \ to do so like this:

```python
open(self.full_path, 'r') as input, \
            open(self.output_csv, 'ab') as output:
```
