# -*- coding: utf-8 -*-
"""
A statement that we want non-ASCII character errors to be disregarded by terminal
(all of the non-ASCII errors we were getting were errors in comment lines, not code)

This statement needs to be at the start of the code.
"""

#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

"""
Not-to-be-used preliminary defintions
"""

locations = {}

def change_location():
    pass

player_actual = {
    "Class": "Arch_Mage",
    "Name" : "<INSERT>",
    "Gender" : "<INSERT>",
    "Birthday" : "LOL",
    "Element" : "Fire",
    "Health" : 14,
    "Strength" : 8,
    "Stamina" : 10,
    "Defense" : 9,
    "Resistance" : 11,
    "Magic" : 20,
    "Speed" : 11,
    "Luck" : 4,
    "Intelligence" : 9,
    "Level" : 1,
    "Exp" : 0,
    "Coins" : 30,
    "Location" : "Metal"
}

global player_combat
player_combat = player_actual

#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

"""
To-be-used preliminary defintions
"""

global beat_fire
beat_fire = True

global beat_water
beat_water = False

global beat_wind
beat_wind = False

global beat_earth
beat_earth = False

global beat_metal
beat_metal = False


global has_started
has_started = False

global shopped_before
shopped_before = False

items = {
    "wand": [10, "Magic"],
    "lucky potion": [13, "Luck"],
    "winged shoes": [10, "Speed"],
    "book": [8, "Intelligence"],
    "health potion": [8, "Health"],
    "fairy dust": [4, "Magic"]
    }

    # change so that magic increases will be greater if one is in a shop of one's magic type

item_inventory = {}

#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

"""
There's a problem to fix or a section to improve immediately under wherever "#*" is found
use command f #* to find errors
"""

#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

"""
Imports
"""
from time import sleep
from random import randint
import random
from os import system
from sys import exit

#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

"""
Aesthetic Additions
"""
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

"""
Winning and losing
"""
def lose():
    print ""
    print ""
    sleep(1)
    print color.BOLD + "You died." + color.END
    sleep(1)
    print "Conquering really isn't your thing, is it?"
    print "Ah well. Better luck next time, I suppose."
    sleep(1)
    print "Would you like to play again? "
    play_again = (raw_input("> ")).lower()
    if "y" in play_again:
        global has_started
        has_started = False
        system('clear')
        start()
    else:
        exit(0)

def win():
    print ""
    print ""
    sleep(1)
    print color.BOLD + "Congratulations!" + color.END
    print "You have conquered all four elemental leaders."
    print "You are now the leader of (whatever our world name is)."
    print ""
    sleep(1)
    print "Would you like to play again? "
    play_again = (raw_input("> ")).lower()
    if "y" in play_again:
        global has_started
        has_started = False
        system('clear')
        start()
    else:
        exit(0)

#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

"""
Base mob stats
"""

# Mob Set-Up
global initial_mob
initial_mob = {
    "Name" : "<INSERT>",
    "Element" : "<INSERT>",
    "Health" : 25,
    "Strength" : 10,
    "Stamina" : 10,
    "Defense" : 8,
    "Resistance" : 7,
    "Magic" : 10,
    "Speed" : 11,
    "Luck" : 4,
    "Level" : 1,
    "Intelligence" : 7,
    "Exp" : 20
}

base_mob = initial_mob

#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

"""
Boss stats defined
"""
Fire_Boss = {
    "Class" : "Fire_Boss",
    "Name" : "<INSERT>",
    "Element" : "Fire",
    "Health" : 24,
    "Strength" : 18,
    "Stamina" : 20,
    "Defense" : 19,
    "Resistance" : 21,
    "Magic" : 30,
    "Speed" : 21,
    "Luck" : 14,
    "Intelligence" : 19,
    "Level" : 15,
    "Exp" : 500,
    "Location" : "fire_boss_location"
}

Earth_Boss = {
    "Class" : "Earth_Boss",
    "Name" : "<INSERT>",
    "Element" : "Earth",
    "Health" : 30,
    "Strength" : 26,
    "Stamina" : 24,
    "Defense" : 19,
    "Resistance" : 21,
    "Magic" : 18,
    "Speed" : 17,
    "Luck" : 15,
    "Intelligence" : 17,
    "Level" : 15,
    "Exp" : 500,
    "Location" : "earth_boss_location"
}

Water_Boss = {
    "Class" : "Water_Boss",
    "Name" : "<INSERT>",
    "Element": "Water",
    "Health" : 27,
    "Strength" : 21,
    "Stamina" : 25,
    "Stamina" : 24,
    "Defense" : 19,
    "Magic" : 26,
    "Speed" : 19,
    "Luck" : 24,
    "Intelligence" : 30,
    "Level" : 15,
    "Exp" : 500,
    "Location" : "water_boss_location"
}

Metal_Boss = {
    "Class" : "Metal_Boss",
    "Name" : "<INSERT>",
    "Element" : "Metal",
    "Health" : 25,
    "Strength" : 18,
    "Stamina" : 16,
    "Stamina" : 24,
    "Defense" : 19,
    "Magic" : 24,
    "Speed" : 22,
    "Luck" : 25,
    "Intelligence" : 26,
    "Level" : 15,
    "Exp" : 500,
    "Location" : "metal_boss_location"
}

Wind_Boss = {
    "Class" : "Wind_Boss",
    "Name" : "<INSERT>",
    "Element" : "Wind",
    "Health" : 25,
    "Strength" : 19,
    "Stamina" : 20,
    "Stamina" : 24,
    "Defense" : 19,
    "Magic" : 21,
    "Speed" : 21,
    "Luck" : 22,
    "Intelligence" : 19,
    "Level" : 15,
    "Exp" : 500,
    "Location" : "wind_boss_location"
}

#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

"""
Intro Text
"""
def game_intro_text():
    print ""
    print color.BOLD + 'Welcome adventurer.' + color.END
    sleep(1)
    print ""
    print "You have decided to embark upon this journey of courage,"
    sleep(1)
    print "determination"
    sleep(1)
    print "and power."
    sleep(1)
    print ""
    print "You have entered into a world of magic."
    sleep(1)
    print "This beautiful land has many incredible qualities about it"
    sleep(1)
    print "however it is a world in a state of repression!"
    sleep(1)
    print ""
    print "For centuries now,"
    sleep(1)
    print "this world has been ruled by four dictators:"
    sleep(1)
    print "Fire,"
    sleep(1)
    print "Earth,"
    sleep(1)
    print "Wind,"
    sleep(1)
    print "and Water."
    sleep(1)
    print ""
    print "The masters of these four elements hold immense power and authority,"
    sleep(1)
    print "each one ruling a sector of the world."
    sleep(1)
    print ""
    print "Yet the world is falling apart under their rule,"
    sleep(1)
    print "the people are growing restless and they need a leader…"
    sleep(1)
    print "a leader who can help them and not hinder them."
    sleep(1)
    print ""
    print "Embarking on this journey,"
    sleep(1)
    print "you are entrusted with one task and one task only…"
    sleep(1)
    print ""
    print color.BOLD + "Overthrow the dictators." + color.END
    print ""
    sleep(2)
    print "And let’s not forget: this is a place of magic."
    sleep(1)
    print "You can make use of these people’s elemental magic"
    sleep(1)
    print "to help you in your quest to reestablish order in this desperate land."
    sleep(1)
    print ""
    print "But take heed:"
    sleep(1)
    print "not all residents of this region will support you in your rise to power"
    sleep(1)
    print "(there are those who are not educated enough to recognize the danger"
    sleep(1)
    print "lurking behind the unstable peace)."
    sleep(1)
    print ""
    print "If you are strong enough,"
    sleep(1)
    print "brave enough,"
    sleep(1)
    print "and smart enough,"
    sleep(1)
    print "you will succeed."
    sleep(1)
    print ""
    print "If not, you will undoubtedly die."
    sleep(1)
    print ""
    print color.BOLD + "Good luck." + color.END
    sleep(2)
    print ""

    print "Type something (anything) once you've finished reading to continue."

    input = raw_input("> ").lower()

#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
"""
The 5 Categories
1) Arch_Mage, super aggressive, great offense stat growths, poor durability
2) Warden, Super defensive and sturdy, very slow and a bit thick in the head
3) Priest, aimed at protecting yourself more and skilled offense
4) Arcane_Smith, more well rounded
5) Arch_Caster, super agile and playful, good for high-risk high reward
"""
#stats
Arch_Mage = {
    "Class": "Arch_Mage",
    "Name" : "<INSERT>",
    "Gender" : "<INSERT>",
    "Birthday" : "LOL",
    "Element" : "Fire",
    "Health" : 14,
    "Strength" : 8,
    "Stamina" : 10,
    "Defense" : 9,
    "Resistance" : 11,
    "Magic" : 20,
    "Speed" : 11,
    "Luck" : 4,
    "Intelligence" : 9,
    "Level" : 1,
    "Exp" : 0,
    "Coins" : 30,
    "Location" : "Metal"
}

Warden = {
    "Class" : "Warden",
    "Name" : "<INSERT>",
    "Gender" : "<INSERT>",
    "Birthday" : "LOL",
    "Element" : "Earth",
    "Health" : 20,
    "Strength" : 16,
    "Stamina" : 14,
    "Defense" : 9,
    "Resistance" : 11,
    "Magic" : 8,
    "Speed" : 7,
    "Luck" : 5,
    "Intelligence" : 7,
    "Level" : 1,
    "Exp" : 0,
    "Coins" : 30,
    "Location" : "Metal"
}

