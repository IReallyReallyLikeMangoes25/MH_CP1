# MH 2nd Format outputs notes


name = "Eric"
age = 9999999999999999999999999999999999999999999999999
grade = .75
money = 25

print("Hello {}, nice to meet you! You are {:,}, years old. You have a {:%} in this class. You have ${:.2f}, that is a lot of money.".format(name, age, grade, money))

print(f"Hello {name}, nice to meet you! You are {age:,}, years old. You have a {grade:%} in this class. You have ${money:.2f}, that is a lot of money.")