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

game_images = [rock, paper, scissors]
my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if my_choice < 3:
    print(game_images[my_choice])

computer_choice = random.choice([0,1,2])
print("Computer Choice:")
print(game_images[computer_choice])


if my_choice >= 3 or my_choice < 0:
    print("You have selected invalid number. You lose!")
elif my_choice == 0 and computer_choice == 2:
    print("You win!")
elif my_choice == 2 and computer_choice == 0:
    print("You lose!")
elif computer_choice > my_choice:
    print("You lose!")
elif my_choice  > computer_choice:
    print("You win!")
elif my_choice == computer_choice:
    print("It's a draw!")
