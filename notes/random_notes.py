# MH 2nd random numbers notes

import random

# prints two random numbers
print(random.random()) # float between 0 and 1
print(random.randint(1, 100)) # integer between value a and b

# always ad coments in your code to further clarify what is going on

name = input("What is your name? \n").strip().title()

# random stats creator
stat_one = random.randint(1,10) + random.randint(1,10)
stat_two = random.randint(1,10) + random.randint(1,10)
stat_three = random.randint(1,10) + random.randint(1,10)
stat_four = random.randint(1,10) + random.randint(1,10)
stat_five = random.randint(1,10) + random.randint(1,10)
stat_six = random.randint(1,10) + random.randint(1,10)

print(f"Your stat options are: {stat_one}, {stat_two}, {stat_three}, {stat_four}, {stat_five}, {stat_six}")

# set individual stats
strength = int(input("Which stat are you making strength? \n")) + 2
