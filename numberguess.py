import random 

print("Welcome to the number guessing game!")
r=random.randint(1, 50)
while True:
    num=int(input("Guess a number between 1 and 50: "))
    if num==r:
        print("Congratulations! You guessed the number.")
        break
    elif num<r:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")


