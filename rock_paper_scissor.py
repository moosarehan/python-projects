import random
print("Welcome to Rock, Paper, Scissors!")
userwins=0
compwins=0
options=["rock","paper","scissors"]
while True:
    userinput=input("Type Rock/Paper/Scissors or Q to quit: ").strip().lower()
    if userinput=="q":
        break
    if userinput not in options:
        print("INVALID INPUT.PLEASE ENTER AGAIN!")
        continue
    randomnum=random.randint(0,2)
    compchoice=options[randomnum]
    print("Computer chose: ",compchoice)
    if userinput=="rock" and compchoice=="scissors":
        print("you win!")
        userwins+=1
    elif userinput=="scissors" and compchoice=="paper":
        print("you win !")
        userwins+=1
    elif userinput=="paper" and compchoice=="rock":
        print("you win!")
        userwins+=1
    elif userinput==compchoice:
        print("It's a tie!")    
        continue
    else:
        print("you lose!")
        compwins+=1
        continue


print("THANKS FOR PLAYING THE GAME SEE YOU NEXT TIME!   BYE!")
print(f"the user won {userwins}")
print(f"the computer won {compwins}")