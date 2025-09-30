# MH 2nd Shopping List Manager

shopping_list = []

while True:
    action = input("Would you like to exit, add, remove, or print out your shopping list.\n")
    action.lower
    action.strip
    if action == "add":
        new = input("What would you like to add?\n")
        shopping_list.append(new)
        print(shopping_list)

    elif action == "remove":
        remove = input("What would you like to remove?\n")
        if remove in shopping_list:
            shopping_list.remove(remove)
            print(shopping_list)
        else:
            print("That item is not in your shopping list.")

    elif action == "print":
        print(shopping_list)

    elif action == "exit":
        break
    else:
        print("That is not one of the options for actions you can do.")