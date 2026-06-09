import random
secretnumber = random.randint(1, 10)
guess = 0
while guess!= secretnumber:
    guess = int(input("Guess the number between 1 and 10: "))
    if guess < secretnumber:
        print("Too low! Try again.")
    elif guess > secretnumber:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number.")