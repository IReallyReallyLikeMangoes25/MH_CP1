# MH 2nd final project

import random
play_or_quit = input("Do you want to play or quit?").lower().strip().capitalize()

current_room = 0

stats = {
    "player" : {
        "health" : 10,
        "attack" : 13,
        "special_attack" : 15,
        "defense" : 7,
        "special defense" : 6,
        "speed" : 10
    },
    "grunt" : {
        "health" : 10,
        "attack" : 7,
        "defense" : 13,
        "special defense" : 10,
        "speed" : 10,
        "magic" : 10
    },
    "Don" : {
        "health" : 13,
        "attack" : 7,
        "defense" : 7,
        "special defense" : 9,
        "speed" : 10,
        "magic" : 17
    }
}

inventory = {

}

player = True
Don = True
broken_wand = True
cursed_lasagne = True
thirty_dollars = True
generator = True
cauldron = True
artifact = True

def dons_office():
    pass

def front_room():
    pass

def kitchen():
    pass

def supplies_room():
    pass

def incantation_room():
    pass

def generator_room():
    pass

def game_room():
    pass

def vault():
    pass

def meting_room():
    pass

def battle():
    pass

def player_turn(player_stats, enemy_stats, player_inventory):
    action = input("What would you like to do?\n1. Attack\n2. Heal\n3. Special attack\n4. Use inventory item")
    while True:
        if action == 1:
            pass
        elif action == 2:
            pass
        elif action == 3:
            pass
        elif action == 4:
            pass
        else:
            pass
def enemy_turn(player_stats, enemy_stats):
    action = random.randint(1, 4)
    if action == 1:
        pass
    elif action == 2:
        pass
    elif action == 3:
        pass
    else:
        pass
