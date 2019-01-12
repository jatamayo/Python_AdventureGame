# -*- coding: utf-8 -*-
import time
import random
import os

# ------------------------------------------------
# ----------  GLOBAL VARIABLES -------------------
# ------------------------------------------------

list_questions = 0
list_answers = 1
list_correct_answers = 2
list_incorrect_answers = 3
list_description_level = 4

# ------------------------------------------------
# ----------  INFORMATION FOR 3 LEVELS -----------
# ------------------------------------------------

list_dance_battle = [['Wow.. The opponent is dancing the -TAKE THE L- dance \nWhat are you going to do?\n', 'Wow.. The opponent is dancing the -FRESH- dance \nWhat are you going to do?\n', 'Wow.. The opponent is dancing the -BEST MATES- dance \nWhat are you going to do?\n'],  # NOQA
    ['1-Accept the challenge and doing the dance - THE WORM -?\n2-Run away from the battle?', '1-Accept the challenge and doing the dance - LLAMA BELL -?\n2-Run away from the battle?', '1-Accept the challenge and doing the dance - WIGGLE -?\n2-Run away from the battle?'],  # NOQA
    ['Wow.. that is a really dance battle. excellent we have impressed to your opponent. Now we are ready to go to the battle.'],  # NOQA
    ['oh, we havent impressed your opponent, before to go to the battle we need to win our battle dance. lets try again.'],  # NOQA
    ['Hello, welcome to the world of -FORTNITE-. are you ready to start the battle.', 'To start we are going to go to the first stage, before start the battle we need to wait for a seconds.', 'Wait a momment, what is that? a player wants to have a dance battle. Ok lets start.']  # NOQA
]

list_treasure_chest = [['ASSAULT RIFLE, MINIGUN, HEAVY SHOTGUN', 'TACTICAL SHOTGUN, PUMP SHOTGUN, HAND CANNON', 'GRAPPLER, COMPACT GUN'],  # NOQA
    ['1-Select a combo of weapons\n2-Dont choice a combo of weapons because we dont want to kill to our oponents', '1-Select a combo of weapons\n2-Dont choice a combo of weapons and turn off the console', '1-Select a combo of weapons\n2-Dont choice a combo of weapons and only collect wood'],  # NOQA
    ['Excellent, we have the necessary weapons to go to fight with all your opponents'],  # NOQA
    ['excellent decision, but to win this battle we need some weapons, lets try again'],  # NOQA
    ['Great. now we are on -battle royale-, the first thing we need to do is go to find some treasure.', 'Great we have found a treasure. lets to open it', 'oh wow, we have find some weapons, its time to choice which weapon we need to go to the battle.']  # NOQA
]

list_win_or_die = [['all the squad is coming to fight with heavy weapons.', 'all the squad is coming to fight with only legendary weapons.', 'All the squad is building and castle.'],  # NOQA
    ['1-Build and fight from up.\n2-Run away from the battle', '1-Throw grenades and build faster.\n2-Go inside the storm', '1-Build a castle and fight with honor\n2-Turn off the console'],  # NOQA
    ['Wow, that was a great battle, the best battle ever, Congratulations now you are the winner'],  # NOQA
    ['That is a pity, we were so close to win. lets try again.'],  # NOQA
    ['Awesome, now we have all the necessary to go to the battle', '.Wow what is that? some squad is coming to you. ', 'Looks like that is the last squad, this will be our most important battle', '1 vs 4 looks like a hard battle but we are ready to accept the challenge. what are you going to do?']  # NOQA
]

# ------------------------------------------------
# ----------  GENERAL FUNCTIONS ------------------
# ------------------------------------------------


def Clean_Screen():
    '''
        Function behavior: Clean the console screen
        Inputs: none
        Outputs: none
    '''
    os.system('cls')  # on windows - if you are using windows comment the -clear - functions and use this one # NOQA
    # os.system('clear')  # on linux / os x - if you are using linux comment the -cls - functions and use this one # NOQA