Priest = {
    "Class" : "Priest",
    "Name" : "<INSERT>",
    "Gender" : "<INSERT>",
    "Birthday" : "LOL",
    "Element" : "Water",
    "Health" : 17,
    "Strength" : 11,
    "Stamina" : 15,
    "Resistance" : 14,
    "Defense" : 9,
    "Magic" : 16,
    "Speed" : 9,
    "Luck" : 6,
    "Intelligence" : 11,
    "Level" : 1,
    "Exp" : 0,
    "Coins" : 30,
    "Location" : "Metal"
}

Arcane_Smith = {
    "Class" : "Arcane_Smith",
    "Name" : "<INSERT>",
    "Gender" : "<INSERT>",
    "Birthday" : "LOL",
    "Element" : "Metal",
    "Health" : 15,
    "Strength" : 8,
    "Stamina" : 6,
    "Resistance" : 14,
    "Defense" : 9,
    "Magic" : 14,
    "Speed" : 12,
    "Luck" : 5,
    "Intelligence" : 10,
    "Level" : 1,
    "Exp" : 0,
    "Coins" : 30,
    "Location" : "Metal"
}

Arch_Caster = {
    "Class" : "Arch_Caster",
    "Name" : "<INSERT>",
    "Gender" : "<INSERT>",
    "Birthday" : "LOL",
    "Element" : "Wind",
    "Health" : 15,
    "Strength" : 9,
    "Stamina" : 10,
    "Resistance" : 14,
    "Defense" : 9,
    "Magic" : 11,
    "Speed" : 11,
    "Luck" : 5,
    "Intelligence" : 9,
    "Level" : 1,
    "Exp" : 0,
    "Coins" : 30,
    "Location" : "Metal"
}

#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

"""
Display Menu
"""
#Display the different Classes, still need to have updated Components
#AKA name, birthday, gender
def display_character_options():
    print ""

    print "____________" * 10
    print "These are the Base Stats. Character Creation Results May Vary"
    print "____________" * 10

    sleep(1)
    print ""
    print color.BOLD + 'Arch Mage' + color.END
    print Arch_Mage
    sleep(1)
    print ""
    print color.BOLD + 'Warden' + color.END
    print Warden
    sleep(1)
    print ""
    print color.BOLD + 'Priest' + color.END
    print Priest
    sleep(1)
    print ""
    print color.BOLD + 'Arcane Smith' + color.END
    print Arcane_Smith
    sleep(1)
    print ""
    print color.BOLD + 'Arch Caster' + color.END
    print Arch_Caster
    sleep(1)
    print ""

#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

"""
Character Design instructions text
"""
def character_creation_text():
    sleep(5)
    print "____________" * 10
    sleep(1)
    print ""
    sleep(1)
    print "____________" * 10
    print ""
    print "Avaliable Classes: Arch_Mage , Warden , Priest , Arcane_Smith , Arch_Caster"
    print ""
    print "____________" * 10
    sleep(1)
    print ""
    sleep(1)
    print "____________" * 10

#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

"""
Beginning Character Design
"""
#Character Creation
# player_actual = player_class_chosen is in this section
def create_a_character():
    while True:
        print ""
        print "What Class do you want to play as?"
        class_decision = raw_input("> ").lower()
        if "arch_mage" in class_decision or "mage" in class_decision:
            global player_class_chosen
            player_class_chosen = Arch_Mage
            break
        elif "warden" in class_decision:
            global player_class_chosen
            player_class_chosen = Warden
            break
        elif "priest" in class_decision:
            global player_class_chosen
            player_class_chosen = Priest
            break
        elif "arcane_smith" in class_decision or "arcane" in class_decision or "smith" in class_decision:
            global player_class_chosen
            player_class_chosen = Arcane_Smith
            break
        elif "arch_caster" in class_decision or "caster" in class_decision:
            global player_class_chosen
            player_class_chosen = Arch_Caster
            break
        else:
            print "Please choose one of the available classes."
            continue

    global player_actual
    player_actual = player_class_chosen

#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

"""
Player stat customization
"""
def request_personal_stats():
    #Request Name
    print ""
    player_name = raw_input("What is your name: ")
    #Change Name
    player_actual["Name"] = player_name

    #Request Gender
    print ""
    gender_decision = raw_input("What is your preferred gender: ")
    #Change Gender
    player_actual["Gender"] = gender_decision

    #Request Birthday
    print ""
    bday_decision = raw_input("What is your birthday (Month|Year[Last 2 digits]): ")
    #Change Birthday
    player_actual["Birthday"] = bday_decision

#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

"""
Battle:
Use Level matching with mob. Multiplier to get mob stats. Create algorithm for
Luck and combat interactions.
"""

# Mob stats random assignment
def mob_element_assignment():
    rng_numb = random.random()
    assign_element = round(rng_numb, 2)
    if assign_element <= 0.20:
        base_mob["Element"] = "Fire"
    elif assign_element > 0.20 and assign_element <= 0.40:
        base_mob["Element"] = "Wind"
    elif assign_element > 0.40 and assign_element <= 0.60:
        base_mob["Element"] = "Earth"
    elif assign_element > 0.60 and assign_element <= 0.80:
        base_mob["Element"] = "Metal"
    elif assign_element > 0.80:
        base_mob["Element"] = "Water"
def mob_name_assignment():
    mob_name_rand = random.randint(0,30,)
    Mob_list = ["Leonard","Kmeq","Qlurydirs","Flem", "Cittaht", "Hound",
    "Dragon","Centaur","Glentrobs", "Vampire", "Scourge", "Zergling", "Teemo",
    "Forgotten", "Awoken","Hive","Vex","Fallen", "Jovian", "Taken", "Cabal",
    "Warlocks","Demons","Mercenary", "Bandit", "Rogue", "Assassin",
    "Anti-Net-Neutrality", "Memes", "Trump"]
    base_mob["Name"] = Mob_list[mob_name_rand-1]
def mob_stat_assignment():
    base_mob["Level"] = player_actual["Level"]
    stat_prob = {
        "0" : 0.90,
        "1" : 0.80,
        "2" : 0.80,
        "3" : 0.80,
        "4" : 0.80,
        "5" : 0.92,
        "6" : 0.75,
        "7" : 0.80,
        "8" : 0.82,
        "9" : 1.00,
        }
    global base_mob
    base_mob = initial_mob
    for i in range(base_mob["Level"]):
        for i in range(10):
            new = random.random()
            rounded_new = round(new, 2)
            if rounded_new < stat_prob[str(i)]:
                if i == 0:
                    base_mob["Health"] = initial_mob["Health"] + 1
                elif i == 1:
                    base_mob["Strength"] = initial_mob["Strength"] + 1
                elif i == 2:
                    base_mob["Stamina"] = initial_mob["Stamina"] + 1
                elif i == 3:
                    base_mob["Defense"] = initial_mob["Defense"] + 1
                elif i == 4:
                    base_mob["Resistance"] = initial_mob["Resistance"] + 1
                elif i == 5:
                    base_mob["Magic"] = initial_mob["Magic"] + 1
                elif i == 6:
                    base_mob["Speed"] = initial_mob["Speed"] + 1
                elif i == 7:
                    base_mob["Luck"] = initial_mob["Luck"] + 1
                elif i == 8:
                    base_mob["Intelligence"] = initial_mob["Intelligence"] + 1
                elif i == 9:
                    base_mob["Exp"] = initial_mob["Exp"] + 10

#Calling Everything
#Use these functions in creating the mob each time.
mob_element_assignment()
mob_name_assignment()
mob_stat_assignment()
# print base_mob to call the mob
# Spell | Combat Actions

#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
"""
Battle set-up (place after player_actual and boss and base_mob have been defined, but before battle function)
"""

"""
Elements Pentagon

< Fire < Water < Earth < Metal < Wind <

Hit Rate = (Weapons Accuracy + Intelligence + Luck)
Avoidance = (Speed + Luck/2)
Accuracy = Hit Rate (Attacker) - Avoidance (Defender) + Elements Pentagon

Physical Attack = Strength + (Weapon Might + Elemental Advantage) x Luck/2
Magic Attack = Magic + (Tome Might + Elemental Advantage x 2) x Luck/2

Defense(dmg_reduc) = (Defense + Intelligence) * Luck
Resistance(mag_dmg_reduc) = (Resistance + Intelligence * 4) * Luck

Physical Damage = Physical Attack - Defense
Magic Damage = Magic Attack - Resistance
"""
#Elements Pentagon Advantage Determinator

player_element = player_actual["Element"]
mob_element = base_mob["Element"]

