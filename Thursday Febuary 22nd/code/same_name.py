name = 'Kelly'


def hello():
    global name
    name = 'Jess'
    return 'Hello {}'.format(name)


def hi():
    name = 'Alex'
    return 'Hi {}'.format(name)


print(name)  # Kelly
print(hello())  # Hello Jess
print(name)  # Hello Jess
print(hi())  # Hi Alex
