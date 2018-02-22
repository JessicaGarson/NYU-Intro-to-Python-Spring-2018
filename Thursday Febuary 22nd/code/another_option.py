# Define function to check if name contains a vowel
def has_vowel():
    if set('aeiou').intersection(name.lower()):
        print('Your name contains a vowel.')
    else:
        print('Your name does not contain a vowel.')


if __name__ == '__main__':
    name = str(input('Enter your name: '))
    print('The name you entered is {}'.format(name))
    has_vowel()
