# MH 2nd average grade practice

# sorry for using and if/else instead of a for loop, but I already started before I realized I could do that 

classes = int(input("How many classes do you have?\n"))

if classes == 1:
    period_1 = float(input("What is your first period grade? \n"))
    grades = period_1


elif classes == 2:
    period_1 = float(input("What is your first period grade? \n"))
    period_2 = float(input("What is your second period grade? \n"))
    grades = period_1 + period_2

elif classes == 3:
    period_1 = float(input("What is your first period grade? \n"))
    period_2 = float(input("What is your second period grade? \n"))
    period_3 = float(input("What is your third period grade? \n"))
    grades = period_1 + period_2 + period_3
    
elif classes == 4:
    period_1 = float(input("What is your first period grade? \n"))
    period_2 = float(input("What is your second period grade? \n"))
    period_3 = float(input("What is your third period grade? \n"))
    period_4 = float(input("What is your fourth period grade? \n"))
    grades = period_1 + period_2 + period_3 + period_4

    
elif classes == 5:
    period_1 = float(input("What is your first period grade? \n"))
    period_2 = float(input("What is your second period grade? \n"))
    period_3 = float(input("What is your third period grade? \n"))
    period_4 = float(input("What is your fourth period grade? \n"))
    period_5 = float(input("What is your fifth period grade? \n"))
    grades = period_1 + period_2 + period_3 + period_4 + period_5

    
elif classes == 6:
    period_1 = float(input("What is your first period grade? \n"))
    period_2 = float(input("What is your second period grade? \n"))
    period_3 = float(input("What is your third period grade? \n"))
    period_4 = float(input("What is your fourth period grade? \n"))
    period_5 = float(input("What is your fifth period grade? \n"))
    period_6 = float(input("What is your sixth period grade? \n"))
    grades = period_1 + period_2 + period_3 + period_4 + period_5 + period_6
    
elif classes == 7:
    period_1 = float(input("What is your first period grade? \n"))
    period_2 = float(input("What is your second period grade? \n"))
    period_3 = float(input("What is your third period grade? \n"))
    period_4 = float(input("What is your fourth period grade? \n"))
    period_5 = float(input("What is your fifth period grade? \n"))
    period_6 = float(input("What is your sixth period grade? \n"))
    period_7 = float(input("What is your seventh period grade? \n"))
    grades = period_1 + period_2 + period_3 + period_4 + period_5 + period_6 + period_7


else:
    print("We do cannot calculate that many classes.")


print("Your current average grade is:", round(grades, 2))