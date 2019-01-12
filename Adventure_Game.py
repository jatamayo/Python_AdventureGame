import time
import random
import os
from os import system, name

#------------------------------------------------
#----------  GLOBAL VARIABLES -------------------
#------------------------------------------------

list_questions =0
list_answers = 1
list_correct_answers = 2
list_incorrect_answers = 3
list_description_level = 4

#------------------------------------------------
#----------  INFORMATION FOR 3 LEVELS -----------
#------------------------------------------------

list_dance_battle = [
    ['First question option 1','First question option 2','First question option 3'],
    ['First answer option 1','First answer option 2','First answer option 3'],
    ['First correct answer option 1','First correct answer option 2','First correct answer option 3'],
    ['First incorrect answer option 1','First incorrect answer option 2','First incorrect answer option 3'],
    ['First description level 1','First description level  2','First description level  3']
]

list_treasure_chest = [
    ['Second question option 1','Second question option 2','Second question option 3'],
    ['Second answer option 1','Second answer option 2','Second answer option 3'],
    ['Second correct answer option 1','Second correct answer option 2','Second correct answer option 3'],
    ['Second incorrect answer option 1','Second incorrect answer option 2','Second incorrect answer option 3'],
    ['Second description level 1','Second description level 2','Second description level 3']
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

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')


def Description_Level(list_answers_questions):
    '''
        Function behavior:  
        Inputs:
        Outputs:
    '''
    print ("Description level")
    for index in range(len(list_answers_questions[list_description_level])):
        time.sleep(3)
        print(list_answers_questions[list_description_level][index])
    print ("\n\n")
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
        user_option = input("Now it's time to make a decision, 1 or 2:")
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

def Dance_Battle(list_answers_questions):
    '''
        Function behavior:  
        Inputs:
        Outputs:
    '''
    time.sleep(3)
    Description_Level(list_answers_questions)
    user_answer = Input_Validation()
    print (user_answer)
    if user_answer == "1":
        print(random.choice(list_answers_questions[list_correct_answers]))
        Treasure_Chest(list_treasure_chest)
        clear()
    else:
        print(random.choice(list_answers_questions[list_incorrect_answers]))
        Dance_Battle(list_dance_battle)
        clear()

def Treasure_Chest(list_answers_questions):
    '''
        Function behavior:  
        Inputs:
        Outputs:
    '''
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

def Win_or_Die(list_answers_questions):
    '''
        Function behavior:  
        Inputs:
        Outputs:
    '''
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

