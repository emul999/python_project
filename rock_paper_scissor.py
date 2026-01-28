'''
workflow of project

1- input from user (rock , paper , scissor)
2- computer choice (using random method)
3- result print

case 1 
rock = rock (tie)
rock = paper (paper win)
rock = scissor (rock win)

case 2 
paper = rock (paper win)
paper = paper (tie)
paper = scissor (scissor win)

case 3 
scissor = scissor (tie)
scissor = paper(scissor win)
scissor = rock(rock win58)
'''


import random
item_list = ["rock","paper","scissor"]

while True:

 user_choice = input("Enter your move = rock , papaer , scissor = ")
 comp_choice = random.choice(item_list)

 print(f"user choice = {user_choice},computer choice = {comp_choice}")

 if user_choice == comp_choice:
    print("both chooses : = match tie")
 elif user_choice == "rock":
    if comp_choice == "paper":
        print("paper covers rock = computer win ")
    else:
        print("rock smashes scissor = you win")

 elif user_choice == "paper":
    if comp_choice == "scissor":
        print("scissor cuts paper , comuter win")
    else:
        print("paper covers rock , you win")

 elif user_choice == "scissor":
    if comp_choice == " paper":
        print("scissor cuts paper , you win")
    else:
        print("rock smashes scissor , computer win")