def Description_Level(list_answers_questions):
    '''
        Function behavior: Print the presentation text from each level
        Inputs: list with answers and questions -list_answers_questions-
        Outputs: none
    '''
    for index in range(len(list_answers_questions[list_description_level])):
        time.sleep(3)
        print(list_answers_questions[list_description_level][index])
    print ("\n")
    time.sleep(3)
    print(random.choice(list_answers_questions[list_questions]))
    time.sleep(2)
    print(random.choice(list_answers_questions[list_answers]))


def Input_Validation():
    '''
        Function behavior: Validate if the user input is between the options 1 or 2
        Inputs: none
        Outputs: user ipnut validated
    '''
    while True:
        user_option = input("\nWhat are you going to do? option 1 or option 2?")
        if user_option == "1" or user_option == "2":
            return user_option
        else:
            print ("oh oh, that is not an option, please try again ")
            condition = False


def Play_Again():
    '''
        Function behavior:  Functions to answer the user if wants to play again, if so, restart the game
        Inputs: none
        Outputs: user option
    '''
    yes_play_again = ["yes", "y", "YES"]
    no_play_again = ["no", "n", "NO"]
    while True:
        user_play_again_option = input("\n\nWould you like to play again yes, no? :")
        if user_play_again_option in yes_play_again:
            print ("Lets play again")
            Clean_Screen()
            Dance_Battle(list_dance_battle)
        elif user_play_again_option in no_play_again:
            print ("bye bye")
            exit()
        else:
            print ("oh oh, that is not an option, please try again ")

# ------------------------------------------------
# ----------  MAIN GAME FUNCTIONS ----------------
# ------------------------------------------------

battle_dance_tittle = '''
██████╗  █████╗ ████████╗████████╗██╗     ███████╗    ██████╗  █████╗ ███╗   ██╗ ██████╗███████╗
██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║     ██╔════╝    ██╔══██╗██╔══██╗████╗  ██║██╔════╝██╔════╝
██████╔╝███████║   ██║      ██║   ██║     █████╗      ██║  ██║███████║██╔██╗ ██║██║     █████╗
██╔══██╗██╔══██║   ██║      ██║   ██║     ██╔══╝      ██║  ██║██╔══██║██║╚██╗██║██║     ██╔══╝
██████╔╝██║  ██║   ██║      ██║   ███████╗███████╗    ██████╔╝██║  ██║██║ ╚████║╚██████╗███████╗
╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝'''


def Dance_Battle(list_answers_questions):
    '''
        Function behavior:  First stage of the game, -battle dance- print and show the game instructions and manage the logic of the first stage
        Inputs: list with answers and questions -list_answers_questions-
        Outputs: none
    '''
    Clean_Screen()
    print (battle_dance_tittle)
    time.sleep(3)
    Description_Level(list_answers_questions)
    user_answer = Input_Validation()
    print (user_answer)
    if user_answer == "1":
        print(random.choice(list_answers_questions[list_correct_answers]))
        time.sleep(8)
        Treasure_Chest(list_treasure_chest)
    else:
        print(random.choice(list_answers_questions[list_incorrect_answers]))
        time.sleep(8)
        Dance_Battle(list_dance_battle)

treasure_chest_tittle = '''
████████╗██████╗ ███████╗ █████╗ ███████╗██╗   ██╗██████╗ ███████╗     ██████╗██╗  ██╗███████╗███████╗████████╗
╚══██╔══╝██╔══██╗██╔════╝██╔══██╗██╔════╝██║   ██║██╔══██╗██╔════╝    ██╔════╝██║  ██║██╔════╝██╔════╝╚══██╔══╝
   ██║   ██████╔╝█████╗  ███████║███████╗██║   ██║██████╔╝█████╗      ██║     ███████║█████╗  ███████╗   ██║
   ██║   ██╔══██╗██╔══╝  ██╔══██║╚════██║██║   ██║██╔══██╗██╔══╝      ██║     ██╔══██║██╔══╝  ╚════██║   ██║
   ██║   ██║  ██║███████╗██║  ██║███████║╚██████╔╝██║  ██║███████╗    ╚██████╗██║  ██║███████╗███████║   ██║
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝     ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝   ╚═╝'''


