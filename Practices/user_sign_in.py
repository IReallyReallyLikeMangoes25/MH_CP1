# MH 2nd user sign in practice

username = input("What is your username?\n")
password = input("What is your password?\n")

user_check = input("Type in your username again to verify:\n")
pass_check = input("Type in your password again to verify:\n")

if user_check == username and pass_check == password:
    print(f"Thankyou for verifying {username}, we have confirmed your username and password.")

else:
    print("Incorrect username or password.")