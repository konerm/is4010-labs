import random

def generate_mad_lib(adjective, noun, verb):
    """Return a nonempty story containing all three supplied words."""
    return f"Once upon a time, a {adjective} {noun} {verb} through the park."

def guessing_game():
    """Run an interactive number-guessing game."""
    secret_number = random.radint (1, 100)

    while True:
        guess = int(input("Enter your guess: "))
        if guess < secret_number:
            print("Too low.")
        elif guess > secret_number:
            print("Too high")
        else:
            print("You guessed correctly!")
            break