def calculate_love_score(first, second):
    complete_name = first + second

    first_value = 0
    second_value = 0

    first_letter = ["t", "r", "u", "e"]

    second_letter = ["l", "o", "v", "e"]

    for i in first_letter:
        first_value += complete_name.lower().count(i)
        
    for i in second_letter:
        second_value += complete_name.lower().count(i)

    print(f"Love Score={str(first_value) + str(second_value)}")


calculate_love_score("Praveen Kumar", "kavyasri")