# MH 2nd elif and logical operators notes

homework = False
chores = True
room = False

if homework and chores and room:
    print("You may go to your friends how.")

elif not chores or not room:
    pass

else:
    print("Go do your homework.")

username = input("What's your username?\n")
password = input("What's your password?\n")

if username == "mhsiao" and password == "100410":
    print("Welcome back Mirai.")
else:
    print("Get out of here.")

# you can have infinite elifs
# You can put conditionals inside of conditionals