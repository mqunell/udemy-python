from random import randint
from sys import argv

# Run like `py random_game.py 1 100`

_, low, high = argv
answer = randint(int(low), int(high))
num_guesses = 0


def get_number_input(prompt):
    user_input = input(prompt)
    try:
        int_input = int(user_input)
        global num_guesses
        num_guesses += 1
        return int_input
    except ValueError:
        return get_number_input("You have to enter a number! Try again: ")


guess = get_number_input(f"Guess a number between {low} and {high}: ")

while guess != answer:
    direction = "lower" if guess > answer else "higher"
    guess = get_number_input(f"Try again! You need to guess {direction}: ")
else:
    plural = "guess" if num_guesses == 1 else "guesses"
    print(f"You got it in {num_guesses} {plural}!")
