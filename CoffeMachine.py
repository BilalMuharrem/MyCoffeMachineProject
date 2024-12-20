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
    "water": 500,
    "milk": 300,
    "coffee": 200,
    "money": 0
}

remaining=[]

for ürün in resources:
    remaining.append(resources[ürün])

def report():
    for ürün in resources:
        print(f"{ürün}: {resources[ürün]}")
    print(f"left amount is {remaining}")

def check():
    global should_end
    if girdi=="report":
        #report()
        print(remaining)
    elif girdi=="off":
        should_end=False

def comparison():
    water_needed = MENU[girdi]["ingredients"].get("water", 0)
    milk_needed = MENU[girdi]["ingredients"].get("milk", 0)
    coffee_needed = MENU[girdi]["ingredients"].get("coffee", 0)

    if remaining[0] < water_needed:
        print("Sorry, not enough water!")
        return False
    elif remaining[1] < milk_needed:
        print("Sorry, not enough milk!")
        return False
    elif remaining[2] < coffee_needed:
        print("Sorry, not enough coffee!")
        return False
    else:
        remaining[0] -= water_needed
        remaining[1] -= milk_needed
        remaining[2] -= coffee_needed
        return True

def prices():
    money =  resources.get("money")
    peny=int(input("Penny: "))*0.01
    nickel=int(input("Nickel: "))*0.05
    dime=int(input("Dime: "))*0.1
    quarter=int(input("Quarter: "))*0.25
    money += peny+nickel+dime+quarter

    money_needed = MENU[girdi].get("cost")
    if money >= money_needed:
        money -= money_needed
        print(f"Para üstünüz ${money}")
        remaining[3] += money_needed
        return True
    else:
        print("You did not insert enough money")
        return False

should_end = True
while should_end:
    girdi=input("What would you like? (espresso/latte/cappuccino): ").lower()
    if girdi=="report" or  girdi=="off":
        check()
    elif girdi in MENU:
        if not comparison():
            break
        print("Please insert coins!")
        if not prices():
            break
    else:
        print("Invalid option. Please choose espresso, latte, cappuccino, report or off.")