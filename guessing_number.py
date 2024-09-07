import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 10  # Number of attempts allowed

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")
    print(f"You have {attempts} attempts to guess the correct number.\n")

    # Loop until the user runs out of attempts
    while attempts > 0:
        guess = int(input("Enter your guess: "))

        # Check the user's guess
        if guess == secret_number:
            print("Congratulations! You guessed the correct number!")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

        # Reduce the number of attempts
        attempts -= 1
        print(f"Remaining attempts: {attempts}\n")

    # If the user runs out of attempts
    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")

# Run the game
number_guessing_game()