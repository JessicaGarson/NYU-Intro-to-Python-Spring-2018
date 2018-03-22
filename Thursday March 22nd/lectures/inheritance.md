# Object Oriented Programming Continued
On Monday we discussed the following concepts
1. Object oriented programming
2. The difference between objects and classes
3. The basic syntax of classes
4. How there can be class and instance variables.

## Let's talk through some examples
```python
class Customer(object):
    """A customer of ABC Bank with a checking account. Customers have the
    following properties:

    Attributes:
        name: A string representing the customer's name.
        balance: A float tracking the current balance of the customer's account.
    """

    def __init__(self, name, balance=0.0):
        """Return a Customer object whose name is *name* and starting
        balance is *balance*."""
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount*
        dollars."""
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        """Return the balance remaining after depositing *amount*
        dollars."""
        self.balance += amount
        return self.balance
```

# Inheritance
We already know this word. What does it mean in terms of biology?

In programming, this isn't too far off too. Inheritance helps us organize classes into a hierarchy. Therefore classes can inherit attributes and behavior from classes above in the hierarchy.

## Parents and children
One example is if we had a parent class called Parent that has class variables for last_name, height, and eye_color that the child class Child will inherit from the Parent.

Child classes can also called subclasses. Because of the fact that the child is inheriting, we can reuse code which is pretty nifty.

Let's walk through this example that shows us how variables are being pass down to a child class.
```python
class Fam:
    def __init__(self, first_name, last_name='Garson',
                 hair='brown', tounge_roll=True):
        self.first_name = first_name
        self.last_name = last_name
        self.hair = hair
        self.tounge_roll = tounge_roll

    def vacation(self):
        print('We go swimming on the lake every year during our vacation')

    def dinner(self):
        print('Family dinner is at 7pm every night')


class Bro(Fam):
    pass


alan = Bro('Alan')
print('{} {}'.format(alan.first_name, alan.last_name))
print(alan.hair)
print(alan.tounge_roll)
alan.vacation()
alan.dinner()
```

So what if we adapt the code to give the bro class a method. Can only the child class run that code?  

```python
class Fam:
    def __init__(self, first_name, last_name='Garson',
                 hair='brown', tounge_roll=True):
        self.first_name = first_name
        self.last_name = last_name
        self.hair = hair
        self.tounge_roll = tounge_roll

    def vacation(self):
        print('We go swimming on the lake every year during our vacation')

    def dinner(self):
        print('Family dinner is at 7pm every night')


class Bro(Fam):

    def has_kids(self):
        print('I have 2 children')


def main():
    alan = Bro('Alan')
    print('{}   {}'.format(alan.first_name, alan.last_name))
    print(alan.hair)
    print(alan.tounge_roll)
    alan.vacation()
    alan.dinner()
    jess = Fam('Jess')
    jess.vacation()
    alan.has_kids()
    # Can we run this?
    # jess.has_kids()


if __name__ == "__main__":
    main()
```

## Overriding the parent class
If we add another method called the same thing as another method in the child class we can override the parent method. Let's check this out in an example.

```python
class Fam:
    def __init__(self, first_name, last_name='Garson',
                 hair='brown', tounge_roll=True):
        self.first_name = first_name
        self.last_name = last_name
        self.hair = hair
        self.tounge_roll = tounge_roll

    def vacation(self):
        print('We go swimming on the lake every year during our vacation')

    def dinner(self):
        print('Family dinner is at 7pm every night')


class Bro(Fam):

    def has_kids(self):
        print('I have 2 children')

    def dinner(self):
        print('Family dinner is at 6pm every night')


def main():
    alan = Bro('Alan')
    print('{}   {}'.format(alan.first_name, alan.last_name))
    print(alan.hair)
    print(alan.tounge_roll)
    alan.vacation()
    alan.dinner()
    jess = Fam('Jess')
    jess.vacation()
    alan.has_kids()
    jess.dinner()
    alan.dinner()


if __name__ == "__main__":
    main()
```
## Super!
With the super() function, you can gain access to inherited methods that have been overwritten in a class object.

When we use the super() function, we are calling a parent method into a child method to make use of it. For example, we may want to override one aspect of the parent method with certain functionality, but then call the rest of the original parent method to finish the method. This is most commonly used with the `__init__` method.

In a program that grades students, we may want to have a child class for Weighted_grade that inherits from the Grade parent class. In the child class Weighted_grade, we may want to override a calculate_grade() method of the parent class in order to include functionality to calculate a weighted grade, but still keep the rest of the functionality of the original class. By invoking the super() function we would be able to achieve this.

Example:
```python
class Fam:
    def __init__(self, first_name, last_name='Garson',
                 hair='brown', tounge_roll=True):
        self.first_name = first_name
        self.last_name = last_name
        self.hair = hair
        self.tounge_roll = tounge_roll

    def vacation(self):
        print('We go swimming on the lake every year during our vacation')

    def dinner(self):
        print('Family dinner is at 7pm every night')


class Bro(Fam):
    def __init__(self, city='boston'):
        self.city = city
        super().__init__(self)

    def has_kids(self):
        print('I have 2 children')

    def dinner(self):
        print('Family dinner is at 6pm every night, with his two kids')


def main():
    kelly = Bro()

    # Initialize first name
    kelly.first_name = 'Kelly'

    # Use parent __init__() through super()
    print('{} {}'.format(kelly.first_name, kelly.last_name))

    # Use child __init__() override
    print(kelly.city)

    # Use parent swim() method
    kelly.vacation()


if __name__ == "__main__":
    main()
```
## Multiple Inheritance
Multiple inheritance is when a class can inherit attributes and methods from more than one parent class. This can allow programs to reduce redundancy, but it can also introduce a certain amount of complexity as well as ambiguity, so it should be done with thought to overall program design.

```python
class Fam:
    def __init__(self, first_name, last_name='Garson',
                 hair='brown', tounge_roll=True):
        self.first_name = first_name
        self.last_name = last_name
        self.hair = hair
        self.tounge_roll = tounge_roll

    def vacation(self):
        print('We go swimming on the lake every year during our vacation')

    def dinner(self):
        print('Family dinner is at 7pm every night')


class Bro(Fam):
    def __init__(self, city='boston'):
        self.city = city
        super().__init__(self)

    def has_kids(self):
        print('I have 2 children')

    def dinner(self):
        print('Family dinner is at 6pm every night, with his two kids')


class Cat:

    def community(self):
        print("I live with the fam.")


class Dog:

    def protect_fam(self):
        print('I protect the fam')


class Pets(Cat, Dog):
    pass


def main():
    great_barrier = Pets()
    great_barrier.community()
    great_barrier.protect_fam()


if __name__ == "__main__":
    main()
```
