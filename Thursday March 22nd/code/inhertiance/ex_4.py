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
