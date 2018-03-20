class Student:

    # Class variables
    insitution = 'NYU'
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
    print(andy.age)

    # Print out class variable location
    print(andy.location)

    # Second object
    george = Student('George', 29)

    # Print out instance variable name
    print(george.name)
    print(george.age)

    # Use set_followers method and pass followers instance variable
    george.set_followers(130)

    # Print out class variable animal_type
    print(george.insitution)


if __name__ == "__main__":
    main()
