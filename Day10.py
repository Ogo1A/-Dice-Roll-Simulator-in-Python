import random

min_val=1
max_val=6

roll_again="yes"
while roll_again == "yes" or roll_again =="y":
    print("Rolling The Dice...")
    print("The Values are:")

    print(random.randint(min_val,max_val))

    roll_again=input("Role the dice again")
    