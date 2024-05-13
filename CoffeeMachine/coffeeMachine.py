MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
    "money": 0
}


def report():
    """Output Resources"""
    print(f'Water: {resources["water"]} \nmilk: {resources["milk"]} \ncoffe: {resources["coffee"]}\nMoney: ${resources["money"]}')


def coins(actual_price):
    """takes Actual_price return remaining money and add money in resources"""
    print("please insert coins.")
    quarters = int(input("How many Quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many dime? "))
    pennies = int(input("How many pennies? "))
    dollars_inserted = round(quarters * 0.25 + nickles * 0.05 + dimes * 0.01 + pennies * 0.01, 2)
    # print(f"dollars_inserted: ${dollars_inserted}")
    # print(f"actual_price: ${actual_price}")
    if dollars_inserted > actual_price:
        print(f"Here is {round(dollars_inserted - actual_price, 2)} Change.")
        return actual_price
    if dollars_inserted == actual_price:
        return actual_price
    else:
        print(f"Sorry that's not {dollars_inserted} enough money. Money refunded.")
        return 0


def is_resource_suffecient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry There is not enough {item}")
            return False
        else:
            return True


is_on = True
while is_on:
    customer_coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if customer_coffee == "report":
        report()
    elif customer_coffee == "off":
        print(f"Shutting down Machine")
        is_on = False
    else:
        choice = MENU[customer_coffee]
        if is_resource_suffecient(choice["ingredients"]):
            money_inserted = coins(choice["cost"])
            if money_inserted != 0:
                print(f"Here is your {customer_coffee} ☕")
                resources["water"] -= choice["ingredients"]["water"]
                resources["milk"] -= choice["ingredients"]["milk"]
                resources["coffee"] -= choice["ingredients"]["coffee"]
                resources["money"] += money_inserted