def set_elemental_advantages():
    #Player elemental_advantage
    #Fire
    if player_element == "Fire":
        if mob_element == "Earth":
            global elemental_advantage
            elemental_advantage = 2
        elif mob_element == "Water":
            global elemental_advantage
            elemental_advantage = 0
        elif mob_element == "Metal":
            global elemental_advantage
            elemental_advantage = 2
        elif mob_element == "Wind":
            global elemental_advantage
            elemental_advantage = 5
        elif mob_element == "Fire":
            global elemental_advantage
            elemental_advantage = 3

    #Water
    if player_element == "Water":
        if mob_element == "Earth":
            global elemental_advantage
            elemental_advantage = 2
        elif mob_element == "Water":
            global elemental_advantage
            elemental_advantage = 0
        elif mob_element == "Metal":
            global elemental_advantage
            elemental_advantage = 2
        elif mob_element == "Wind":
            global elemental_advantage
            elemental_advantage = 5
        elif mob_element == "Fire":
            global elemental_advantage
            elemental_advantage = 3

    #Earth
    if player_element == "Earth":
        if mob_element == "Earth":
            global elemental_advantage
            elemental_advantage = 2
        elif mob_element == "Water":
            global elemental_advantage
            elemental_advantage = 0
        elif mob_element == "Metal":
            global elemental_advantage
            elemental_advantage = 2
        elif mob_element == "Wind":
            global elemental_advantage
            elemental_advantage = 5
        elif mob_element == "Fire":
            global elemental_advantage
            elemental_advantage = 3

    #Metal
    if player_element == "Metal":
        if mob_element == "Earth":
            global elemental_advantage
            elemental_advantage = 2
        elif mob_element == "Water":
            global elemental_advantage
            elemental_advantage = 0
        elif mob_element == "Metal":
            global elemental_advantage
            elemental_advantage = 2
        elif mob_element == "Wind":
            global elemental_advantage
            elemental_advantage = 5
        elif mob_element == "Fire":
            global elemental_advantage
            elemental_advantage = 3

    #Wind
    if player_element == "Wind":
        if mob_element == "Earth":
            global elemental_advantage
            elemental_advantage = 2
        elif mob_element == "Water":
            global elemental_advantage
            elemental_advantage = 0
        elif mob_element == "Metal":
            global elemental_advantage
            elemental_advantage = 2
        elif mob_element == "Wind":
            global elemental_advantage
            elemental_advantage = 5
        elif mob_element == "Fire":
            global elemental_advantage
            elemental_advantage = 3


    #Mob elemental_advantage
    #Fire
    if mob_element == "Fire":
        if player_element == "Earth":
            global mob_elemental_advantage
            mob_elemental_advantage = 2
        elif player_element == "Water":
            global mob_elemental_advantage
            mob_elemental_advantage = 0
        elif player_element == "Metal":
            global mob_elemental_advantage
            mob_elemental_advantage = 2
        elif player_element == "Wind":
            global mob_elemental_advantage
            mob_elemental_advantage = 5
        elif player_element == "Fire":
            global mob_elemental_advantage
            mob_elemental_advantage = 3

    #Water
    if mob_element == "Water":
        if player_element == "Earth":
            global mob_elemental_advantage
            mob_elemental_advantage = 2
        elif player_element == "Water":
            global mob_elemental_advantage
            mob_elemental_advantage = 0
        elif player_element == "Metal":
            global mob_elemental_advantage
            mob_elemental_advantage = 2
        elif player_element == "Wind":
            global mob_elemental_advantage
            mob_elemental_advantage = 5
        elif player_element == "Fire":
            global mob_elemental_advantage
            mob_elemental_advantage = 3

    #Earth
    if mob_element == "Earth":
        if player_element == "Earth":
            global mob_elemental_advantage
            mob_elemental_advantage = 2
        elif player_element == "Water":
            global mob_elemental_advantage
            mob_elemental_advantage = 0
        elif player_element == "Metal":
            global mob_elemental_advantage
            mob_elemental_advantage = 2
        elif player_element == "Wind":
            global mob_elemental_advantage
            mob_elemental_advantage = 5
        elif player_element == "Fire":
            global mob_elemental_advantage
            mob_elemental_advantage = 3

    #Metal
    if mob_element == "Metal":
        if player_element == "Earth":
            global mob_elemental_advantage
            mob_elemental_advantage = 2
        elif player_element == "Water":
            global mob_elemental_advantage
            mob_elemental_advantage = 0
        elif player_element == "Metal":
            global mob_elemental_advantage
            mob_elemental_advantage = 2
        elif player_element == "Wind":
            global mob_elemental_advantage
            mob_elemental_advantage = 5
        elif player_element == "Fire":
            global mob_elemental_advantage
            mob_elemental_advantage = 3

    #Wind
    if mob_element == "Wind":
        if player_element == "Earth":
            global mob_elemental_advantage
            mob_elemental_advantage = 2
        elif player_element == "Water":
            global mob_elemental_advantage
            mob_elemental_advantage = 0
        elif player_element == "Metal":
            global mob_elemental_advantage
            mob_elemental_advantage = 2
        elif player_element == "Wind":
            global mob_elemental_advantage
            mob_elemental_advantage = 5
        elif player_element == "Fire":
            global mob_elemental_advantage
            mob_elemental_advantage = 3


#Spells And Tome Might Defining

#Offensive Spells (for player)
#Fire
def Asterium():
    if player_actual["Element"] == "Fire":
        return 7
    else:
        return 5
    base_mob['Strength'] = base_mob['Strength'] - 1
    player_combat['Stamina'] = player_combat['Stamina'] - 1

#Earth
def Terraflice():
    if player_actual["Element"] == "Earth":
        return 8
    else:
        return 4
    base_mob['Defense'] = base_mob['Defense'] - 1
    player_combat['Stamina'] = player_combat['Stamina'] - 1

#Wind
def Ventusia():
    if player_actual["Element"] == "Wind":
        return 5
    else:
        return 3
    base_mob["Speed"] = base_mob["Speed"] - 1
    player_combat['Stamina'] = player_combat['Stamina'] - 1

#Water
def Aquerius():
    if player_actual["Element"] == "Water":
        return 9
    else:
        return 4
    base_mob["Magic"] = base_mob["Magic"] - 1
    player_combat['Stamina'] = player_combat['Stamina'] - 1

#Metal
def Metalon():
    if player_actual["Element"] == "Metal":
        return 7
    else:
        return 5
    base_mob["Resistance"] = base_mob["Resistance"] - 1
    player_combat['Stamina'] = player_combat['Stamina'] - 1


#Defensive Spells
#Fire
def Infernalia():
    if player_actual["Element"] == "Fire":
        player_combat["Strength"] = player_combat["Strength"] + 2
        player_combat["Magic"] = player_combat["Magic"] + 4
    else:
        player_combat["Strength"] = player_combat["Strength"] + 2
        player_combat["Magic"] = player_combat["Magic"] + 2
    player_combat['Stamina'] = player_combat['Stamina'] - 1

#Earth
def Leonius():
    if player_actual["Element"] == "Earth":
        player_combat["Health"] = player_combat["Health"] + 5
    else:
        player_combat["Health"] = player_combat["Health"] + 3
    player_combat['Stamina'] = player_combat['Stamina'] - 1

#Water
def Gionire():
    if player_actual["Element"] == "Water":
        player_combat["Resistance"] = player_combat["Resistance"] + 4
    else:
        player_combat["Resistance"] = player_combat["Resistance"] + 2
    player_combat['Stamina'] = player_combat['Stamina'] - 1

#Wind
def Nureilla():
    if player_actual["Element"] == "Water":
        player_combat["Speed"] = player_combat["Speed"] + 5
    else:
        player_combat["Speed"] = player_combat["Speed"] + 2
    player_combat['Stamina'] = player_combat['Stamina'] - 1

#Metal
def Xanthos():
    if player_actual["Element"] == "Metal":
        player_combat["Defense"] = player_combat["Defense"] + 5
    else:
        player_combat["Defense"] = player_combat["Defense"] + 2
    player_combat['Stamina'] = player_combat['Stamina'] - 1


mob_weapon_might = 10
mob_tome_might = 10
def player_weapons_accuracy():
    weapons_accuracy = 10 + 2 * player_combat["Level"]
    weapons_accuracy = int(weapons_accuracy)
    return weapons_accuracy
def player_weapon_might():
    weapon_might = 15 + 2 * player_combat["Level"]
    return weapon_might
#Hit Chance
def player_hit_rate():
    player_hit_rate = 1 - float((player_weapons_accuracy() + player_combat["Intelligence"]
    + player_combat["Luck"]))
    return player_hit_rate
#Avoidance
def player_avoidance():
    player_avoidance = (player_combat["Speed"] + float(player_combat["Luck"])/2)
    return player_avoidance

#AP = Attack Power
def player_AP():
    player_AP = player_combat["Strength"] + (player_weapon_might()
    + elemental_advantage) * float(player_combat["Luck"])/2
    player_AP = int(player_AP)
    return player_AP
#MP = Magic Power
def player_MP():
    player_MP = player_combat["Magic"] + ((tome_might + elemental_advantage
    * 2)) * (player_combat["Luck"])/2
    player_MP = int(player_MP)
    return player_MP
#DP = Defensive Power
def player_DP():
    player_DP = ((player_combat["Defense"] + player_combat["Intelligence"])
    * float(player_combat["Luck"])/4)
    player_DP = int(player_DP)
    return player_DP

#RP = Resistive Power
def player_RP():
    player_RP = ((player_combat["Resistance"] + player_combat["Intelligence"])
    * float(player_combat["Luck"])/2)
    player_RP = int(player_RP)
    return player_RP

# Mob Stuff
def mob_hit_rate():
    mob_hit_rate = 1 - float((player_weapons_accuracy() + base_mob["Intelligence"]
    + base_mob["Luck"]))
    return mob_hit_rate
