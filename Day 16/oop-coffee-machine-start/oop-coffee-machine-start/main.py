from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



if __name__ == '__main__':
    coffe_contine = True
    menu = Menu()
    coffemaker = CoffeeMaker()
    moneymachine = MoneyMachine()

    while coffe_contine:
        

        coffee = input(f"What would you like? {menu.get_items()}:")
        
        check_coffee = menu.find_drink(coffee)
        if check_coffee:
            if moneymachine.make_payment(check_coffee.cost):
                if coffemaker.is_resource_sufficient(check_coffee):
                    coffemaker.make_coffee(check_coffee)
                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                print("Insufficent Amount")
                    

        