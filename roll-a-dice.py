import random

response = "y"
while response == "y":
    no = random.randint(1, 6)
    if no == 1:
        print("---------")
        print("|       |")
        print("|   o   |")
        print("|       |")
        print("---------")
    elif no == 2:
        print("---------")
        print("|       |")
        print("| o   o |")
        print("|       |")
        print("---------")
    elif no == 3:
        print("---------")
        print("|   o   |")
        print("|   o   |")
        print("|   o   |")
        print("---------")
    elif no == 4:
        print("---------")
        print("| o   o |")
        print("|       |")
        print("| o   o |")
        print("---------")
    elif no == 5:
        print("---------")
        print("| o   o |")
        print("|   o   |")
        print("| o   o |")
        print("---------")
    elif no == 6:
        print("---------")
        print("| o   o |")
        print("| o   o |")
        print("| o   o |")
        print("---------")
    response = input("Roll again? (y/n): ")
print("Thanks for playing!")
