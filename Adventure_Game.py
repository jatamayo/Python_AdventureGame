# -*- coding: utf-8 -*-
import time
import random
import os

#------------------------------------------------
#----------  GLOBAL VARIABLES -------------------
#------------------------------------------------

list_questions =0
list_answers = 1
list_correct_answers = 2
list_incorrect_answers = 3
list_description_level = 4
list_tittle = 5

#------------------------------------------------
#----------  INFORMATION FOR 3 LEVELS -----------
#------------------------------------------------



list_dance_battle = [
    ['Wow.. The opponent is dancing the -TAKE THE L- dance \nWhat are you going to do?\n','Wow.. The opponent is dancing the -FRESH- dance \nWhat are you going to do?\n','Wow.. The opponent is dancing the -BEST MATES- dance \nWhat are you going to do?\n'],
    ['1-Run away from the battle?\n2-Accept the challenge and doing the dance - THE WORM -?','1-Run away from the battle?\n2-Accept the challenge and doing the dance - LLAMA BELL -?','1-Run away from the battle?\n2-Accept the challenge and doing the dance - WIGGLE -?'],
    ['Wow.. that is a really dance battle. excellent we have impressed to your opponent. Now we are ready to go to the battle.'],
    ['oh, we havent impressed your opponent, before to go to the battle we need to win our battle dance. lets try again.'],
    ['Hello, welcome to the world of -FORTNITE-. are you ready to start the battle.','To start we are going to go to the first stage, before start the battle we need to wait for a seconds.','Wait a momment, what is that? a player wants to have a dance battle. Ok lets start.']
]

list_treasure_chest = [
    ['Second question option 1','Second question option 2','Second question option 3'],
    ['Second answer option 1','Second answer option 2','Second answer option 3'],
    ['Second correct answer option 1','Second correct answer option 2','Second correct answer option 3'],
    ['Second incorrect answer option 1','Second incorrect answer option 2','Second incorrect answer option 3'],
    ['Great. now we are on -battle royale-, the first thing we need to do is go to find some treasure.','Great we have found a treasure. lets to open it','oh wow, we have find some weapons, its time to choice what weapon we need to go to the battle.']
]

list_win_or_die = [
    ['Third question option 1','Third question option 2','Third question option 3'],
    ['Third answer option 1','Third answer option 2','Third answer option 3'],
    ['Third correct answer option 1','Third correct answer option 2','Third correct answer option 3'],
    ['Third incorrect answer option 1','Third incorrect answer option 2','Third incorrect answer option 3'],
    ['Third description level 1','Third description level 2','Third description level 3']
]

#------------------------------------------------
#----------  GENERAL FUNCTIONS ------------------
#------------------------------------------------

def Description_Level(list_answers_questions):
    '''
        Function behavior:  
        Inputs:
        Outputs:
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
        Function behavior:  
        Inputs:
        Outputs:
    '''
    condition = False
    while True:
        user_option = input("\nWhat are you going to do? option 1 or option 2?")
        if user_option == "1" or user_option == "2":
            return user_option  
            condition = True
        else:
            print ("oh oh, that is not an option, please try again ")
            condition = False

def Play_Again():
    '''
        Function behavior:  
        Inputs:
        Outputs:
    '''
    yes_play_again = ["yes", "y", "YES"]
    no_play_again = ["no", "n", "NO"]
    while True:
        user_play_again_option = input("play again? :")
        if user_play_again_option in yes_play_again:
            print ("Lets play again")
            Dance_Battle(list_dance_battle)
        elif user_play_again_option in no_play_again:
            print ("bye bye")
            exit()
        else:
            print ("oh oh, that is not an option, please try again ")
            condition = False

#------------------------------------------------
#----------  MAIN GAME FUNCTIONS ----------------
#------------------------------------------------

battle_dance_tittle = '''   
██████╗  █████╗ ████████╗████████╗██╗     ███████╗    ██████╗  █████╗ ███╗   ██╗ ██████╗███████╗
██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║     ██╔════╝    ██╔══██╗██╔══██╗████╗  ██║██╔════╝██╔════╝
██████╔╝███████║   ██║      ██║   ██║     █████╗      ██║  ██║███████║██╔██╗ ██║██║     █████╗  
██╔══██╗██╔══██║   ██║      ██║   ██║     ██╔══╝      ██║  ██║██╔══██║██║╚██╗██║██║     ██╔══╝  
██████╔╝██║  ██║   ██║      ██║   ███████╗███████╗    ██████╔╝██║  ██║██║ ╚████║╚██████╗███████╗
╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝'''

def Dance_Battle(list_answers_questions):
    '''
        Function behavior:  
        Inputs:
        Outputs:
    '''
    os.system('cls')  # on windows - if you are using windows comment the -clear - functions and use this one
    # os.system('clear')  # on linux / os x - if you are using linux comment the -cls - functions and use this one
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
        Function behavior:  
        Inputs:
        Outputs:
    '''
    os.system('cls')  # on windows - if you are using windows comment the -clear - functions and use this one
    # os.system('clear')  # on linux / os x - if you are using linux comment the -cls - functions and use this one
    time.sleep(3)
    Description_Level(list_answers_questions)
    user_answer = Input_Validation()
    print (user_answer)
    if user_answer == "1":
        print(random.choice(list_answers_questions[list_correct_answers]))
        Win_or_Die(list_win_or_die)
    else:
        print(random.choice(list_answers_questions[list_incorrect_answers]))
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
        Function behavior:  
        Inputs:
        Outputs:
    '''
    os.system('cls')  # on windows - if you are using windows comment the -clear - functions and use this one
    # os.system('clear')  # on linux / os x - if you are using linux comment the -cls - functions and use this one
    time.sleep(3)
    Description_Level(list_answers_questions)
    user_answer = Input_Validation()
    print (user_answer)
    if user_answer == "1":
        print(random.choice(list_answers_questions[list_correct_answers]))
        Play_Again()        
    else:
        print(random.choice(list_answers_questions[list_incorrect_answers]))
        Win_or_Die(list_win_or_die)

Dance_Battle(list_dance_battle)