def Treasure_Chest(list_answers_questions):
    '''
        Function behavior:  First stage of the game, -treasure chest- print and show the game instructions and manage the logic of the second stage
        Inputs: list with answers and questions -list_answers_questions-
        Outputs: none
    '''
    Clean_Screen()
    print (treasure_chest_tittle)
    time.sleep(3)
    Description_Level(list_answers_questions)
    user_answer = Input_Validation()
    print (user_answer)
    if user_answer == "1":
        print(random.choice(list_answers_questions[list_correct_answers]))
        time.sleep(8)
        Win_or_Die(list_win_or_die)
    else:
        print(random.choice(list_answers_questions[list_incorrect_answers]))
        time.sleep(8)
        Treasure_Chest(list_treasure_chest)

win_or_die_tittle = '''
██╗    ██╗██╗███╗   ██╗     ██████╗ ██████╗     ██████╗ ██╗███████╗
██║    ██║██║████╗  ██║    ██╔═══██╗██╔══██╗    ██╔══██╗██║██╔════╝
██║ █╗ ██║██║██╔██╗ ██║    ██║   ██║██████╔╝    ██║  ██║██║█████╗
██║███╗██║██║██║╚██╗██║    ██║   ██║██╔══██╗    ██║  ██║██║██╔══╝
╚███╔███╔╝██║██║ ╚████║    ╚██████╔╝██║  ██║    ██████╔╝██║███████╗
 ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝     ╚═════╝ ╚═╝  ╚═╝    ╚═════╝ ╚═╝╚══════╝'''


def Win_or_Die(list_answers_questions):
    '''
        Function behavior:  First stage of the game, -win or die- print and show the game instructions and manage the logic of the third stage
        Inputs: list with answers and questions -list_answers_questions-
        Outputs: none
    '''
    Clean_Screen()
    print (win_or_die_tittle)
    time.sleep(3)
    Description_Level(list_answers_questions)
    user_answer = Input_Validation()
    print (user_answer)
    if user_answer == "1":
        print(random.choice(list_answers_questions[list_correct_answers]))
        time.sleep(6)
        print (victory_royale_tittle)
        time.sleep(4)
        Play_Again()
    else:
        print(random.choice(list_answers_questions[list_incorrect_answers]))
        time.sleep(8)
        Win_or_Die(list_win_or_die)

victory_royale_tittle = '''
 ██╗ ██╗  ██╗    ██╗   ██╗██╗ ██████╗████████╗ ██████╗ ██████╗ ██╗   ██╗    ██████╗  ██████╗ ██╗   ██╗ █████╗ ██╗     ███████╗
████████╗███║    ██║   ██║██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝    ██╔══██╗██╔═══██╗╚██╗ ██╔╝██╔══██╗██║     ██╔════╝
╚██╔═██╔╝╚██║    ██║   ██║██║██║        ██║   ██║   ██║██████╔╝ ╚████╔╝     ██████╔╝██║   ██║ ╚████╔╝ ███████║██║     █████╗
████████╗ ██║    ╚██╗ ██╔╝██║██║        ██║   ██║   ██║██╔══██╗  ╚██╔╝      ██╔══██╗██║   ██║  ╚██╔╝  ██╔══██║██║     ██╔══╝
╚██╔═██╔╝ ██║     ╚████╔╝ ██║╚██████╗   ██║   ╚██████╔╝██║  ██║   ██║       ██║  ██║╚██████╔╝   ██║   ██║  ██║███████╗███████╗
 ╚═╝ ╚═╝  ╚═╝      ╚═══╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝'''

Dance_Battle(list_dance_battle)
