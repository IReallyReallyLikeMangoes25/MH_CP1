# MH 2nd order up practice
full_order = []
cost = 0

# menu dictionary
menu = {
# inside of the menue dictionary there will three more dictionaries, one for sides, one for drinks, and one for main courses
"sides" : {
    "Mozarella sticks" : 4.99,
    "Garlic knots" : 3.99,
    "Cheesy sticks" : 3.99,
    "Salad" : 2.99
},

"entrees" : {
    "Pepperoni pizza" : 8.99,
    "Cheese pizza" : 7.99,
    "Supreme pizza" : 9.99,
    "Meat lovers pizza" : 9.99
},

"drinks" : {
    "Coke a cola" : 2.99,
    "Water" : 0,
    "Sprite" : 2.99,
    "Lemonade" : 3.99
}
}


# function for ordering 
# takes in a dictionary
def order(options, title):
    cart = []
    price = 0
# prints out the options
    for option in options:
        print(option)
# asks user what they want and how many items they want
    how_many = int(input(f"How many {title} will you be ordering?\n"))
    while True:
        for item in range(how_many):
            item = str(input("What item would you like to order?\n"))
            if item in options:
                cart.append(item)
                price += options[item]
            else:
                # if they give an invalid input ask again
                print("That item is not one of the options, please input another choice.\n")
        break

    return cart, price
# returns each choice and how much this part of the order will cost

# run function for sides
sides, cost_1 = order(menu["sides"], "sides")
for item in sides:
    full_order.append(item)
cost += cost_1
# run function for drinks
drinks, cost_2 = order(menu["drinks"], "drinks")
for item in drinks:
    full_order.append(item)
cost += cost_2
# run function for entrees
entrees, cost_3 = order(menu["entrees"], "entrees")
for item in entrees:
    full_order.append(item)
cost += cost_3
# add every return of food and price to a new list
# print out new list and total cost
print("Your order is:")
for i in full_order:
    print(i)

print(f"Total cost: {cost}")