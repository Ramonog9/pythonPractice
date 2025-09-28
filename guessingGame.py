import random
import time

guess = int(input("Welcome to the Guessing Game! You have 3 attempts to guess the correct number between 1 and 10. Press any number to start!"))
guesses_left = 3
correct_number = random.randint(1,10)

while guess != correct_number and guesses_left > 0:
    guess = int(input("What is your guess?"))
    if guess > correct_number:
        print("Guess lower")
    else:
        print("Guess higher")
    guesses_left -= 1
if guesses_left == 0:
    print("You're out of guesses! The correct number was:", correct_number)
else:
    print("You guessed correct!")