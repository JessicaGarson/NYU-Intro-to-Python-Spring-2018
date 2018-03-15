# File handling

## Basic syntax
```python
with open('states.txt', 'r') as states_file:
    states = states_file.read()

print(states)
```
What does this code do?

- You might notice a new word we haven't seen yet, with. With is a keyword that tells Python we're going to do something with a file we're about to open.
- When all commands within the indentation have been run, the file is closed automatically.
- open() is a built-in function that tells Python to open a file.
- It takes two arguments, a file name and a mode. he "mode" to open the file in, as a string.
- The different modes are as follows:
  1. 'r' : use for reading
  2. 'w' : use for writing
  3. 'x' : use for creating and writing to a new file
  4. 'a' : use for appending to a file
  5. 'r+' : use for reading and writing to the same file
- The as keyword creates a variable for your file handler. The variable in this example is states_file, but you could use any variable name you want.
- read() is a file method — a function that only works with file handlers.  In this example, the file handler is states_file. .read() will read the entire contents of the file. In line 2 above, I've saved it into the variable states.

We can turn this into a list. Using .split()

```python
with open('states.txt', 'r') as states_file:
    state_list = states_file.read().split('\n')

print(state_list)
```
## What about if we have a csv file?
Can we use the same syntax here?
```python
with open('name_score.csv', 'r') as f:
    name_score = f.read()
print(name_score)
```

## DictReader
The DictReader class basically creates a CSV object that behaves like a Python OrderedDict. It works by reading in the first line of the CSV and using each comma separated value in this line as a dictionary key. The columns in each subsequent row then behave like dictionary values and can be accessed with the appropriate key.
```python
import csv  
with open('name_score.csv') as csvfile:  
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row[Score])
```

## Writing files
```python
with open('file.txt', 'w') as f:
    f.write('This file now exists!')
    f.close()
```
In this code we are creating a file if it doesn't already exist. We are writing a the contents of the file and closing the connection to the file.
