import random
name=input( "give me your name to start the quiz of secret number:")
min = int(input("the min number you want to play with, is:"))
max = int(input("the max number you want to play with, is:"))

secret = random.randint(min,max)
guess = None
tries= 0
print(secret)
while guess != secret:

    input_text = input(f"Hallo {name},now try to guess the secret number (between {min} and {max}): ")
    guess = int(input_text)
    tries = tries + 1

    if guess < min or guess > max:
        print(f"Oh {name},This number is not in the valid range you already choosed. Try again!")
    elif guess == secret:
        print(f"Bravo {name},You guessed it - congratulations! It's number {secret} but it had took you {tries} tries.")
    else:
        print(f"Sorry {name}, your guess is not correct... The secret number is not {guess}")

# TODO: read file "hiscore.txt", get current highscore

# TODO: say "you are better than last time" if highscore improved

# TODO: save current number of attempts to file "hiscore.txt" if better than highscore
hiscore = open("hiscore.txt", "r")
content = int(hiscore.read())
hiscore.close()
if content == tries :
    print("you have the same highscore")
elif content > tries :
    hiscore = open("hiscore.txt", "w")
    hiscore.write(f"{tries}")
    hiscore.close()
    content = tries
    print(f" you have a new highscore, it had taken only {content} tries")
else :
    print(f"you did not reach the old highscore, it was only {content} tries but you took {tries} tries ")
print (content)


