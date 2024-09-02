MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = {
    "value": 0,
}


def report_output():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money['value']}")


def check_resource(coffee):
    if coffee == 'espresso': 
        if resources['coffee'] < MENU[coffee]["ingredients"]["coffee"] and resources['water'] < MENU[coffee]["ingredients"]["water"]:
            return False
    else:
        if resources['coffee'] < MENU[coffee]["ingredients"]["coffee"] and resources['water'] < MENU[coffee]["ingredients"]["water"] and resources['milk'] < MENU[coffee]["ingredients"]["milk"]:
            return False
    return True

def process_coins(quarter, dime, nickle, penny):
    quarter *= 0.25
    dime *= 0.10
    nickle *= 0.05
    penny *= 0.01
    total = quarter + dime + nickle + penny
    return total


def deduct_resources(coffee_choice):
    resources['water'] -= MENU[coffee_choice]['ingredients']['water']
    resources['coffee'] -= MENU[coffee_choice]['ingredients']['coffee']
    if coffee_choice != 'espresso':
        resources['milk'] -= MENU[coffee_choice]['ingredients']['milk']



def coffee_make():


    on = True

    while on:
        coffee = input("What would you like? (espresso/latte/cappuccino):")

        if coffee == 'report':
            report_output()
        elif coffee == 'off':
            on = False
            print("Coffee machine is under maintenance. Please try again after an hour.")
        else:
            resource_check = check_resource(coffee)

            if resource_check:
                 print("Please insert coins.")
                 quarters = int(input("How many quarters?: "))
                 dimes = int(input("How many dimes?: "))
                 nickles = int(input("How many nickles?: "))
                 pennies = int(input("How many pennies?: "))

                 if process_coins(quarters, dimes, nickles, pennies) == MENU[coffee]["cost"]:
                    deduct_resources(choice)
                    print(f"Here is your {choice} ☕. Have a good one!")
                 elif process_coins(quarters, dimes, nickles, pennies) > MENU[coffee]["cost"]:
                    deduct_resources(choice)
                    change = process_coins(quarters, dimes, nickles, pennies) - MENU[choice]['cost']
                    print(f"Here is ${change} in change.")
                    print(f"Here is your {choice} ☕. Have a good one!")
                 elif process_coins(quarters, dimes, nickles, pennies) < MENU[coffee]["cost"]:
                    print(f"Not enough money, ${(process_coins(quarters, dimes, nickles, pennies))} refunded.")

            else:
                print("No enough resource to make coffee")


coffee_make()