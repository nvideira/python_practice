import data

on = True
money = 0
max_water = 2000
max_milk = 1000
max_coffee = 300


def check_ingredients(drink):
    for part in data.MENU[drink]["ingredients"]:
        if data.MENU[drink]["ingredients"][part] > data.resources[part]:
            print(f"Sorry. Not enough {part}.")
            return False
    return True


def payment(drink):
    quarters = int(input("How many quarters will you insert? "))
    dimes = int(input("How many dimes will you insert? "))
    nickles = int(input("How many nickles will you insert? "))
    pennies = int(input("How many pennies will you insert? "))
    total_paid = round((quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01), 2)
    if total_paid < data.MENU[drink]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        print(f"Here is ${round((total_paid - data.MENU[drink]['cost']), 2)} dollars in change.")
        return True


while on:
    order = input("What would you like? ").lower()
    if order == "off":
        on = False
    elif order == "report":
        for resource in data.resources:
            if resource == "water" or resource == "milk":
                print(f"{resource.capitalize()}: {data.resources[resource]}ml")
            else:
                print(f"{resource.capitalize()}: {data.resources[resource]}g")
        print(f"Money: ${money}")
    elif order == "espresso" or order == "latte" or order == "cappuccino":
        if check_ingredients(order):
            if payment(order):
                for thing in data.MENU[order]["ingredients"]:
                    data.resources[thing] -= data.MENU[order]["ingredients"][thing]
                print(f"Here is your {order}. Enjoy!")
                money += data.MENU[order]["cost"]
    elif order == "refill":
        for src in data.resources:
            add = int(input(f"How much {src} will you add? "))
            if src == "water" and data.resources[src] + add > max_water:
                add = max_water - data.resources[src]
                print(f"{src.capitalize()} capacity is now at max.")
            elif src == "milk" and data.resources[src] + add > max_milk:
                add = max_milk - data.resources[src]
                print(f"{src.capitalize()} capacity is now at max.")
            elif src == "coffee" and data.resources[src] + add > max_coffee:
                add = max_coffee - data.resources[src]
                print(f"{src.capitalize()} capacity is now at max.")
            data.resources[src] += add
