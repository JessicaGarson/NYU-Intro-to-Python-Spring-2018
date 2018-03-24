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

    jess = Fam('Jess')
    jess.vacation()
    jess.city()


if __name__ == "__main__":
    main()
