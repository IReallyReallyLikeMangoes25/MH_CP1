# MH 2nd fix the game practice

import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False
    while not game_over:
        # The error here is a runtime error, guess is being saved as a string so it can't be compared to the number to guess, which is an integer.
        guess = int(input("Enter your guess: "))
        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
        # There's a second if statement creating a logic error, because even if the player eceeded their attempt amount it would print out if they were too high or low.
        elif guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif guess > number_to_guess:
            print("Too high! Try again.")
            attempts += 1
            # In both elifs there is a logic error, the code didn't add any attempts to the attempt count so people could have unlimited attempts even though they're not supposed to.
        elif guess < number_to_guess:
            print("Too low! Try again.")  
            attempts += 1
        # The continue here was creating a logic error, because it never actually ran, or did anything at all. The code works fine without it.
    print("Game Over. Thanks for playing!")
start_game()