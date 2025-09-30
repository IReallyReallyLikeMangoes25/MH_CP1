# MH 2nd list notes

import random

names = ["Mirai", "Owyn", "Anna", "Aron", "Eric", 5, 3.14, False]

print(names)
print(names[0])
print(names[random.randint(1, len(names))])
print(random.choice(names))
names[-1] = "Vivienne"
names.extend(["Irene", "Annica"])
names += ["Gemma"]
names.remove(5)
names.remove(3.14)
best_name = names.index("Mirai")
print(best_name)
print(names)
names.pop(best_name)
print(names)
names.insert(0, "Mirai")

# list = changable, ordered
# tuple = not changable, ordered
classes = ("Monk", "Druid")
# set = changable, unordered
fruit = {"apple", "kiwi", "banana"}