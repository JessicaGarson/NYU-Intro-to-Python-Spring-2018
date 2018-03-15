# The os library
The os library in python allows us to interact with our operating system.

## Interacting with our os
Remember the second class where we got to know the command line let's do this with python

## Where are we
The pwd equivalent is as follows:
```python
import os

current_directory = os.getcwd()
print(os.getcwd()) # equivalent to pwd
```

## Let's go up a directory
Remember cd .. that allows us to up a directory. Let's do this with python.
```python
os.chdir("..") # equivalent to cd ..
print(os.getcwd())
os.chdir(current_directory)
print(os.getcwd())
```

## Is this file or a directory
```python
print(os.path.isdir("file.txt"))
print(os.path.isfile("file.txt"))
```
## Glob for pattern matching
The glob library allows us to match files
```python
from glob import glob
```

## Let's go through our files
Let's see all our text files
```python  
files = glob("*.txt")
print(files)
first_file = open(files[0], "r")
contents_one = first_file.read()
print(contents_one)
second_file = open(files[1], "r")
print(contents_two)
```

## Let's scan the directory
We can use the os.scandir to quickly list the files and folders in the directory.
```python
folders = []
files = []

for entry in os.scandir('/Users/jessicagarson/Documents/NYU-Intro-to-Python-Spring-2018/Thursday March 15th/code_and_files'):
    if entry.is_dir():
        folders.append(entry.path)
    elif entry.is_file():
        files.append(entry.path)
        
print('Folders:\n{}'.format(folders))
print('Files:\n{}'.format(files))
```
