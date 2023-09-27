MENU={
    "espresso":{
        "ingredients": {
            "water":50,
            "coffee":18,
        },
        "cost":200,
    },
    "latte":{
        "ingredients": {
            "water":200,
            "milk":150,
            "coffee":18,
            },
        "cost":300,
    },
    "tea":{
        "ingredients": {
            "water":50,
            "milk":50,
            "tea_powder":20,
            },
        "cost":150,
    },
    "cappuccino": {
            "ingredients": {
                "water":250,
                "coffee":24,
                "milk":100,
            },
        "cost":350,
    }
}
profit=0
resources={
    "water":500,
    "milk":500,
    "coffee":100,
    "tea_powder":100
}

def is_resource_sufficient(order_ingredients):
    """ return True when order can be made and false if resource is insufficient """
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:
            print(f"sorry there is not enough{item}.")
            return False
    return True

def process_cash():
    """Return the caash inserted """
    print("please insert cash")
    total =int(input("insert money in cash :"))
    return total

def is_transaction_successful(money_received,drink_cost):
    """return true when payment is accpeted and return false when money is insufficient. """
    if money_received >= drink_cost:
        change = (money_received - drink_cost)
        print(f"here is the change of yours {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry that not enough money,money refunded ")
        return False

def make_coffee(drink_name,order_ingredients):
    """deduct the required ingredints from the resources"""
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"here is your {drink_name} ☕️,enjoy ")


is_on =True
while is_on:
    choice=input("What whould you like to have?(espresso/latte/cappaccino/tea)")
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"water : {resources['water']}ml")
        print(f"milk : {resources['milk']}ml")
        print(f"coffee : {resources['coffee']}gm")
        print(f"tea_powder : {resources['tea_powder']}gm")
        print(f"money = rs{profit}")
    else:
        drink=MENU[choice]
        print(f"you ordered {choice} with {drink['cost']}")
        if is_resource_sufficient(drink["ingredients"]):
            payment=process_cash()
            print("payments is=" ,payment)
            if is_transaction_successful(payment,drink['cost']):
                make_coffee(choice,drink["ingredients"])