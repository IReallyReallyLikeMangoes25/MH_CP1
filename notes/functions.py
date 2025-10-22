# MH 2nd period Functions notes
# imports
# set global variables
# functions
# code

player_hp = 100
monster_hp = 100

def addNum(x, y):
    return x + y

def initials(name):
    names = name.split(" ")
    initial = ""
    for name in names:
        initial += name[0]
    return initial

print(addNum(5, 5))

num = addNum(addNum(-1347, 1234), addNum(5, 50))
print(num)

while num < addNum(9.2342, 42):
    print("duck")
    num += 1


print(f"My initials are: {initials("Mirai Hsiao")}")


def attack(dmg, turn):
    if turn == "player":
        return monster_hp - dmg, player_hp
    
    else:
        return monster_hp, player_hp - dmg
    
monster_hp, player_hp = attack(15, "monster")
print(f"Player health is now: {player_hp}")
print(f"Monster health is now: {monster_hp}")

monster_hp, player_hp = attack(15, "player")
print(f"Player health is now: {player_hp}")
print(f"Monster health is now: {monster_hp}")

print(f"a = {ord("a")}")
print(f"100 = {chr(100)}")

letter = "a"

num = ord(letter)

num += 1

print(chr(num))