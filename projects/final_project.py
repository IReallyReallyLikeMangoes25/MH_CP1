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
    print("description")
    choice = input("You see two doors at the back, seems they're the only ways forward. Which way should you go?\nDoor one\nDoor two")
    while True:
        if choice == "Door one":
            print("You walk up to the door and open it, hoping that red stain on the bottom is just marinara.")
        elif choice == "Door two":
            print("You approach the door and open it.")
        else:
            print("You can't see a door like that anywhere, choose from the ones you can see.")
            choice = input("You see two doors at the back, seems they're the only ways forward. Which way should you go?\nDoor one\nDoor two")

def kitchen():
    print("Looks like this is just the kitchen")

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

def player_turn(player_attack, player_specialatk, enemy_defense, enemy_specialdef, player_inventory):
    action = input("What would you like to do?\n1. Attack\n2. Heal\n3. Special attack\n4. Use inventory item")
    auto_win = False
    while True:
        if action == 1:
            damage = (player_attack / 5) - (enemy_defense /5)
            return damage
        elif action == 2:
            healed = random.randint(0, 4)
            return healed
        elif action == 3:
            damage = (player_specialatk / 5) - (enemy_specialdef / 5)
        elif action == 4:
            print(player_inventory)
            use = input("what item would you like to use?")
            while True:
                if use == "broken wand":
                    rand = random.randint(1,2)
                    if rand == 1:
                        healed = 5
                        return healed
                    else:
                        healed = -4
                        return healed
                elif use == "30 dollars":
                    if enemy_defense == 13:
                        auto_win = True
                        return auto_win
                    else:
                        healed = -5
                        return healed
                else:
                    print("That is not in your inventoy, please choose again.")
                    use = input("what item would you like to use?")
        else:
            print("That is not an option right now, make anoter choice.")
            action = input("What would you like to do?\n1. Attack\n2. Heal\n3. Special attack\n4. Use inventory item")

def enemy_turn(player_attack, player_specialdef, player_defense, enemy_attack, enemy_defense, enemy_specialatk, magic):
    action = random.randint(1, 4)
    if action == 1:
        damage = (enemy_attack / 5) - (player_defense /5)
        return damage
    elif action == 2:
        healed = random.randint(1,4)
        return healed
    elif action == 3:
        damage = (magic / 5) - (player_specialdef /5)
        return damage
    else:
        damage = (enemy_specialatk / 5) - (player_specialdef /5)
        return damage
