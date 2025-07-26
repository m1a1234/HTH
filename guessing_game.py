# Guessing Game - Mia Carozza

import random

def generate_random_number():
    return random.randint(1, 100)

def get_user_guess():

    for user_input in range (10):
        guess = int(input("enter your guess"))
        if guess >= 1 and guess <=100:
            return guess
        else:
            print ("Enter a number between 1 and 100")

def play_guessing_game():
    secret_number = generate_random_number() 
    print(secret_number)
    guess = get_user_guess()

    number = False
    while number == False:

        if guess > secret_number:
            number = False
            print("Try again thats to high")
            guess = get_user_guess()

        elif guess < secret_number:
            number = False
            print ("Try again thats to low")
            guess = get_user_guess()

        elif guess == secret_number:
            number = True
            print ("You got it")

play_guessing_game()