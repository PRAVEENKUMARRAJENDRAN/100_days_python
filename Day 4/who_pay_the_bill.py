import random

friends = ["Praveen", "kavya", "Siva", "Santhosh"]

random_bill_payer_position = random.randint(0,3)

print("{0} will pay the bill".format(friends[random_bill_payer_position])) 

print("{0} will pay the next bill".format(random.choice(friends)))