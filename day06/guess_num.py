# Writing a Python program that guesses a number between 1 and 10.
import random

def guess_number():
    target_number = random.randint(1, 10)
    while True:
        guess = int(input("Guess a number between 1 and 10: "))
        if guess < target_number:
            print("Too low, try again!")
        elif guess > target_number:
            print("Too high, try again!")
        else:
            print("Congratulations! You guessed the correct number.")
            break

guess_number()



