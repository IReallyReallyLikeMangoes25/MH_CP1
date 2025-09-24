# MH 2nd what is my grade practice

grade = float(input("What is your number grade?\n"))

if grade >= 95:
    print("Congrats! You have an A+!")
elif grade <= 94 and grade >= 90:
    print("Good job! You have an A-!")
elif grade >= 87 and grade <= 89:
    print("Keep up the hard work! You have a B+!")
elif grade >= 85 and grade <= 86:
    print("Nice job! You have a B!")
elif grade >= 80 and grade <= 84:
    print("Still in high range! You have a B-!")
elif grade >= 77 and grade <= 79:
    print("You have a C+!")
elif grade >= 75 and grade <= 76:
    print("You have a C!")
elif grade >= 70 and grade <= 74:
    print("Be careful, you have a C-!")
elif grade >= 67 and grade <= 69:
    print("Uh oh, You have a D+!")
elif grade >= 65 and grade <= 66:
    print("Uh oh, you have a D!")
elif grade >= 60 and grade <= 64:
    print("You're almost failing! You have a D-!")
else:
    print("You're failing! You have an F!")