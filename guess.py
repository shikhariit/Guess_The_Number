import random
import time

random_no = random.randint(1, 10)
guess = 0
c1 = 0
while True:
    guess != random_no:
        guess = int(input("Guess a Number(from 1 to 10): \n Press 404 to quit"))
    if guess == 404:
        exit()
    elif guess < random_no:
        print("Be Bold Increase Your Guess")
    elif guess > random_no:
        print("Don't Be Too Bold Decrease Your Guess")
    elif guess == random_no:
       print("JackPot computer too generated {}".format(guess)
       c1 = c1 + 1
    print("Your Total Correct Guesses = " , c1)
    time.sleep(1)
