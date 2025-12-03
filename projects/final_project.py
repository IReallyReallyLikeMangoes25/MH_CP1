# MH 2nd final project

# INPUT play: ask user "Do you want to play or quit?"

# STATS:{
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
    #}}

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
        # return their door choice

    # Incantation room:
        # In this room there's a grunt, run the battle function
        # in this room if the cauldron is still full ask the player if they would like to use it
        # if they do randomize to choose what they get - 
        # +5 attack/speed/defense
        # return cauldron as False (empty) and display door options
        # the player has 3 door options in this room
        # door 1 - Go back to the generator room
        # door 2 - Go to the meeting room
        # door 3 - Go to the Dons office
        # return their door choice

    # Generator room:
        # in this room if the player hasn't already turned off the generator they will be given the choice to turn it off
        # if they choose to turn it off give all enemies -3 speed and player -3 attack and return generator as False (turned off) and display door options
        # the player has two door options in this room
        # door 1 - Go back to the kitchen
        # door 2 - Go to the incantation room
        # return their door choice

    # Kitchen:
        # check if cursed lasagne has been eaten, if it has provide door options, if it hasn't ask player if they want to eat the lasagne
        # if the player eats the lasagne randomly choose between giving them a stat boost or debuff and return cured lasagne as False (eaten) and display door options
        # the player will be given three door choices in this room
        # door 1 - Go back to the front room
        # door 2 - Go to the generator room
        # door 3 - Go to the meeting room
        # return their door choice

    # Game room:
        # Check if the broken wand is already in the players inventory, if it is provide door options, if it's not ask the player if they would like to pick up the broken wand
        # If they want to pick it up return broken wand as False (in inventory) and display door options
        # The player will have 3 door options in this room:
        # door 1 - Go to the meeting room
        # door 2 - Go to the Dons office
        # door 3 - Go to the vault
        # return their door choice

    # The vault:
        # Check if the $30 is already in the players inventory, if it is provide door options, if it's not ask them if they would like to pick it up
        # if they pick it up return 30 dollars as False (in inventory) and display door options
        # in this room there are 2 door options
        # door 1 - Go to the supplies room
        # door 2 - Go to the game room
        # return their door choice

    # Meeting room:
        # there are two grunts in this room, run the battle function for both
        # the player has to defeat both to get the door options
        # the player has 4 door options in this room
        # door 1 - Go to the kitchen
        # door 2 - Go to the supplies room
        # door 3 - Go to the game room
        # door 4 - Go to the incantation room
        # return their door choice

    # Supplies room:
        # check if the artifact has already been knocked over, if it hasn't ask the player if they want to knock it over
        # If they say they do, -2 from all enemy attack stats, return artifact as False (knocked over) and display door options
        # in this room the player has the choice between 3 doors
        # door 1 - Go back to the front room
        # door 2 - Go to the vault
        # door 3 - Go to the meeting room
        # return their door choice

    # Battle:
        # if the player is faster
            # While the player and enemy are alive:
                # player turn (players + enemies stats/inventory)
                # enemy turn (players + enemies stats)

        # if the enemy is faster:
            # While the player and enemy are alive:
                # enemy turn (players + enemies stats)
                # player turn (players + enemies stats/inventory)

    # Player turn: Takes in players stats, enemies stats, and player inventory
        # ask user what they want to do from the options:
            # INPUT: "What would you like to do?"

    # Enemy turn: Takes in players stats and enemies stats

# GAME:
    # while user wants to play the game:
        # begin user in the front room, run the Front room function



    