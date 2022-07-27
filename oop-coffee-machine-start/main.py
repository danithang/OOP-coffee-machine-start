from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# calling all classes from imports and putting them in a variable
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

# establishing a while loop for the machine
is_on = True
while is_on:
    # calling the get_items() method and putting it in a variable to use in the coffee_choice input
    options = menu.get_items()
    coffee_choice = input(f"Would you like an: {options}? Type 'off' to turn off the machine or 'report' to get "
                          f"resources. ")
    # if, elif, statements to turn off machine, get report of resources and money in machine
    if coffee_choice == "off":
        is_on = False
    elif coffee_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        # else statement to call method find_drink and creating a variable for it and passing coffee_choice in output
        drink = menu.find_drink(coffee_choice)
        # nested if statement to see if resources are sufficient to make the drink variable
        if coffee_maker.is_resource_sufficient(drink):
            # another nested if statement to input money into machine and pass through the drink variable and cost
            # for the output
            if money_machine.make_payment(drink.cost):
                # if payment is enough then make the drink
                coffee_maker.make_coffee(drink)





