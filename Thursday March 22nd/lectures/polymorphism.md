# Polymorphism
Polymorphism is simply the fact that we call the same method with different parameters and it can do different things.

## We already know this
This is something we've already been doing for most of the class.
```python
def times_3(a):
    return a * 3


print(times_3(a=3))
print(times_3(a='Jess'))
```
This function behaves differently with strings than it does with integers.

## What does this mean for object oriented programming?
For object-oriented programming in Python, this means that a particular object belonging to a particular class can be used in the same way as if it were a different object belonging to a different class.

Let's create the following example and run it as we have been for a bit now:
```python
class Shark():
    def swim(self):
        print("The shark is swimming.")

    def swim_backwards(self):
        print("The shark cannot swim backwards, but can sink backwards.")

    def skeleton(self):
        print("The shark's skeleton is made of cartilage.")


class Clownfish():
    def swim(self):
        print("The clownfish is swimming.")

    def swim_backwards(self):
        print("The clownfish can swim backwards.")

    def skeleton(self):
        print("The clownfish's skeleton is made of bone.")


sammy = Shark()
sammy.skeleton()

casey = Clownfish()
casey.skeleton()
```

## Polymorphism with Class Methods
We can use each of these different class types in the same way, we can first create a for loop that iterates through a tuple of objects. From there we can loop through without worrying which class type each object is.

```python
class Shark():
    def swim(self):
        print("The shark is swimming.")

    def swim_backwards(self):
        print("The shark cannot swim backwards, but can sink backwards.")

    def skeleton(self):
        print("The shark's skeleton is made of cartilage.")


class Clownfish():
    def swim(self):
        print("The clownfish is swimming.")

    def swim_backwards(self):
        print("The clownfish can swim backwards.")

    def skeleton(self):
        print("The clownfish's skeleton is made of bone.")


sammy = Shark()

casey = Clownfish()

for fish in (sammy, casey):
    fish.swim()
    fish.swim_backwards()
    fish.skeleton()
```

## Polymorphism with a function
We can also create a function that can take any object, allowing for polymorphism.


```python
class Shark():
    def swim(self):
        print("The shark is swimming.")

    def swim_backwards(self):
        print("The shark cannot swim backwards, but can sink backwards.")

    def skeleton(self):
        print("The shark's skeleton is made of cartilage.")


class Clownfish():
    def swim(self):
        print("The clownfish is swimming.")

    def swim_backwards(self):
        print("The clownfish can swim backwards.")

    def skeleton(self):
        print("The clownfish's skeleton is made of bone.")


def in_the_pacific(fish):
    fish.swim()


sammy = Shark()

casey = Clownfish()

in_the_pacific(sammy)
in_the_pacific(casey)
```
