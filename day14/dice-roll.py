import random

def roll_dice():
    return random.randint(1, 6)

# Simulate a dice roll and print the outcome
outcome = roll_dice()
print("Outcome of the dice roll:", outcome)
