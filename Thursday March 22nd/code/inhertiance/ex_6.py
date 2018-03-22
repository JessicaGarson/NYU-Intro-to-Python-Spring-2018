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
