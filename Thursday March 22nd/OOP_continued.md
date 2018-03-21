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
