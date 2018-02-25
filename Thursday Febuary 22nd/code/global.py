a = 6


def oneplus():
    global a
    a = 1 + a
    return a


def twoplus():
    global a
    a = 2 + a
    return a


print(a)  # 6
print(oneplus())  # 7
print(twoplus())  # 9
print(a)  # 9
