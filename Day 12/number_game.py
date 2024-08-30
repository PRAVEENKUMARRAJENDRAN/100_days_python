import random

EASY_ATTEMPT = 10
HARD_ATTEMPT = 5


def check_number(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer is {actual_answer}")

def set_difficult(level):
    if level == 'easy':
        return EASY_ATTEMPT
    elif level == 'hard':
        return HARD_ATTEMPT


def guess_number():
    print("Welcome to the Number Game!")
    number_choosen = random.randrange(1,100)
    print(number_choosen)

    level = input("Choose a difficulty. Type 'easy' or 'hard': ")

    turns = set_difficult(level)

    guess = 0 

    while guess != number_choosen:
        if turns == 0:
            break
        print(f"THe number of guess left is {turns}")
        guess = int(input("Make a guess:"))
        turns = check_number(guess, number_choosen, turns)
        

        




guess_number()
