a = 6


def oneplus():
    global a
    a = 1 + a
    return a


def twoplus():
    global a
    a = 2 + a
    return a


print(a)
print(oneplus())
print(twoplus())
print(a)
