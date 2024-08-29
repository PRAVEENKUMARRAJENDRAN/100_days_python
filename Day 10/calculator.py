
def addition(a, b):
    v = a+b
    print(f"{a} + {b} = {v}")
    return v

def subtraction(a, b):
    v = a-b
    print(f"{a} - {b} = {v}")
    return v

def multiplication(a, b):
    v = a*b
    print(f"{a} * {b} = {v}")
    return v

def division(a, b):
    v = a/b
    print(f"{a} / {b} = {v}")
    return v

def calculation():
    cal_func_end = False

    first_number = int(input("What's the first number?"))
    while not cal_func_end:
        op = input("""
        + \n
        - \n
        * \n
        / \n
        Pick an operation.
        """)

        next_number = int(input("What's the next number?"))

        if op == '+':
            first_number = addition(first_number, next_number)
        elif op == '-':
            first_number = subtraction(first_number, next_number)
        elif op == '*':
            first_number = multiplication(first_number, next_number)
        elif op == '/':
            first_number = division(first_number, next_number)

        c = input(f"Type y for contine with {first_number} else n")

        if c == 'n':
            cal_func_end = True

        






if __name__ == "__main__":
    print("The Calculator Problem")
    calculation()
    
    