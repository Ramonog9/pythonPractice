import random
import time

guess = int(input("Welcome to the Guessing Game! You have 3 attempts to guess the correct number between 1 and 10. Press 0 to start!"))
catch = False
while guess != 0 and not catch:
    guess = int(input("Please press 0 to start the game!"))
    if guess == 0:
        catch = True
guesses_left = 3
time.sleep(3)
print("Choosing a number!")
correct_number = random.randint(1,10)
time.sleep(2)
print("I got my number! Bet you can't guess it!")

while guess != correct_number and guesses_left > 0:
    guess = int(input("What is your guess?"))
    if guess > correct_number:
        print("Guess lower")
    else:
        print("Guess higher")
    guesses_left -= 1
if guesses_left == 0 and guess != correct_number:
    print("You're out of guesses! The correct number was:", correct_number)
else:
    print("You guessed correct!")