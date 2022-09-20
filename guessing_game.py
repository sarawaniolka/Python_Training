# simple guessing game

from random import randint

# the computer gets a random number
number = randint(1, 10)

# asking for input
guess = input("Guess a number between 1 and  10: ")
guess = int(guess)

# comparing the input with the number
while guess != number:
    if guess > number:
        print("Your guess is too high!")
        guess = input("Guess a number between 1 and  10: ")
        guess = int(guess)
    else:
        print("Your guess is too low!")
        guess = input("Guess a number between 1 and  10: ")
        guess = int(guess)
print("Your guess is correct!")