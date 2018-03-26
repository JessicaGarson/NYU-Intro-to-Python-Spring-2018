# Steps to Turning a Hangman Game into a Class Based Version

The way that I like to think of classes is that's another pattern of thinking of your code so that's a bit more reusable and you repeat yourself a bit. While the perfect use case is something like a game that has many different characters each that have things like health points and things like that.

This guide will walk you through how to take the code you have and turn it into a classed based version.

## Original code
This code was written by Andy. 
```python
guesses = 0
guessed_letters = []
word = "dorito"


while guesses < 5:
    guess = input("Hi. Please guess a letter.")

    if set(word).intersection(set(guessed_letters)) == set(word):
        break

    if guess in word and guess not in guessed_letters:
        print("Correct!")
        guessed_letters.append(guess)
        print("So far you've used ", guessed_letters, "as letters.")
        print("You've got",5-guesses,"guesses left.")

    elif guess not in word and guess not in guessed_letters:
        guesses += 1
        print("Wrong!")
        guessed_letters.append(guess)
        print("So far you've used ", guessed_letters, "as letters.")
        print("You've got",5-guesses,"guesses left.")

    elif guess in guessed_letters:
        print("You've already guessed that letter, please guess again.")

    else:
        print("ERROR")

if set(word).intersection(set(guessed_letters)) == set(word):
    print("You won!")
else:
    print("You lost!")
```

## Step 1 - Define Your Class
Create a class and call it hangman.

```python
class Hangman():
```
## Step 2: Create the Constructor Method
From here you can define your starting variables

```python
def __init__(self, word, guesses=0,   guessed_letters=[]):
      self.word = word
      self.guesses = guesses
      self.guessed_letters = guessed_letters
      self.word = word
```

## Step 2 - Adding the Guesses Less Than 5 Method
Let's take the code you wrote for what to do if your guesses are less than 5 and turn that into a function.

```python
def guesses_less_than_5(self, word, guesses, guessed_letters):
      while guesses < 5:
          guess = input("Hi. Please guess a letter.")

          if set(word).intersection(set(guessed_letters)) == set(word):
              break

          if guess in word and guess not in guessed_letters:
              print("Correct!")
              guessed_letters.append(guess)
              print("So far you've used ", guessed_letters, "as letters.")
              print("You've got", 5-guesses, "guesses left.")

          elif guess not in word and guess not in guessed_letters:
              guesses += 1
              print("Wrong!")
              guessed_letters.append(guess)
              print("So far you've used ", guessed_letters, "as letters.")
              print("You've got", 5-guesses, "guesses left.")

          elif guess in guessed_letters:
              print("You've already guessed that letter, please guess again.")

          else:
              print("ERROR")
```
## Step 3 - Set Intersection
Let's take the code that takes the set intersection and turn that into a method.

```python
def set_intersection(self, word, guesses, guessed_letters):
      if set(word).intersection(set(guessed_letters)) == set(word):
          print("You won!")
      else:
          print("You lost!")
```

## Tying it together
For this you will use a main function to tie things together. To tie it together.

```python
def main():
    dorrito = Hangman('dorito')
    dorrito.guesses_less_than_5(word=dorrito.word, guesses=dorrito.guesses, guessed_letters=dorrito.guessed_letters)
    dorrito.set_intersection(word=dorrito.word, guesses=dorrito.guesses, guessed_letters=dorrito.guessed_letters)

if __name__ == "__main__":
  main()
```

## Full code
```python
class Hangman():
    def __init__(self, word, guesses=0, guessed_letters=[]):
        self.word = word
        self.guesses = guesses
        self.guessed_letters = guessed_letters
        self.word = word

    def guesses_less_than_5(self, word, guesses, guessed_letters):
        while guesses < 5:
            guess = input("Hi. Please guess a letter.")

            if set(word).intersection(set(guessed_letters)) == set(word):
                break

            if guess in word and guess not in guessed_letters:
                print("Correct!")
                guessed_letters.append(guess)
                print("So far you've used ", guessed_letters, "as letters.")
                print("You've got", 5-guesses, "guesses left.")

            elif guess not in word and guess not in guessed_letters:
                guesses += 1
                print("Wrong!")
                guessed_letters.append(guess)
                print("So far you've used ", guessed_letters, "as letters.")
                print("You've got", 5-guesses, "guesses left.")

            elif guess in guessed_letters:
                print("You've already guessed that letter, please guess again.")

            else:
                print("ERROR")

    def set_intersection(self, word, guesses, guessed_letters):
        if set(word).intersection(set(guessed_letters)) == set(word):
            print("You won!")
        else:
            print("You lost!")


def main():
    dorrito = Hangman('dorito')
    dorrito.guesses_less_than_5(word=dorrito.word, guesses=dorrito.guesses, guessed_letters=dorrito.guessed_letters)
    dorrito.set_intersection(word=dorrito.word, guesses=dorrito.guesses, guessed_letters=dorrito.guessed_letters)


if __name__ == "__main__":
    main()
```

## So this was a lot of work, why do this?
While this might not be the best example for object oriented programming, if you had a lot of moving pieces or had like 5 or 6 words you wanted to run the same methods on this would be a more robust way to go about doing this and rewrite the same bits of code less.
