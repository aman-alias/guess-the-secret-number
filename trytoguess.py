import random
name=input( "give me your name to start the quiz of secret number:")
min = int(input("the min number you want to play with, is:"))
max = int(input("the max number you want to play with, is:"))

secret = random.randint(min,max)


guess = None

while guess != secret:
    input_text = input(f"Hallo {name},now try to guess the secret number (between {min} and {max}): ")
    guess = int(input_text)

    if guess < min or guess > max:
        print(f"Oh {name},This number is not in the valid range you already choosed. Try again!")
    elif guess == secret:
        print(f"Bravo {name},You guessed it - congratulations! It's number {secret}.")
    else:
        print(f"Sorry {name}, your guess is not correct... The secret number is not {guess}")
