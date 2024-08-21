print("Welcome to Python Pizza delivers!")
size = input("What soze pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input(" Do you want extra cheese? Y or N: ")


if size == 'S':
    if pepperoni == 'Y':
        bill = 15 + 2
    else:
        bill = 15
elif size == 'M':
    if pepperoni == 'Y':
        bill = 20 + 3
    else:
        bill = 20
elif Size :
    if pepperoni == 'Y':
        bill = 25 + 3
    else:
        bill = 25

if extra_cheese == 'Y':
    bill = bill + 1

print("Your final bill is: ${0}".format(bill))
