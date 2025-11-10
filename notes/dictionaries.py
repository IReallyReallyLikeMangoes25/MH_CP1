# MH 2nd dictionaries notes\
avatar = {
    "earth" : {
        "Toph" : "My name is Toph, cuz it sounds like TOUGH and that's just what I am."
    },
    
    "water" : {
        "Katara" : "It's not like I am a preachy cybaby who can't help but make speaches about hope all the time."
    }
}

print(avatar["earth"]["Toph"])

person = {
    # Key: value,
    "Name" : "Mirai",
    "Age" : 14,
    "Job" : "Instructor",
    "siblings" : "Owyn, Irene, Vivienne"
}

print(person["Name"])
print(person.keys())
for key in person.keys():
    print(f"{key} : {person[key]}")

print(person.values())
person["Age"] += 1
person["Birthday"] = "October 4"
print(person.items())