#Avoidance
def mob_avoidance():
    mob_avoidance = (base_mob["Speed"] + float(base_mob["Luck"])/2)
    return mob_avoidance
#AP = Attack Power
def mob_AP():
    mob_AP = base_mob["Strength"] + (mob_weapon_might
    + mob_elemental_advantage/2) * float(base_mob["Luck"])/2
    mob_AP = int(mob_AP)
    return mob_AP
#MP = Magic Power
def mob_MP():
    mob_MP = base_mob["Magic"] + ((mob_tome_might + mob_elemental_advantage/2
    )) * (base_mob["Luck"])/2
    mob_MP = int(mob_MP)
    return mob_MP
#DP = Defensive Power
def mob_DP():
    mob_DP = ((base_mob["Defense"] + base_mob["Intelligence"])
    * float(base_mob["Luck"])/2)
    mob_DP = int(mob_DP)
    return mob_DP
#RP = Resistance Power
def mob_RP():
    mob_RP = ((base_mob["Resistance"] + base_mob["Intelligence"])
    * float(base_mob["Luck"])/2)
    mob_RP = int(mob_RP)
    return mob_RP

"""
Hit Rate - Avoidance then RNG gen number, if smaller, then hit, otherwise miss.
The Stamina is reduced by one. If Stamina = 0 Exit Combat Room. Stamina only
matters for the player.
"""

#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

"""
General battle function definition
"""

def battle():
        global base_mob
        base_mob = initial_mob
        base_mob["Health"] = 25

        player_combat = player_actual
        system('clear')
        sleep(1)
        print "You have entered combat with "+ str(base_mob['Name'])+ "!"
        sleep(1)
        print "When HP = 0, you lose! When Stamina = 0, you withdraw from battle"
        sleep(1)
        print "It's as if nothing happens... Good Luck " + str(player_actual["Name"]) + "!"
        print ""
        print "(Just to make the battle a bit more difficult..."
        sleep(1)
        print "you won't be able to see your opponent's attacks."
        sleep(1)
        print "They are using magic, after all.)"
        sleep(1)

        while base_mob["Health"] > 0 and player_combat["Health"] > 0 and player_combat["Stamina"] > 0:
            off = 0
            print ""
            print "Your current stats are:"
            sleep(1)
            print color.BOLD + "Health: " + color.END + str(player_combat["Health"])\
            + color.BOLD + ", Strength: " + color.END + str(player_combat["Strength"])\
            + color.BOLD + ", Magic: " + color.END + str(player_combat["Magic"])\
            + color.BOLD + ", Stamina: " + color.END + str(player_combat["Stamina"]) + ","
            print color.BOLD + "Speed: " + color.END + str(player_combat["Speed"])\
            + color.BOLD + ", Resistance: " + color.END + str(player_combat["Resistance"])\
            + color.BOLD + ", Defense: " + color.END + str(player_combat["Defense"])
            print ""
            sleep(1)
            print "The "+str(base_mob["Name"])+"'s current stats are:"
            print color.BOLD + "Health: " + color.END + str(base_mob["Health"])\
            + color.BOLD + ", Strength: " + color.END + str(base_mob["Strength"])\
            + color.BOLD + ", Magic: " + color.END + str(base_mob["Magic"])\
            + color.BOLD + ", Stamina: " + color.END + str(base_mob["Stamina"]) + ","
            print color.BOLD + "Speed: " + color.END + str(base_mob["Speed"])\
            + color.BOLD + ", Resistance: " + color.END + str(base_mob["Resistance"])\
            + color.BOLD + ", Defense: " + color.END + str(base_mob["Defense"])
            print ""
            print ""
            sleep(1)
            print "You have 2 Choices. 1) Weapon 2) Spell"
            print "---" * 20
            while True:
                choice = raw_input("> ").lower()
                if choice == "weapon":
                    #Calls the Algorithms
                    a = player_AP()
                    d = mob_DP()
                    pdmg = a - d # player damage dealt
                    if pdmg == 1 or pdmg == -1:
                        pdmg = 2*pdmg
                    if pdmg > 0:
                        pdmg = (-1)*pdmg
                    elif pdmg == 0:
                        pdmg = -8
                    else:
                        pass

                    phr = player_hit_rate()
                    mobavoi = mob_avoidance()
                    if -(phr - mobavoi)/45 > random.random():
                        #Affects the Actual Health of Mob
                        print ""
                        print "You hit it!"
                        print ""
                        base_mob["Health"] = base_mob["Health"] + (pdmg)
                        player_combat["Stamina"] = player_combat["Stamina"] - 1
                    elif -(phr - mobavoi)/45 < random.random():
                        print ""
                        print "Hit Missed"

                    #Mob Return Attack
                    return_attack = random.random()
                    mob_choice = round(return_attack, 2)

                    # mob uses weapon
                    if mob_choice > 0.5:
                        a = mob_AP()
                        d = player_DP()
                        mdmg = a - d

                        if mdmg == 1 or mdmg == -1:
                            mdmg = 2*mdmg
                        if mdmg > 0:
                            mdmg = (-1)*mdmg
                        elif mdmg == 0:
                            mdmg = -8
                        else:
                            pass

                        mhr = mob_hit_rate()
                        player_avoi = player_avoidance()
                        if -(mhr - player_avoi)/45 > random.random():
                            player_combat["Health"] = player_combat["Health"] + int(round(mdmg/10))

                    # mob uses spell
                    elif mob_choice <= 0.5:
                        a = mob_MP()
                        d = player_RP()
                        mdmg = a - d
                        if mdmg == 1 or mdmg == -1:
                            mdmg = 2*mdmg
                        if mdmg > 0:
                            mdmg = (-1)*mdmg
                        elif mdmg == 0:
                            mdmg = -8
                        else:
                            pass

                        mhr = mob_hit_rate()
                        player_avoi = player_avoidance()

                        if -(mhr - player_avoi)/45 > random.random():
                            player_combat["Health"] = player_combat["Health"] + int(round(mdmg/10))
                    break
                elif choice == "spell":
                    while True:
                        print ""
                        print color.BOLD + "Choose one of the following spells to use:" + color.END
                        print color.BOLD + "Offensive – " + color.END + "Asterium, Terraflice, Ventusia, Aquerius, Metalon"
                        print color.BOLD + "Defensive – " + color.END + "Infernalia, Leonius, Gionire, Nureilla, Xanthos"
                        #Calls the Algorithms

                        Spell_Choice = raw_input("> ").lower()

                        if Spell_Choice == "asterium":
                            tome_might = Asterium()
                            off = 1 # "off" for "offensive"
                        elif Spell_Choice == "terraflice":
                            tome_might = Terraflice()
                            off = 1
                        elif Spell_Choice == "ventusia":
                            tome_might = Ventusia()
                            off = 1
                        elif Spell_Choice == "aquerius":
                            tome_might = Aquerius()
                            off = 1
                        elif Spell_Choice == "metalon":
                            tome_might = Metalon()
                            off = 1
                        elif Spell_Choice == "infernalia":
                            Infernalia()
                            break
                        elif Spell_Choice == "leonius":
                            Leonius()
                            break
                        elif Spell_Choice ==  "gionire":
                            Gionire()
                            break
                        elif Spell_Choice ==  "nureilla":
                            Nureilla()
                            break
                        elif Spell_Choice == "xanthos":
                            Xanthos()
                            break
                        else:
                            print "That's  not a valid spell."
                            print "Please try again."
                            continue

                        if off == 1:
                            tome_might = Spell_Choice
                            a = player_AP()
                            d = mob_DP()
                            pdmg = a - d
                            if pdmg == 1 or pdmg == -1:
                                pdmg = 2*pdmg
                            if pdmg > 0:
                                pdmg = (-1)*pdmg
                            elif pdmg == 0:
                                pdmg = -8
                            else:
                                pass

                            phr = player_hit_rate()
                            mobavoi = mob_avoidance()
                            if -(phr - mobavoi)/45 > random.random():
                                #Affects the Actual Health of Mob
                                print ""
                                print "You hit it!"
                                print ""
                                base_mob["Health"] = base_mob["Health"] + (pdmg)
                                break
                            elif -(phr - mobavoi)/45 < random.random():
                                print "Hit Missed."
                                break

                            #Mob Return Attack
                            return_attack = random.random()
                            mob_choice = round(return_attack, 2)

                            # mob uses weapon
                            if mob_choice > 0.5:
                                a = mob_AP()
                                d = player_DP()
                                mdmg = a - d

                                if mdmg == 1 or mdmg == -1:
                                    mdmg = 2*mdmg
                                if mdmg > 0:
                                    mdmg = (-1)*mdmg
                                elif mdmg == 0:
                                    mdmg = -8
                                else:
                                    pass

                                mhr = mob_hit_rate()
                                player_avoi = player_avoidance()
                                if -(mhr - player_avoi)/45 > random.random():
                                    player_combat["Health"] = player_combat["Health"] + int(round(mdmg/10))

                            # mob uses spell
                            elif mob_choice <= 0.5:
                                a = mob_MP()
                                d = player_RP()
                                mdmg = a - d
                                if mdmg == 1 or mdmg == -1:
                                    mdmg = 2*mdmg
                                if mdmg > 0:
                                    mdmg = (-1)*mdmg
                                elif mdmg == 0:
                                    mdmg = -8
                                else:
                                    pass

                                mhr = mob_hit_rate()
                                player_avoi = player_avoidance()

                                if -(mhr - player_avoi)/45 > random.random():
                                    player_combat["Health"] = player_combat["Health"] + int(round(mdmg/10))
                            break
                    break
                else:
                    print "Please type either \"Weapon\" or \"Spell\" exactly as shown."
                    continue

        if player_combat["Health"] <= 0:
            lose()

        elif base_mob["Health"] <= 0:
            player_actual["Exp"] = player_actual["Exp"] + base_mob["Exp"]
            player_actual["Coins"] += 5

            if player_actual["Location"] == "Alice":
                player_actual["Coins"] += 50
                print color.BOLD +"Congratulations!" + color.END + " You have beaten " + base_mob["Name"] + "."
                print "You gain " + str(base_mob["Exp"]) + " Exp and 55 coins."

            elif base_mob == Fire_Boss:
                print color.BOLD +"Congratulations!" + color.END\
                + " You have beaten " + color.RED + "the Fire Boss" + color.END + "."
                global beat_fire
                beat_fire = True

            elif base_mob == Water_Boss:
                print color.BOLD +"Congratulations!" + color.END\
                + " You have beaten " + color.BLUE + "the Water Boss" + color.END + "."
                global beat_water
                beat_water = True

            elif base_mob == Wind_Boss:
                print color.BOLD +"Congratulations!" + color.END\
                + " You have beaten " + color.PURPLE + "the Wind Boss" + color.END + "."
                global beat_wind
                beat_wind = True

            elif base_mob == Earth_Boss:
                print color.BOLD +"Congratulations!" + color.END\
                + " You have beaten " + color.GREEN + "the Earth Boss" + color.END + "."
                global beat_earth
                beat_earth = True

            elif base_mob == Metal_Boss:
                print color.BOLD +"Congratulations!" + color.END\
                + " You have beaten " + color.DARKCYAN + "the Metal Boss" + color.END + "."
                global beat_metal
                beat_metal = True

            else:
                print color.BOLD +"Congratulations!" + color.END + " You have beaten " + base_mob["Name"] + "."
                print "You gain " + str(base_mob["Exp"]) + " Exp and 5 coins."

            level_up()

        elif player_combat["Stamina"] <= 0:
            print "You have lost your battle with " + base_mob["Name"] + "."
            print "You automatically withdraw."

            level_up()

        else:
            print "You have been launched into an abyss of faulty code."
            print "If you object to this turn of events, please contact the creators."

