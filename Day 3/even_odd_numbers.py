num = int(input("Enter the number to check whether eve or odd"))

print(num)

if num % 2 == 0:
    print("The given number {0} is even".format(num))
elif num % 3 == 1:
    print("The given number {0} is odd".format(num))
