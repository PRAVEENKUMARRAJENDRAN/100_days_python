from data import data
from art import *
from random import randint

print(len(data))


def celebrity_comparsion(comparsion_a, comparision_b):
    if comparsion_a["follower_count"] > comparision_b["follower_count"]:
        return "A"
    else:
        return "B"









def higher_lower():

    print(logo)
    game_continues = True
    final_score = 0 
    current_index = 0

    while game_continues:
        random_selection = randint(1, len(data)-1)
        print("Compare A: {0},{1}, from {2}".format(data[current_index]["name"], data[current_index]["description"], data[current_index]["country"]))
        print(vs)
        print("Compare B: {0},{1}, from {2}".format(data[random_selection]["name"], data[random_selection]["description"], data[random_selection]["country"]))
        selection = input("Who has more followers? Type 'A' or 'B'")

        celebrity_results = celebrity_comparsion(data[current_index], data[random_selection])

        if celebrity_results == selection:
            print("You Won")
            final_score += 1
            #game_continues = True
            if selection == 'B':
                current_index = random_selection
        else:
            final_score -= 1
            print("Sorry, that's wrong. Final Score: {0}".format(final_score))
            game_continues = False

















higher_lower()