#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

"""
Mob battle function definition
"""

def mob_battle():
    set_elemental_advantages()
    mob_element_assignment()
    mob_name_assignment()
    mob_stat_assignment()

    battle()

#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

"""
Boss battle function definition
"""

def boss_battle():
    if player_actual["Location"] == "fire_boss_location":
        global base_mob
        base_mob = Fire_Boss
    elif player_actual["Location"] == "earth_boss_location":
        global base_mob
        base_mob = Earth_Boss
    elif player_actual["Location"] == "water_boss_location":
        global base_mob
        base_mob = Water_Boss
    elif player_actual["Location"] == "metal_boss_location":
        global base_mob
        base_mob = Metal_Boss
    elif player_actual["Location"] == "wind_boss_location":
        global base_mob
        base_mob = Wind_Boss

    set_elemental_advantages()

    battle()

#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

"""
Determines whether the player is prepared to fight a boss

This should be called when the player enters the boss location
"""

def should_battle_boss():
    if player_actual["Level"] > 10:
        locations[new_location]["text2"]()
        print ""
        sleep(1)
        print "You're about to fight a boss."
        sleep(1)
        print "Bosses are stronger than mobs, so there's a higher chance you'll die..."
        sleep(1)
        print "But, if you win this fight, you gain 500 exp."
        sleep(1)
        print ""
        print "And remember: you must defeat all five bosses before you can truly say you've taken over."
        sleep(1)
        print ""
        print "Good luck! And try not to die."
        sleep(1)
        boss_battle()

        current_location = player_actual["Location"]
        new_location = locations[current_location]["directions"]['Leave']
        player_actual["Location"] = new_location
        print "You are back in the middle of town."
        change_location()

    else:
        sleep(1)
        print "You are not yet strong enough to stand a chance in this battle."
        sleep(1)
        print ""
        print ""
        current_location = player_actual["Location"]
        new_location = locations[current_location]["directions"]['Leave']
        player_actual["Location"] = new_location
        print "You are back in the middle of town."
        change_location()


#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

"""
Magic Shop stuff (must go after boss_battle() definition and after player_actual definition)
"""

class MagicShop(object):
# init possibly uneeded. only use if there are variables common to every class.
    def __init__(self, name):
        self.shop_name = name
        self.shop_type = "n ERROR"
        self.available_merchandise = items

    def trade(self):
        while True:
            print ""
            print "What would you like to acquire?"
            print "Please type only the name of the item, exactly as you see it spelled in the catalogue."
            global item_to_take
            item_to_take = raw_input("> ").lower()
            if item_to_take in self.available_merchandise:
                break
            else:
                print "That is not a valid request."
                sleep(1)
                print "Please try again."
                continue
        while True:
            print "What would you like to trade for that item?"
            global item_to_give
            item_to_give = raw_input("> ").lower()
            if item_to_give in item_inventory:
                break
            else:
                print "You don't currently own that item."
                print "Please try again."
                continue

        # This is a usable version of the item to be removed from the shop's inventory.
        global to_take_usable
        to_take_usable = self.available_merchandise[item_to_take]

        # These are usable versions of the items the player wants to take and give.
        # These allow us to modify the player's stats.
        global player_stat_gained
        player_stat_gained = to_take_usable[1]
        #player_actual[item_to_take]

        global to_lose_usable
        to_lose_usable = item_inventory[item_to_give]
        global player_stat_lost
        player_stat_lost = to_lose_usable[1]
        #player_actual[item_to_give]


        self.available_merchandise.pop(item_to_take)
        item_inventory.pop(item_to_give)
        item_inventory.update({item_to_take : to_take_usable})
        player_actual[player_stat_gained] += to_take_usable[0]
        player_actual[player_stat_lost] -= to_lose_usable[0]

        print "Thank you for your business!"

        current_location = player_actual["Location"]
        new_location = locations[current_location]["directions"]['Leave']
        player_actual["Location"] = new_location
        print "You are back in the middle of town."
        change_location()


    def buy(self):
        while True:
            print ""
            print "What would you like to acquire?"
            print "Please type only the name of the item, as you see it spelled in the catalogue."
            item_to_take = raw_input("> ").lower()
            if not(item_to_take in self.available_merchandise):
                print "That is not a valid request."
                sleep(1)
                print "Please try again."
                continue
            else:
                break

        # This is a usable version of the item to be removed from the shop's inventory.
        global to_take_usable
        to_take_usable = self.available_merchandise[item_to_take]

        # This is a usable version of the item the player wants to take.
        # This allows us to modify the player's stats.
        global player_stat_gained
        player_stat_gained = to_take_usable[1]

        self.available_merchandise.pop(item_to_take)
        item_inventory.update({item_to_take : to_take_usable})
        player_class_chosen["Coins"] -= to_take_usable[0]
        #items.get(item_to_take[0]) had this before, wanted to save it just in case
        player_actual[player_stat_gained] += to_take_usable[0]

        print "Thank you for your business!"

        current_location = player_actual["Location"]
        new_location = locations[current_location]["directions"]['Leave']
        player_actual["Location"] = new_location
        print "You are back in the middle of town."
        change_location()

    def shop(self):
        print ""
        print "Here is the current shop inventory:"
        print ""
        sleep(1)
        print self.available_merchandise
        print ""
        sleep(1)
        print "Each item corresponds to a number and a stat."
        sleep(1)
        print "The number represents both how much the item will cost you"
        sleep(1)
        print "and how much it will increase the corresponding stat."
        print ""
        sleep(1)

        while True:
            if item_inventory and player_actual["Coins"] > 0:
                print "Would you like to buy something, trade something, or leave the shop?"
                break

            elif item_inventory and player_actual["Coins"] == 0:
                print "Would you like to trade or leave?"
                break

            elif not(item_inventory) and player_actual["Coins"] > 0:
                print "Would you like to buy something or leave the shop?"
                break

            elif not(item_inventory) and player_actual["Coins"] == 0:
                print "The shopkeeper won't be happy with a non-customer hanging around it their shop."
                print "Do you want to leave now, or stay and risk confronting the angry shopkeeper?"
                break

            else:
                pass

        while True:
            buy_or_trade = raw_input("> ").lower()

            if "buy" in buy_or_trade:
                self.buy()
                break

            elif "trade" in buy_or_trade:
                self.trade()
                break

            elif "leave" in buy_or_trade:
                print "Thank you for visiting the magic shop."
                current_location = player_actual["Location"]
                new_location = locations[current_location]["directions"]['Leave']
                player_actual["Location"] = new_location
                print "You are back in the middle of town."
                change_location()
                break

            elif "stay" in buy_or_trade:
                if player_actual["Element"] == self.element:
                    print color.BOLD + "Shop Owner:" + color.END
                    print "I won't go so far as to fight someone of my same element,"
                    print "but neither will I tolerate loitering in my shop."
                    sleep(1)
                    print "Leave."
                    sleep(1)
                    move = 'Leave'
                    break
                else:
                    shop_owner_battle()
                    break
            elif buy_or_trade == "Q":
              break

            else:
                print "You're not making sense."
                sleep(1)
                print "Please try again."
                continue


    def first_shop(self):
        global shopped_before
        shopped_before = True
        print "Welcome to the Magic Shop!"
        sleep(1)
        print "This is a%s shop." % self.shop_type
        sleep(1)
        print "At a Magic Shop, you can buy or trade magic items to change your stats."
        print ""
        sleep(1)
        print "You can only pay or trade for one item while you're here,"
        print "then you have to move on and explore some more!"
        print ""
        sleep(1)
        print "You currently have " + str(player_actual["Coins"]) + " coins"
        sleep(1)
        print "and the following items:"
        sleep(1)
        print item_inventory
        sleep(1)
        print ""
        self.shop()


    def shop_again(self):
        print "Welcome to the Magic Shop!"
        sleep(1)
        print "This is a%s shop." % self.shop_type
        sleep(1)
        print "You currently have " + str(player_actual["Coins"]) + " coins"
        sleep(1)
        print "and the following items:"
        sleep(1)
        print item_inventory
        sleep(1)
        self.shop()

    def first_or_again(self):
        if shopped_before:
            system('clear')
            self.shop_again()
            print ""
            sleep(1)
        else:
            system('clear')
            self.first_shop()
            print ""
            sleep(1)


