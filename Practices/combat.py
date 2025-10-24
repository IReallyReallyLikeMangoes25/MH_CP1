# MH 2nd Combat practice

name = ("Hello young trainer! What is your name?\n")
starter = str(input(f"Hello {name}, nice to meet you. I am Professor Oak, please choose a starter pokemon:\n1. Bulbasaur\n2. Squirtle\n3. Charmander\n"))
rival = ""
hp = 0
atk = 0
defense = 0
spec_atk = 0
spec_def = 0
speed = 0

rhp = 0
ratk = 0
rdefense = 0
rspec_atk = 0
rspec_def = 0
rspeed = 0

if starter == 1:
    starter = "Bulbasaur"
    hp = 45
    atk = 49
    defense = 49
    spec_atk = 65
    spec_def = 65
    speed = 45

    rival = "Charmander"
    rhp = 39
    ratk = 52
    rdefense = 43
    rspec_atk = 60
    rspec_def = 50
    rspeed = 65

elif starter == 2:
    starter = "Squirtle"
    hp = 44
    atk = 48
    defense = 65
    spec_atk = 50
    spec_def = 64
    speed = 43

    rival = "Bulbasaur"
    rhp = 45
    ratk = 49
    rdefense = 49
    rspec_atk = 65
    rspec_def = 65
    rspeed = 45

else:
    starter = "Charmander"
    hp = 39
    atk = 52
    defense = 43
    spec_atk = 60
    spec_def = 50
    speed = 65

    rival = "Squirtle"
    rhp = 44
    ratk = 48
    rdefense = 65
    rspec_atk = 50
    rspec_def = 64
    rspeed = 43

def your_turn(hp, atk, defense, spec_atk, spec_def, speed):
    pass

def rival_turn(rhp, ratk, rdefense, rspec_atk, rspec_def, rspeed):
    pass


print(f"Great! {starter} is the perfect choice for you. Now, in order to begin your journey as a trainer, you must fight your rival in a battle. Your rival has chosen {rival}")

print(f"Go {starter}!")
print(f"Go {rival}!")


if speed > rspeed:
    print(f"{starter} goes first!")
    your_turn(hp, atk, defense, spec_atk, spec_def, speed)
else:
    print(f"{rival} goes first!")
    rival_turn(rhp, ratk, rdefense, rspec_atk, rspec_def, rspeed)

while hp > 0 or rhp > 0:
    pass

print()