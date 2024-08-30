import random

#A function that checks whether my sum is greator than 21
def check_cardsum(a):
    if a > 21:
        return True

def final_result(my_cards, computer_cards, result=None):
    if result or sum(my_cards) > sum(computer_cards):
        print(f"Your final hand: {my_cards}, final score: {sum(my_cards)}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_cards[0]}")
        print("You went over. You lose.")
        return
    else:
        print(f"Your final hand: {my_cards}, final score: {sum(my_cards)}")
        print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
        print("You win.")
        return

def select_inital_cards():
    c = []
    for i in range(2):
        c.append(random.randrange(1,10))
    return c

def current_cards(my_cards, computer_cards):
    print(f"Your cards: {my_cards}, current score: {sum(my_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")

def intial_gane():
    game_continues = True
    my_cards = select_inital_cards()
    computer_cards = select_inital_cards()

    current_cards(my_cards, computer_cards)

    while game_continues:     
        contine_game = input("Type 'y' to get another card, type 'n' to pass: ")

        if contine_game == 'y':
            my_cards.append(random.randrange(1,10))
            computer_cards.append(random.randrange(1,10))
            current_cards(my_cards, computer_cards)
            if check_cardsum(sum(my_cards)):
                final_result(my_cards, computer_cards, True)
        else:
            game_continues = False
            final_result(my_cards, computer_cards)



if __name__ == '__main__':
    start = input("Do you want to start playing the blackstone project ? click Y to start")

    if start == 'Y':
        intial_gane()
    else:
        print("Please select Y to start the Game")