class Earth(MagicShop):
    def __init__(self, name):
        super(Earth, self).__init__(name)
        self.shop_type = "n earth"
        self.knows_name = True
        self.element = "Earth"
        self.available_merchandise = items

class Fire(MagicShop):
    def __init__(self, name):
        super(Fire, self).__init__(name)
        self.shop_type = " fire"
        self.knows_name = True
        self.element = "Fire"
        self.available_merchandise = items

class Water(MagicShop):
    def __init__(self, name):
        super(Water, self).__init__(name)
        self.shop_type = " water"
        self.knows_name = True
        self.element = "Water"
        self.available_merchandise = items

class Wind(MagicShop):
    def __init__(self, name):
        super(Wind, self).__init__(name)
        self.shop_type = " wind"
        self.knows_name = True
        self.element = "Wind"
        self.available_merchandise = items

class Metal(MagicShop):
    def __init__(self, name):
        super(Metal, self).__init__(name)
        self.shop_type = " metal"
        self.knows_name = True
        self.element = "Metal"
        self.available_merchandise = items

def shop_owner_battle():
    print "The shop owner (as you were warned...) is angered"
    print "by your stubborn refusal to leave"
    print "despite not being a customer."
    print ""
    sleep(1)
    print "The shop owner pushes a button"
    print "and a previously hidden door opens up in the back of the shop."
    print ""
    sleep(1)
    print color.BOLD + "A monster!" + color.END
    print ""
    input_to_allow_reading = raw_input("> ")
    mob_battle()

    current_location = player_actual["Location"]
    new_location = locations[current_location]["directions"]['Leave']
    player_actual["Location"] = new_location
    print "You are back in the middle of town."
    change_location()

earth_shop = Earth("Earth Shop")

fire_shop = Fire("Fire Shop")

water_shop = Water("Water Shop")

wind_shop = Wind("Wind Shop")

metal_shop = Metal("Metal Shop")

#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

"""
Text defintions
"""

def glasscastle_text():
    print ""
    print ""
    print "The castle towers above you, made completely out of glass."
    sleep(1)
    print "You see glass chandeliers, glass tables, and glass crowns."
    sleep(1)
    print "You enter through the glass double doors and look around in amazement."
    sleep(1)
    print "You walk through all the rooms, winding your way up the glass staircase until you reach the top."
    sleep(1)
    print "At the top, you stop in shock..."
    sleep(1)

def inn_text():
    print ""
    print ""
    print "The inn is quite crowded."
    sleep(1)
    print "You can tell that all the people are locals by the way that they chat with each other."
    sleep(1)
    print "You ask the bartender for a drink and sit down at a small table by yourself."
    sleep(1)
    print "A tall woman approaches you. She seems to emit a kind, even caring, aura."
    print "It does make you feel as if something's slightly off, though..."
    sleep(1)
    print "She starts speaking:"
    print "\"Welcome! I'm the innkeeper."
    sleep(1)
    print "I assume you're a traveller; I haven't seen you around before."
    sleep(1)
    print "As you can see, we're quite busy at the moment."
    sleep(1)
    print "This is a popular place to stay among locals who are"
    print "travelling for trade deals, out to hand-pick some magical materials,"
    print "or simply wishing to get away from home for a bit."
    sleep(1)
    print "Because you're not familiar with the Inn, you might not know how quickly rooms can fill up..."
    sleep(1)
    print "So, I thought I'd approach you before it was too late."
    sleep(1)
    print "Would you like to rent a room for the night?\""
    sleep(1)

def hermit_text():
    print ""
    print ""
    print "As you enter the cave, you look around at the moss on the walls."
    sleep(1)
    print "In a corner of the cave, you see a pile of paper scrolls piled up."
    sleep(1)
    print "You hear a noise from behind you and you turn to see the Hermit."
    sleep(1)
    print "'Can you help me?' you ask apprehensively."
    sleep(1)
    print "He nods solemnly."
    sleep(1)
    print "An odd feeling washes over you."
    sleep(1)
    print "For a while, you and the Hermit stare into each others' eyes..."
    sleep(1)
    print "He smiles."
    sleep(1)
    print "Feeling a bit awkward, you hesitantly smile back, turn around, and leave."
    sleep(1)

def market_text():
    print ""
    print ""
    print "The marketplace is flooded with people of all different classes and backgrounds."
    sleep(1)
    print "It seems to be the meeting place for everyone."
    sleep(1)
    print "Wizards walk around looking for the best wands."
    sleep(1)
    print "Shopkeepers gossip with each other and try to reel you into their shops."
    sleep(1)
    print "The mess of sound and people overwhelm you as you walk around."
    sleep(1)
    print "However, the marketplace seems like the best place to be if you are looking for magic, or trouble, or both..."
    sleep(1)
    print "True to your intuition, you soon hear screams and see several townspeople running toward you."
    sleep(1)
    print "Behind them, you spot an enormous figure barreling in your direction!"
    sleep(1)

def alice_text():
    print ""
    print ""
    print "You fall backwards onto a pile of leaves."
    sleep(1)
    print "But the ground collapses beneath you and you are falling..."
    sleep(1)
    print "The leaves swirl around you and you feel the wind rush past your ears."
    sleep(1)
    print "You frantically twist and turn in the air trying to get a sense of where you are and how to stop falling."
    sleep(1)
    print "You see light below you and you are falling and falling towards it."
    sleep(1)
    print "When you can finally see clearly, you see objects floating around you."
    sleep(1)
    print "There are all random objects that range in size and use."
    sleep(1)
    print "To your left is a gold, gilded mirror and to your right is a shell with white spirals."
    sleep(1)
    print "The falling seems endless and you feel your heart sinking."
    sleep(1)
    print "How will you ever stop falling?"
    sleep(1)

def pirate_text():
    print ""
    print ""
    print "You awake with the smell of salt water and fish in your nose."
    sleep(1)
    print "You are drenched and shivering in a nearly pitch black room."
    sleep(1)
    print "One ray of light is escaping from a hatch above your head."
    sleep(1)
    print "You push on the hatch until it slowly and creakily opens."
    sleep(1)
    print "Blinking to ward off the blinding wave of light, you find that you are standing on the deck of a ship."
    sleep(1)
    print "A pirate ship."
    sleep(1)
    print "\"Well... who do we have here?\", a voice from behind you growls."
    sleep(1)
    print "You feel the hair on the back of your neck stand up and you turn to find yourself face to face with a menacing pirate Captain."
    sleep(1)
    print "\"I don't take intrusions into my territory lightly.\""
    sleep(1)
    print "The pirate whistles loudly – louder than you thought it was possible to whistle –"
    sleep(1)
    print "and out of the water, something comes slithering toward you..."

def forest1_text():
    print ""
    print ""
    print "You enter the forest nervously, prepared for the worst."
    sleep(1)
    print "As soon as you hear a sound, you rip your head in the direction of the noise, hands out and eyes wide."
    sleep(1)
    print "Out of the trees, a monstrous bull appears."
    sleep(1)
    print "The bull steps into the clearing and lowers its head, its horns gleaming in the moonlight."
    sleep(1)
    print "You back away slowly... but your foot steps on a twig with a sharp snapping sound."
    sleep(1)
    print "The bull's eyes flash red and it charges!"
    sleep(1)
    print "What will you do now?"
    sleep(1)

def forest2_text():
    print ""
    print ""
    print "You enter the forest nervously, prepared for the worst."
    sleep(1)
    print "As soon as you hear a sound, you rip your head in the direction of the noise, hands out and eyes wide."
    sleep(1)
    print "The tree behind you moves slowly."
    sleep(1)
    print "You scream as the tree opens its wise eyes and looks at you wonderingly."
    sleep(1)
    print "\"Welcome traveller,\" the tree says, as it reaches its branches towards you holding something out."
    sleep(1)
    print "\"I can help you on your journey to defeat the Elements if you will take my gift,\""
    sleep(1)
    print "You take the package that the tree has unveiled and thank the tree in complete wonder."
    sleep(1)
    print "You leave the forest feeling refreshed and rejuvinated."
    sleep(1)

