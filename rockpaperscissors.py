#The computer is going to randomly choose a string from the array
import random
#creates the array for the program to choose from at random for the computer and picked by user
choices = ["Rock", "Paper", "Scissors"]
#This gives the user the ability to choose an option from the array previous from the class library
user_choice = input("What's your choice? Rock, Paper, or Scissors")

#Control flow statement while continously runs for when an error is input when the condition is not met for the array 
while user_choice not in choices:
    user_choice = input("Please properly input a choice of Rock, Paper, or Scissors")

#Computer randomly selects an option
comp_choice = random.choice(choices)
#In order for the comp_choice variable to reflect what the computer will actually choose 
print (f"Computer chose: {comp_choice}")

if user_choice == comp_choice:
    print("Tie")
#The conditions that need to be met in order to win, to draw, or to lose
elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("You lose!")
    else:
        print("You win!")

elif user_choice == "Scissors":
    if comp_choice == "Rock":
        print("You lose!")
    else:
        print("You win!")

elif user_choice == "Paper":
    if comp_choice == "Scissors":
        print("You lose!")
    else:
        print("You win!")
    
        

