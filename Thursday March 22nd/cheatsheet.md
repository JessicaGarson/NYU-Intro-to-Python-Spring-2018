# Cheatsheet
A one pager on most of the major concepts we've covered.

## Command line
pwd - where am I?
cd - change directory
cd .. - go up one directory
ls - list contents
ls - lrt - list contents with more context

```bash
pwd
cd Documents
cd ..
ls
ls -lrt
```

## String formatting
String formatting is like mad libs. You can insert in variables into strings.

```python
print('Hi {}, you are {} years old and you live in Brooklyn'.format(name, age, city))
```

## Functions
Functions are like a mini program inside of your program that contain inside reusable code. They are only run when they are called and they prevent errors and bugs in our code by avoiding duplication.

The basic syntax of a function is this:

```
def something(arguments):
  do something

# to call the function
something(argument=parameter)
```

```python
def hello(name):
  print('Hello {}'.format(name))

hello(name='Jess')
hello(name='Michelle')
```

## Lists
- Lists are containers that can hold multiple pieces of information.
- Lists are commonly used to hold strings (ex: list of attendees’ names) or numbers (ex: number of attendees for each class).
- Sometimes called arrays.

```python
colors = ['red', 'blue', 'green']
```

## Sets
Sets have been defined as a unordered bag of values. Sets have curly brackets around them.

```python
colors = {'orange', 'blue', 'teal', 'purple'}
```

## Tuples
Tuples are immutable. Meaning they are an unchangeable, ordered sequence of elements. While they look similar to lists, the difference is you can't change these.

```python
days_of_the_week = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
```

## Dictionaries
Dictionaries have two components: a key and its corresponding value.

Think of it like a phone book or contact list! If you know my name, (key) you can look up my number (value)

The basic syntax is as follows:
```
key: value
```
```python
handles = {'Michael': 'michaelshore93', 'Daniel': 'danielrein', 'Andrew': 'andyschneider85'}
```

## Loops
Loops allow us to to automate and repeat tasks in a very short amount of time.

### For loop
A for loop lets you use each item one at a time, which is great for performing actions a certain number of times.

```
For each item:
		do something with that item
```

```python
days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for day in days_of_the_week:
    print(day)
```

### While loop
You can think of the while loop as a repeating conditional statement. After an if statement, the program continues to execute code, but in a while loop, the program jumps back to the start of the while statement until the condition is False.

```
while a condition is True:
  do something
```

```python
bread = 35
while bread >= 2:
    print("I'm making a sandwich")
    bread = bread - 2
```
## Start a virtualenv
They are a fresh start without the weight of the baggage of your computer so you can install packages in isolation.

For macs:

```
virtualenv newvenv
source newvenv/bin/activate
```

For PCs:
```
virtualenv newenv
. .\newenv\Scripts\activate.ps1
```
## Start a jupyter notebook
You will need to make sure you have jupyter installed to your environment.

```
pip install jupyter
jupyter notebook
```

## Classes
Classes - a blueprint of an object. Think of this as a blueprint of a house that's about to be built.

Objects - an instance of a class.

```python
class Student:
    def __init__(self, name):
        self.name = name

    def classroom(self):
        print('{} is in class listening to lectures from Jess and pair programming'.format(self.name))

    def frustration(self):
        print('{} is getting a lot of syntax errors, cut and pasting all the things from stack overflow'.format(self.name))

    def happiness(self):
        print('{} is thinking now - OMG, I solved the error I am so happy and smart'.format(self.name))


def main():
    yasha = Student('Yasha')
    yasha.classroom()
    yasha.frustration()
    yasha.happiness()
    joyce = Student('Joyce')
    joyce.classroom()
    joyce.frustration()
    joyce.happiness()
```
## Commit to GitHub
To commit to GitHub use the following steps:

```bash
git add .
git commit -m "adding new changes"
git push
```
