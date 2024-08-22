rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

import random

computer_choice = random.choice([0,1,2])

my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if(my_choice == 0):
    print(rock)
    print("Computer Choice:")
    if computer_choice == 0:
        print(rock)
        print("Match draw")
    elif computer_choice == 1:
        print(paper)
        print("You lose")
    elif computer_choice == 2:
        print(scissors)
        print("You won")
elif my_choice == 1:
        print(paper)
        print("Computer Choice:")
        if computer_choice == 0:
            print(rock)
            print("You won")
        elif computer_choice == 1:
            print(paper)
            print("Match draw")
        elif computer_choice == 2:
            print(scissors)
            print("You lose")
elif my_choice == 2:
        print(scissors)
        print("Computer Choice:")
        if computer_choice == 0:
            print(rock)
            print("You lose")
        elif computer_choice == 1:
            print(paper)
            print("You won")
        elif computer_choice == 2:
            print(scissors)
            print("Match draw")

