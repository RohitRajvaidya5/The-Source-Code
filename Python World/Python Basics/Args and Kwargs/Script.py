def order_pizza(size, *toppings, **details):

    print(f"Ordered a {size} pizza with following toppings :")
    for topping in toppings:
        print(f"- {topping}")

    print(type(toppings))

    print("Details :")
    for key, value in details.items():
        print(f"- {key}: {value}")


order_pizza("large","tomato","pepperoni","onion","capsicum", delivery = True, tip = 7)