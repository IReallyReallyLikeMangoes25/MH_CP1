# MH 2nd squared numbers practice

numbers = [3, 7, 12, 25, 30, 45, 50, 65, 70, 85, 90, 105, 110, 125, 130, 145, 150, 165, 170, 185, 190, 205, 210, 225, 230, 245, 250, 265, 270, 280]

squared = list(map(lambda num: num*num, numbers))

for number, square in zip(numbers, squared):
    print(f"{number} squared is {square}")