# MH 2nd Who are you project
info = {}
num = 0

while num == 0:
    print("Hello! Welcome to Mirai's first coding project of the semster! Please answer a few questions:")
    name = input("What is your name: ")
    if name in info:
        print("Welcome back,", name)
        print(info[name])
    else:
        age = input("What is your age: ")
        fav_color = input("What is your favorite color: ")
        print("Welcome", name, ", my favorite color is also", fav_color, ", though I am definitely not", age, ".")
        info[name.title()] = [age, fav_color]
        print(info)

# for advanced: creat list to store data that hs been input before, a loop after name to check if name has been input before, if it has display that persons information