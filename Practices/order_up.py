# MH 2nd order up practice

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
    "Pepperoni" : 8.99,
    "Cheese" : 7.99,
    "Supreme" : 9.99,
    "Meat lovers" : 9.99
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
    how_many = input(f"How many {title} will you be ordering?")
    while True:
        for i in how_many:
            item = input("What item would you like to order?").lower().strip().title()
            if item in options:
                cart.append[item]
                price += options[item]
            else:
                # if they give an invalid input ask again
                print("That item is not one of the options, please input another choice.")
                how_many += 1
                continue
        break

    return cart, price
# returns each choice and how much this part of the order will cost

# run function for sides
order(menu["sides"], "sides")
# run function for drinks
# run function for entrees
# add every return of food and price to a new list
# print out new list and total cost