def fire_boss_text():
    print ""
    print ""
    print "I’m sorry I wasn’t expecting such an… underwhelming sight…"
    print "Who let this tiny little thing in here?"
    print "When they told me to expect a real battle, you’re quite frankly the last thing I expected to see."
    print "The ruler of fire realm does not have time for fights that don’t even ignite a spark of my efforts."
    print "You think you can walk in here and defeat me? Who do you think you are?"
    print "If you really insist, it’s your death sentence honey."
    print "When you play with fire, you might get burned…"
    print "but don’t worry about the pain your nerves will be the first to go."

def earth_boss_text():
    print ""
    print ""
    print "Hello fellow guest,"
    print "it’s come to my attention that you are causing havoc in my kingdom."
    print "Are you sure we want to settle our differences through violence?"
    print "Do you see what a disturbance you have created already?"
    print "Man, violence is never the answer…"
    print "That’s the problem with this world."
    print "We try to solve all our problems with our fists,"
    print "we just need to spread more love and positivity in the world, you know?"
    print "That’s what I’m trying to make the earth realm all about."
    print "But hey bro if you’re coming into my realm with bad intentions,"
    print "that’s not gonna work for me or my fellow brother and sisters."
    print "I’m going to have to remove you from my space, I only want positive vibes here..."

def wind_boss_text():
    print ""
    print ""
    print "What do you mean you want to challenge me?"
    print "You… an insignificant little human…."
    print "Think you could take on the boss of the wind realm?"
    print "You must be lost little human."
    print "I don’t want you to suffer the consequences because you’re in the wrong place at the wrong time."
    print "Do you know my strength?"
    print "Do you realize the depth of my wrath?"
    print "I have power you could not even imagine."
    print "If you really insist on battling against me,"
    print "the boss of the wind realm never turns down a fight and you will face my wrath."
    print "You may think you might be able to handle me because you’ve met my lesser comrades of the other realms"
    print "but there’s no water around here and you’re about to get blown away..."

def water_boss_text():
    print ""
    print ""
    print "My kingdom is flooded with requests to battle me"
    print "so why exactly should I give you the time of day?"
    print "The bosses of Fire and Wind have been badgering me"
    print "about how I take on the weakest fights to boost my ego and I’m tired of it."
    print "Why waste my time?"
    print "We have the power of tsunamis and whirlpools"
    print "and they have the nerve to challenge my power with a little breeze and flame?"
    print "It’s time I prove them wrong and show them the true force of water."
    print "Since you seem to also doubt my power like those arrogant fools,"
    print "I’ll start with you. Let the battle begin..."
    print "Time to wave goodbye to the world as you know it…"

def metal_boss_text():
    print ""
    print ""
    print "Heyyy no one told me we were having guests over!!"
    print "How you doing?"
    print "Care for a drink?"
    print "Ever since dad left the metal realm I have been living:"
    print "endless supplies of booze, parties, and girls…"
    print "It’s the only way to live if you ask me"
    print "but for some reason Dad keeps pestering me about being a “real leader” to our people"
    print "and maintaining a front of power against the other realms"
    print "but I couldn't care less about all that…"
    print "Wait hold up you’re not here to party?"
    print "You want to fight?"
    print "Man I’ll never understand why everyone in this damn world always wants to fight"
    print "when we could be sharing a drink instead.."
    print "But hey if you insist…"
    print "All I’m saying is you should most definitely be intimidated by these guns of steel,"
    print "they’re even stronger than they look so that says a lot..."

def land_text():
    sleep(1)
    print "You look around,"
    print "and notice a nearby shop with odd sounds and lights coming through the windows."
    sleep(1)
    print ""
    print "Further out, you notice a large, regal-looking building"
    print "which the townsfolk seem to be avoiding."
# to be used for the text for the five lands (the five text definitions below this one)

def metal_text():
    print ""
    print ""
    print "You are now in the land of Metal."
    land_text()

def fire_text():
    print ""
    print ""
    print "You are now in the land of Fire."
    land_text()

def water_text():
    print ""
    print ""
    print "You are now in the land of Water."
    land_text()

def wind_text():
    print ""
    print ""
    print "You are now in the land of Wind."
    land_text()

def earth_text():
    print ""
    print ""
    print "You are now in the land of Earth."
    land_text()

def blank():
    pass

#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

"""
Action function defintions
"""

def mob_action():
    input_to_allow_reading = raw_input("> ")
    mob_battle()
    change_location()

def inn_action():
    while True:
        response = raw_input("> ").lower()

        if "n" in response:
            print "\"Alright. It was nice meeting you " + player_actual["Name"] + "."
            sleep(1)
            print "Please do come again soon!\""
            print ""
            sleep(1)
            print "You finish your drink, then exit the Inn."
            change_location()
            break

        elif "y" in response or "i would":
            print "\"Wonderful! I'll book a room for you right away, " + player_actual["Name"] + ".\""
            sleep(1)
            print ""
            print "You stay the night at the Inn in a comfortable room with a comfortable bed"
            sleep(1)
            print "and wake feeling much better than you did the night before."
            change_location()
            break

        else:
            print "\"Sorry, dear... I didn't catch that..."
            print "Would you mind rephrasing?\""
            continue

def hermit_action():
    player_actual["Magic"] += 10
    player_actual["Defense"] += 5
    player_actual["Intelligence"] += 5
    change_location()

def alice_action():
    if player_actual["Level"] > 5:
        print ""
        print "Finally you land."
        sleep(1)
        print "But only to find yourself in a dark room"
        sleep(1)
        print "with no visible exits"
        sleep(1)
        print ""
        print "You can see the outline of a looming figure only a few feet in front of you."
        input_to_allow_reading = raw_input("> ")
        mob_battle()
        change_location()

    else:
        print ""
        print "Finally you land."
        sleep(1)
        print ""
        print "You land hard."
        sleep(1)
        print "It actually hurt quite a bit."
        sleep(1)
        print ""
        print "But then, you look around you..."
        sleep(1)
        print ""
        print "You've landed in an enormous pile of gold!"
        sleep(1)
        print ""
        print "Would you like to take some, or leave it be?"
        choice = raw_input("> ").lower()

        if "take" in choice or "get" in choice:
            print ""
            print "You scoop up about 50 coins worth of gold!"
            sleep(1)
            print "But then, you hear a loud rumbling..."
            sleep(1)
            print "A doorway opens on one side of the room..."
            sleep(1)
            print "And out steps a monster!"
            sleep(1)
            print ""
            print "You'll only be able to keep the gold if you defeat the monster."
            sleep(1)
            print "So do your best to win!"
            sleep(1)
            print ""
            input_to_allow_reading = raw_input("> ")
            mob_battle()

            change_location()
        else:
            print "You're suddenly back next to the pile of leaves."
            sleep(1)
            print "Too bad you missed out on all that gold."
            sleep(1)
            change_location()

def forest_action():
    if player_actual["Level"] > 7:
        forest1_text()
        input_to_allow_reading = raw_input("> ")
        mob_battle()
        change_location()
    else:
        forest2_text()

        player_actual["Health"] += 5
        player_actual["Magic"] += 5
        player_actual["Stamina"] += 8

        change_location()

def boss_action():
    should_battle_boss()

def land_action():
    change_location()

def metal_shop_action():
    metal_shop.first_or_again()
    change_location()

def fire_shop_action():
    fire_shop.first_or_again()
    change_location()

def water_shop_action():
    water_shop.first_or_again()
    change_location()

def wind_shop_action():
    wind_shop.first_or_again()
    change_location()

def earth_shop_action():
    earth_shop.first_or_again()
    change_location()

#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

"""
Location dictionary definition
"""
# Contains:
    # sub-dictionary for each location
    # key for location text
    # a sub-sub-dictionary for directions, which contains:
        # keys for directions of motion
        # corresponding to new locations
