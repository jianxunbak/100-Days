from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = CoffeeMaker()
money = MoneyMachine()
menu = Menu()


is_on = True

while is_on:
    options = menu.get_items()
    decision = input(f"what drinks do you want? {options}: ")
    if decision == "off":
        is_on = False
    elif decision == "report":
        coffee.report(), money.report()
    else:
        drink_selection = menu.find_drink(decision)
        if coffee.is_resource_sufficient(drink_selection) and money.make_payment(drink_selection.cost):
            coffee.make_coffee(drink_selection)
        else:
            is_on = False


