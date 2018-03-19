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


if __name__ == "__main__":
    main()
