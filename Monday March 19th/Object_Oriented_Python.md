# Object Oriented Python
So what is object oriented programming? Object oriented programming allows us to have reusable patterns of code. We do this so we can repeat ourselves less.

If our code is less repetitive, it is more readable and thus easier to maintain.

This is opposed to procedural programming which is where we have a set of instructions to follow. Older programming languages such as COBAL focus on this type programming. Object oriented programming focuses more on logic than specific instructions.

## But wait, I heard about functional programming what's that?
You may have heard of a different paradigm called functional programming and might be wondering what the difference is between that and object oriented programming.
[Here is a great article from CodeNewbie that explains the difference between the two](https://www.codenewbie.org/blogs/object-oriented-programming-vs-functional-programming).

## Classes and objects
The two core concepts of object oriented programming are classes and objects.

Classes - a blueprint of an object. Think of this as a blueprint of a house that's about to be built.

Objects - an instance of a class.

## This looks similar to functions
We have been working with functions for about a month now, we are building off of this concept.

## Classes
Everything we put inside a class is something that is common to a group of things.

```python
class Student:
    def classroom(self):
        print('in class listening to lectures from Jess and pair programming')

    def frustration(self):
        print('getting a lot of syntax errors, cut and pasting all the things from stack overflow')

    def happiness(self):
        print('OMG, I solved the error I am so happy and smart')
```

## Objects
An object is an instance of a class. In this example students in this class are the example.

Here we are saying Yasha is a student in this class and does the things above we defined has being things that students do.

```python
yasha = Student()
```

```python
class Student:
    def classroom(self):
        print('in class listening to lectures from Jess and pair programming')

    def frustration(self):
        print('getting a lot of syntax errors, cut and pasting all the things from stack overflow')

    def happiness(self):
        print('OMG, I solved the error I am so happy and smart')


def main():
    yasha = Student()
    yasha.classroom()
    yasha.frustration()
    yasha.happiness()


if __name__ == "__main__":
    main()
```

## Something is missing here!
We are missing what's known as a constructor method. The constructor method is used to initialize data. It is run as soon as an object of a class is instantiated. Also known as the `__init__` method.

We can use a name variable that we can use to assign names to objects.  

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

## Class and instance variables
We can assign variables to the class as well as to the instance.

```python
class Student:

    # Class variables
    institution = 'NYU'
    location = 'NYC'

    # Constructor method with instance variables name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method with instance variable followers
    def set_followers(self, followers):
        print('This student has {} GitHub followers'.format(followers))


def main():
    # First object, set up instance variables of constructor method
    andy = Student('Andy', 28)

    # Print out instance variable name
    print(andy.name)

    # Print out class variable location
    print(andy.location)

    # Second object
    george = Student('George', 29)

    # Print out instance variable name
    print(george.name)

    # Use set_followers method and pass followers instance variable
    george.set_followers(130)

    # Print out class variable animal_type
    print(george.institution)


if __name__ == "__main__":
    main()
```

## Resources
- [Beginner's Guide - Object Oriented Programming](https://dev.to/charanrajgolla/beginners-guide---object-oriented-programming)
- [Know thy Self - PyCon 2017](https://www.youtube.com/watch?v=byff9LhYXOg)
- [Classes and Inheritance](http://www.jesshamrick.com/2011/05/18/an-introduction-to-classes-and-inheritance-in-python/)
- [How my Dog learned Polymorphism](https://javaranch.com/campfire/StoryPoly.jsp)