locations = {
    "Metal": {"text":metal_text, "directions": {'North':"Fire",'South':"Water",\
    'East':"Earth",'West':"Wind", 'Shop': "metal_shop", 'Building': "metal_boss_location"},\
    "action": land_action},

    "Fire": {"text":fire_text, "directions": {'South':"Metal",\
    'East':"GlassCastle",'West':"Market", 'Shop': "fire_shop", 'Building': "fire_boss_location"},\
    "action": land_action},

    "Water": {"text":water_text, "directions": {'North':"Metal",'South':"Pirate",\
    'East':"Inn",'West':"Hermit", 'Shop': "water_shop", 'Building': "water_boss_location"},\
    "action": land_action},

    "Wind": {"text":wind_text, "directions": {'North':"Market",'South':"Hermit",\
    'East':"Metal",'West':"Alice", 'Shop': "wind_shop", 'Building': "wind_boss_location"},\
    "action": land_action},

    "Earth": {"text":earth_text, "directions": {'North':"GlassCastle",'South':"Inn",\
    'East':"Forest",'West':"Metal", 'Shop': "earth_shop", 'Building': "earth_boss_location"},\
    "action": land_action},

    "GlassCastle": {"text":glasscastle_text, "directions": {'West':"Fire",'South':"Earth"},\
    "action": mob_action},

    "Inn": {"text":inn_text, "directions": {'North':"Earth",'West':"Water"},\
    "action": inn_action},

    "Hermit": {"text":hermit_text, "directions": {'North':"Wind", 'East':"Water"},\
    "action": hermit_action},

    "Market": {"text":market_text, "directions": {'South':"Wind",'East':"Fire"},\
    "action": mob_action},

    "Alice": {"text":alice_text, "directions": {'East':"Wind"},\
    "action": alice_action},

    "Pirate": {"text":pirate_text, "directions": {'North':"Water"},\
    "action": mob_action},

    "Forest": {"text": blank, "directions": {'West':"Earth"},\
    "action": forest_action},

    "metal_boss_location": {"text2":metal_boss_text, "text":blank, "directions": {'Leave':"Metal"},\
    "action": boss_action},

    "fire_boss_location": {"text2":fire_boss_text, "text":blank, "directions": {'Leave':"Fire"},\
    "action": boss_action},

    "water_boss_location": {"text2":water_boss_text, "text":blank, "directions": {'Leave':"Water"},\
    "action": boss_action},

    "wind_boss_location": {"text2":wind_boss_text, "text":blank, "directions": {'Leave':"Wind"},\
    "action": boss_action},

    "earth_boss_location": {"text2":earth_boss_text, "text":blank, "directions": {'Leave':"Earth"},\
    "action": boss_action},

    "metal_shop": {"text": blank, "directions": {'Leave':"Metal"},\
    "action": metal_shop_action},

    "fire_shop": {"text": blank, "directions": {'Leave':"Fire"},\
    "action": fire_shop_action},

    "water_shop": {"text": blank, "directions": {'Leave':"Water"},\
    "action": water_shop_action},

    "wind_shop": {"text": blank, "directions": {'Leave':"Wind"},\
    "action": wind_shop_action},

    "earth_shop": {"text": blank, "directions": {'Leave':"Earth"},\
    "action": earth_shop_action},
    }

#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

"""
Leveling up
"""

def level_up_mechanism():
    pass

#Exp Level Up Mechanism
#Exp isn't reset, it's a cap value
level_ranges ={
    1 : 0,
    2 : 60,
    3 : 140,
    4 : 240,
    5 : 360,
    6 : 540,
    7 : 760,
    8 : 1040,
    9 : 1360,
    10 : 1720,
    11 : 2100,
    12 : 2500,
    13 : 2920,
    14 : 3380,
    15 : 3500,
    16 : 9999999,
}

# Probabilities by class
#Arch Mage
def arch_mage_level_up():
    global stat_prob
    stat_prob = {
        "0" : 0.74,
        "1" : 0.58,
        "2" : 0.81,
        "3" : 0.77,
        "4" : 0.79,
        "5" : 0.94,
        "6" : 0.67,
        "7" : 0.86,
        "8" : 0.90,
        }
    level_up_mechanism(level_change)

#Warden
def warden_level_up():
    global stat_prob
    stat_prob = {
        "0" : 0.96,
        "1" : 0.80,
        "2" : 0.83,
        "3" : 0.90,
        "4" : 0.84,
        "5" : 0.60,
        "6" : 0.65,
        "7" : 0.71,
        "8" : 0.69,
        }
    level_up_mechanism(level_change)

#Arch_Caster
def arch_caster_level_up():
    global stat_prob
    stat_prob = {
        "0" : 0.65,
        "1" : 0.72,
        "2" : 0.87,
        "3" : 0.85,
        "4" : 0.81,
        "5" : 0.97,
        "6" : 0.75,
        "7" : 0.68,
        "8" : 0.90,
        }
    level_up_mechanism(level_change)

#Priest
def priest_level_up():
    global stat_prob
    stat_prob = {
        "0" : 0.96,
        "1" : 0.65,
        "2" : 0.58,
        "3" : 0.64,
        "4" : 0.93,
        "5" : 0.92,
        "6" : 0.65,
        "7" : 0.88,
        "8" : 0.95,
        }
    level_up_mechanism(level_change)

#Arcane Smith
def arcane_smith_level_up():
    global stat_prob
    stat_prob = {
        "0" : 0.78,
        "1" : 0.90,
        "2" : 0.88,
        "3" : 0.79,
        "4" : 0.79,
        "5" : 0.85,
        "6" : 0.80,
        "7" : 0.83,
        "8" : 0.94,
        }
    level_up_mechanism(level_change)

"""
Order of Stat Growths
"Health_Growth_Probability"
"Strength_Growth_Probability"
"Stamina_Growth_Probabilty"
"Defense_Growth_Probability"
"Resistance_Growth_Probability"
"Magic_Growth_Probabilty"
"Speed_Growth_Probability"
"Luck_Growth_Probability"
"Intelligence_Growth_Probability"
"""
# level up mechanism
def level_up_mechanism(level_change):
    player_actual["Level"] += level_change
    for i in range(8):
        new = random.random()
        rounded_new = round(new, 2)
        if rounded_new < stat_prob[str(i)]:
            if i == 0:
                player_actual["Health"] = player_actual["Health"] + 1
            elif i == 1:
                player_actual["Strength"] = player_actual["Strength"] + 1
            elif i == 2:
                player_actual["Stamina"] = player_actual["Stamina"] + 1
            elif i == 3:
                player_actual["Defense"] = player_actual["Defense"] + 1
            elif i == 4:
                player_actual["Magic"] = player_actual["Magic"] + 1
            elif i == 5:
                player_actual["Speed"] = player_actual["Speed"] + 1
            elif i == 6:
                player_actual["Luck"] = player_actual["Luck"] + 1
            elif i == 7:
                player_actual["Intelligence"] = player_actual["Intelligence"] + 1
    print player_actual


def level_up():
    print "---" * 20
    for i in range(15):
        if player_actual["Exp"] > level_ranges[i+1] and player_actual["Exp"] < level_ranges[i+2]:
            new_level = i+1

            global level_change
            level_change = new_level - player_actual["Level"]

            if player_actual["Class"] == "Arch_Mage":
                arch_mage_level_up()
            elif player_actual["Class"] == "Warden":
                warden_level_up()
            elif player_actual["Class"] == "Priest":
                priest_level_up()
            elif player_actual["Class"] == "Arch_Caster":
                arch_caster_level_up()
            elif player_actual["Class"] == "Arcane_Smith":
                arcane_smith_level_up()

        global level
        level = i+1
    print ""
    print "Your level is currently " + str(player_actual["Level"]) + "."

#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

"""
Location changing
"""

def change_location():
    current_location = player_actual["Location"]

    if has_started:
        system('clear')

    if beat_metal and beat_fire and beat_earth and beat_wind and beat_water:
        win()

    print ""
    print "Here are your current stats:"
    sleep(1)
    print player_actual

    try:
        while True:
            sleep(1)
            print ""
            print ""
            print "From here, you can move"
            print "(or, rather, teleport – we've advanced past walking, thank you very much)"
            print "to any of the following locations:"
            print ""
            for key in locations[current_location]["directions"]:
                sleep(1)
                print " - " + key

            print ""
            sleep(1)
            print "Where would you like to go?"
            where_to = raw_input("> ").lower()

            if "building" in where_to:
                global new_location
                new_location = locations[current_location]["directions"]["Building"]
                break

            elif "shop" in where_to:
                global new_location
                new_location = locations[current_location]["directions"]["Shop"]
                break

            elif "n" in where_to or "north" in where_to:
                global new_location
                new_location = locations[current_location]["directions"]["North"]
                break

            elif "w" in where_to or "west" in where_to:
                global new_location
                new_location = locations[current_location]["directions"]["West"]
                break

            elif "e" in where_to or "east" in where_to:
                global new_location
                new_location = locations[current_location]["directions"]["East"]
                break

            elif "s" in where_to or "south" in where_to:
                global new_location
                new_location = locations[current_location]["directions"]["South"]
                break

            else:
                print "That's not a valid location."
                sleep(1)
                print "Try again."
                continue

    except KeyError:
        print "You have teleported into the deep, dark, oblivion of not following instructions."
        print "Unfortunately, this is a fairly common mistake among beginning magic users."
        print "At any rate..."
        lose()

    player_actual["Location"] = new_location

    system('clear')

    locations[new_location]["text"]()

    locations[new_location]["action"]()

    global has_started
    has_started = True

#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

"""
start() function ––> runs the game
"""

# The ENTIRE game should be run by this.
# start() should be the only function called outside of any sub-unit of code.
def start():
    system('clear')

    game_intro_text()

    while True:
        display_character_options()

        character_creation_text()

        create_a_character()

        request_personal_stats()

        # Player satisfaction confirmation
        system('clear')
        sleep(1)
        print "These are your current stats:"
        print ""
        sleep(1)
        print player_class_chosen
        print ""
        sleep(1)
        print "Are you satisfied with these results?"
        satisfied = raw_input("> ").lower()

        if "m not" in satisfied or "n" in satisfied:
            system('clear')
            continue
        elif "y" in satisfied or "m satisfied" in satisfied or "i am" in satisfied:
            break
        else:
            system('clear')
            continue

    system('clear')

    current_location = player_actual["Location"]
    locations[current_location]["text"]()
    locations[current_location]["action"]()

    global player_combat
    player_combat = player_actual
    # This definition of player_combat is needed for battles.
    # It must be defined after player_actual has been defined in create_a_character()




start()
#
