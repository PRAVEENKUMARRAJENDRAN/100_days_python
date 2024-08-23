import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

nr_letters_selected, nr_symbols_selected, nr_numbers_selected = [], [], []

if nr_letters > 0:
    nr_letters_selected = random.choices(letters, k=nr_letters)
if nr_symbols > 0:
    nr_symbols_selected = random.choices(symbols, k=nr_symbols)
if nr_numbers > 0:
    nr_numbers_selected = random.choices(numbers, k=nr_numbers)


nr_letters_selected.extend(nr_symbols_selected)
nr_letters_selected.extend(nr_numbers_selected)
 
 
print(nr_letters_selected)
password = ''
for i in random.choices(nr_letters_selected, k=(nr_letters+nr_symbols+nr_numbers)):
    password += i

print(password)