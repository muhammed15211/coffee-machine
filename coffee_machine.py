from main import MENU, resources

water = resources['water']
milk = resources['milk']
coffee = resources['coffee']
money = 0

# Coin Operation
penny = 0.01     #1cent
nickel = 0.05    #5cents
dime = 0.10      #10cents
quarter = 0.25   #25cents

#User Payment Calculation
def user_quarter_calculation(user_quarter):
    user_quarter_calc = user_quarter * 0.25
    return user_quarter_calc

def user_dime_calculation(user_dime):
    user_dime_calc = user_dime * 0.10
    return user_dime_calc

def user_nickel_calculation(user_nickel):
    user_nickel_calc = user_nickel * 0.05
    return user_nickel_calc

def user_penny_calculation(user_penny):
    user_penny_calc = user_penny * 0.01
    return user_penny_calc

# Total User Calc.
def total_calc():
    return user_quarter_calculation(user_quarter) + user_dime_calculation(user_dime) + user_nickel_calculation(user_nickel) + user_penny_calculation(user_penny)


# Espresso Ingredients / Costs
espresso_water = MENU['espresso']['ingredients']['water']
espresso_coffee = MENU['espresso']['ingredients']['coffee']
espresso_cost = MENU['espresso']['cost']

# Latte Ingredients / Costs
latte_water = MENU['latte']['ingredients']['water']
latte_coffee = MENU['latte']['ingredients']['coffee']
latte_milk = MENU['latte']['ingredients']['milk']
latte_cost = MENU['latte']['cost']

# Cappuccino Ingredients / Costs
cappuccino_water = MENU['cappuccino']['ingredients']['water']
cappuccino_coffee = MENU['cappuccino']['ingredients']['coffee']
cappuccino_milk = MENU['cappuccino']['ingredients']['milk']
cappuccino_cost = MENU['cappuccino']['cost']

play = True
while play:
    # Taking customer order
    user_order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # When user ask for Espresso
    if user_order == 'espresso':
        # Taking User Funds
        print("Please insert coins.")
        user_quarter = float(input("How many quarters?: "))
        user_dime = float(input("How many dimes?: "))
        user_nickel = float(input("How many nickles?: "))
        user_penny = float(input("How many pennies?: "))

        user_payment = total_calc()

        if espresso_water <= water and espresso_coffee <= coffee and user_payment >= espresso_cost:
            if user_payment > espresso_cost:
                user_change = round(user_payment - espresso_cost, 2)
                print(f"User Change: ${user_change}")
            water -= espresso_water
            coffee -= espresso_coffee
            money += espresso_cost
            print(f"Here is your {user_order} drink!")

        else:
            if user_payment < espresso_cost:
                print("Sorry that's not enough money. Money refunded.")
            elif espresso_water > water:
                print("Sorry there's not enough water.")
            elif espresso_coffee > coffee:
                print("Sorry there's not enough coffee")

    # When User ask for Latte
    elif user_order == 'latte':
        # Taking User Funds
        print("Please insert coins.")
        user_quarter = float(input("How many quarters?: "))
        user_dime = float(input("How many dimes?: "))
        user_nickel = float(input("How many nickles?: "))
        user_penny = float(input("How many pennies?: "))

        user_payment = total_calc()

        if latte_water <= water and latte_milk <= milk and latte_coffee <= coffee and user_payment >= latte_cost:
            if user_payment > latte_cost:
                user_change = round(user_payment - latte_cost, 2)
                print(f"User Change: ${user_change}")
            water -= latte_water
            milk -= latte_milk
            coffee -= latte_coffee
            money += latte_cost
            print(f"Here is your {user_order} drink!")

        else:
            if user_payment < latte_cost:
                print("Sorry that's not enough money. Money refunded.")
            elif latte_water > water:
                print("Sorry there's not enough water.")
            elif latte_coffee > coffee:
                print("Sorry there's not enough coffee.")
            elif latte_milk > milk:
                print("Sorry there's not enough milk.")

    # When User ask for Cappuccino
    elif user_order == 'cappuccino':
        # Taking User Funds
        print("Please insert coins.")
        user_quarter = float(input("How many quarters?: "))
        user_dime = float(input("How many dimes?: "))
        user_nickel = float(input("How many nickles?: "))
        user_penny = float(input("How many pennies?: "))

        user_payment = total_calc()

        if cappuccino_water <= water and cappuccino_milk <= milk and cappuccino_coffee <= coffee and user_payment >= cappuccino_cost:
            if user_payment > cappuccino_cost:
                user_change = round(user_payment - cappuccino_cost, 2)
                print(f"User Change: ${user_change}")
            water -= cappuccino_water
            milk -= cappuccino_milk
            coffee -= cappuccino_coffee
            money += cappuccino_cost
            print(f"Here is your {user_order} drink!")

        else:
            if user_payment < cappuccino_cost:
                print("Sorry that's not enough money. Money refunded.")
            elif cappuccino_water > water:
                print("Sorry there's not enough water.")
            elif cappuccino_coffee > coffee:
                print("Sorry there's not enough coffee.")
            elif cappuccino_milk > milk:
                print("Sorry there's not enough milk.")

    # If User ask for report
    elif user_order == 'report':
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}g")
        print(f"Money: ${money}")

    elif user_order == 'off':
        play = False