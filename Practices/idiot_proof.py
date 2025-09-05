# MH 2nd idiot proof practice

name = input("What if your full name? ").title().strip()
number = input("What is your phone number? Please put dashes between every section. ").replace("-", " ")
if len(number) < 12:
    print("Invalid number, please try again.")

    number = input("What is your phone number? Please put dashes between every section. ").replace("-", " ")

gpa = float(input("What is your GPA? "))
rounded_gpa = round(gpa, 1)

print(name, number, rounded_gpa)
