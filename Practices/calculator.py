# MH 2nd basic calculator practice

while True:
    num_1 = float(input("What is your first number? "))
    num_2 = float(input("What is your second number? "))
    add = (num_1 + num_2)
    sub = (num_1 - num_2)
    div = (num_1 / num_2)
    mult = (num_1 * num_2)
    operator = int(input("Would you like to 1. add, 2. subtract, 3. multiply, or 4. divide?"))


    if operator == 1:
        print(f"{num_1} + {num_2} = {add}")
    elif operator == 2:
        print(f"{num_1} - {num_2} = {sub}")
    elif operator == 3:
        print(f"{num_1} * {num_2} = {mult}")
    elif operator == 4:
        print(f"{num_1} / {num_2} = {div}")
    

    


