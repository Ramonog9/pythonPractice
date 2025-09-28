import random

guess = int(input("Guess a number between 1 and 10?"))
correct_number = random.randint(1,10)

while guess != correct_number:
    guess = int(input("What is your guess?"))
    if guess > correct_number:
        print("Guess lower")
    else:
        print("Guess higher")
print("You guessed correct!")