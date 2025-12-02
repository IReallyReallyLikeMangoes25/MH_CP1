# MH 2nd final project

# INPUT play: ask user "Do you want to play or quit?"

# STATS/MOVES:
    # player{
        # health - 7
        # speed - 
        # attack - 
        # defense - 
    #}
    # grunt{
        # health - 5
        # speed - 
        # attack - 
        # defense - 
        # magic - 10
    #}
    # Don{
        # health - 10
        # speed - 
        # attack - 
        # defense - 
        # magic - 15
    #}

# ITEMS/INVENTORY:
    # inventory: {begins empty}
    # broken wand: True (not in inventory)
    # cursed lasagne: True (not eaten)
    # 30 dollars: True (not in inventory)
    # Generator: True (power on)
    # cauldron: True (full)
    # artifact: True (safe)

# FUNCTIONS:
    # The Dons office:
        # In this room the battle function will be run on the Don and the Player
        # if the player wins print that they won and ask if they want to play again
        # If the player loses print that they lost and ask if they want to play again
        # If they want to play again return True, if they want to quit return False

    # Front room:
        # In this room the player has their choice of two doors
        # door 1 - leads to the kitchen
        # door 2 - leads to the supplies room

    # Incantation room:
        # In this room there's a grunt, run the battle function
        # in this room if the cauldron is still full ask the player if they would like to use it
        # if they do randomize to choose what they get - 
        # +5 attack/speed/defense
        # return cauldron as False
        # the player has 3 door options in this room
        # door 1 - Go back to the generator room
        # door 2 - Go to the meeting room
        # door 3 - Go to the Dons office

    # Generator room:
        # in this room if the player hasn't already turned off the generator they will be given the choice to turn it off
        # if they choose to turn it off give all enemies -3 speed and player -3 attack and return generator as False
        # the player has two door options in this room
        # door 1 - Go back to the kitchen
        # door 2 - Go to the incantation room

    # Kitchen:
        # check if cursed lasagne has been eaten, if it has provide door options, if it hasn't ask player if they want to eat the lasagne
        # if the player eats the lasagne randomly choose between giving them a stat boost or debuff and return cured lasagne as False
        # the player will be given three door choices in this room
        # door 1 - Go back to the front room
        # door 2 - Go to the generator room
        # door 3 - Go to the meeting room

    # Game room:
    # The vault:
    # Meeting room:
        # there are two grunts in this room, run the battle function for both
        # the player has to defeat both to leave
        # the player has 4 door options in this room
        # door 1 - Go to the kitchen
        # door 2 - Go to the supplies room
        #
    # Supplies room:
        # check if the artifact has already been knocked over, if it hasn't ask the player if they w
        # in this room the player has the choice between 3 doors
        # door 1 - Go back to the front room
        # door 2 - Go to the vault
        # door 3 - Go to the meeting room

    # Battle:
    # Player turn:
    # Enemy turn:

# GAME:
    # while user wants to play the game:
        # begin user in the front room, run the Front room function



    