import os
import random
import time

global me
class Room:
    global me
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
        self.items = {}
        self.props = {}
        self.item_paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)

    def add_items(self, items):
        self.items.update(items)

    def del_items(self, items):
        del self.items[items]

    def add_props(self, props):
        self.props.update(props)

    def add_item_path(self,item_path):
        self.item_paths.update(item_path)

    def check_item_paths(self):
        for item in me.items:
            try:
                self.add_paths(self.item_paths[item])
            except:
                continue

class Character:
    global me
    def __init__(self, name):
        self.name = name
        self.items = {}
        self.hungry = False
        self.riddle_yes = False


    def add_items(self, items):
        self.items.update(items)

    def del_items(self, items):
        del self.items[items]


examine_list = ['look','examine']
take_list = ['take','pick','grab','get']
drop_list = ['drop', 'put down', 'throw']

strange = Room('STRANGE ROOM', 'you are in a small stone room, \nit appears normal but you feel a ...strange... energy\n\na shriveled old human sleeps in the corner -\nsleep talking like an insane person')
hell = Room("HELL", "you enter a large cavern \na river of lava flows next to you \nthere are stairs leading downward")
dirt_room = Room('DIRT ROOM',"""
the ground is covered in dirt
on the eastern wall there is a sign that reads:
    "Logan's Lettuce Dungeon -
        ye who enter shall not leave until obtaining the lettuce
        or thou shalt be smited"

10 feet above the sign there is a doorway
to the south there is a doorway
to the north there is a doorway
""")
dirt_roomP = Room('DIRT ROOM PAST',"""
the ground is covered in dirt
on the eastern wall there is a sign that reads:
    "Congrats on figuring out how to time travel!
    Remember, it's difficult to travel between rooms
    while not in the present.
    Time travel can reveal things about rooms
    and help solve 'puzzles'...
    Have fun traveller!"

10 feet above the sign there is a doorway
to the south there is a doorway
to the north there is a doorway
""")
dirt_roomF = Room('DIRT ROOM FUTURE',"""
the ground is covered in dirt
on the eastern wall there is a sign that reads:
    "congrats on figuring out how to time travel!
    Remember, its difficult to travel between rooms
    while not in the present.
    Time travel can reveal things about rooms
    and help solve 'puzzles'...
    Have fun traveller!"

10 feet above the sign there is a doorway
to the south there is a doorway
to the north there is a doorway
""")
#jack's rooms and stuff:

start_dialogue1 = Room("", "Gaining consciousness, you feel your back pressed against \
a cold, stone wall. \n (press enter to continue)")
start_dialogue2 = Room("", "You open your eyes to find yourself in a small room \
built entirely of stone. \n (press enter to continue)")
start_dialogue3 = Room("", "A searing pain shoots through your head, most likely \
from a previous struggle. \n (press enter to continue)")
start_dialogue4 = Room("", "You can't remember where you are, but more importantly \
who you are.")
start_dialogue5 = Room ("", "Cold shackles and chains wrap around your ankles, trapping you in \
this cell. \n (press enter to continue)")
start_dialogue6 = Room ("", "You hear footsteps coming from behind the door left ajar \
at the far end of the \nroom. \n (press enter to continue)")
start_dialogue7 = Room ("", "Frantically, your eyes dart around the room.  \
You need to unlock your shackles.\
")
start_dialogue8 = Room ("", "The key, old and rusted, breaks in the lock, \
but you still manage to undo your \nshackles.\n\
You slip them off of you just as the door creaks open, and a guard enters. \n\
You square up, and prepare for battle. \n\
(Press enter to continue)")
battle1 = Room ("CELL", "The guard left the door open behind him.")
post_battle1 = Room ("CELL", "The guard left the door open behind him.  You can leave the cell.")
need_to_hide = Room ("PASSGEWAY", "You leave the cell.  Tiptoeing down the passageway, \
you hear a thunder of footfalls in the distance, \n\
most likely a guard patrol coming to check on the one you defeated.  \n\
You need to hide.  You see a broom closet to your RIGHT. \n\
You might also be able to find better shelter further down the passageway.\n\
What do you do?")
guards_find_you = Room ("GAME OVER", "\nGuards thunder around the corner.  Nowhere to go, \n\
you put your hands in the air to surrender, they escort you back to your cell.  \n\
Maybe someday you'll have another chance to try and escape.")
dining_hall = Room ("ENTRANCE TO DINING HALL", "At the end of the passageway, \n\
you realize that the footfalls were just from the guards rushing into the \n\
dining hall for lunch.  You sigh, as you realize that for now, your escape \n\
has gone unnoticed. \n\
There are doors to your RIGHT and LEFT. \n\
The entrance to the dining hall is in front of you, \n\
but there are a several locks on it. \n\
You can also go BACKWARDS to the passageway.")
broom_closet = Room ("BROOM CLOSET", "You slip into a broom closet.\n\
You're starting to feel sick from the horrible smell of cleaning supplies. \n\
The coast is probably clear now.  What do you do?")
art_room = Room ("ART ROOM", "Ah, art.  It's always nice when you're \n\
on a prison break to take a second to enjoy the finer things in life.  \n\
This room is carpeted with red velvet, and the moulding is laced with gold.  \n\
Whoever owns this castle must be quite wealthy.  \n \
There are a couple of things that catch your eye: a fragile looking vase, \n\
a sword, and a portrait of a young man, who must be the king of this castle.  \n\
You can EXIT through a door in the back.")
armory = Room ("ARMORY", "To your dismay, there are no weapons left here that might \n\
aid you in your escape.  You can LEAVE the same way you came.")
safe_passageway = Room ("PASSAGEWAY", "This passageway looks safe now.  \n\
You can continue FORWARD from here,head BACK into your cell, \n\
or enter the broom closet on your RIGHT.")
inside_dining_hall = Room ("DINING HALL", "With the door now unlocked, you enter the dining hall.  \n\
Your mouth waters as the smell of food wafts towards you. \n\
From here, the kitchen is to your RIGHT.")
new_cell = Room ("CELL", "The guard left the door open behind him.  You can LEAVE the cell.")
pre_kitchen_battle = Room ("KITCHEN", "Ravenous, you run into the kitchen, ready to cook yourself a feast. \n\
You make yourself a glorious sandwich, with grilled chicken, bacon, \n\
barbeque sauce, and carmelized onions.\n\
You jump when you hear someone behind you yell \n\
\"What are you doing in my kitchen!\"  \n\
You must have been too loud when you were cooking. \n\
You turn around, and see someone short and stout.  He must be the chef.  \n\
Furious that you would invade his kitchen, he moves in to attack. \n(Press enter to continue)")
kitchen_battle = Room ("KITCHEN", "The chef staggers and falls.  The kitchen is yours. \n\
(Press enter to continue, or any other key to play the fight again)")
meet_king1 = Room ("KITCHEN", "You hear someone slow-clapping behind you.  \n\
A somewhat tall, sunburned young man enters the room with a smile on his face. \n\
This must be the king.")
meet_king2 = Room ("KITCHEN", "\"Well,\" he goes on, \"It appears that I am short a cook, \n\
and I am quite hungry \n\
So, here is my proposal: You can be my cook, or you can go back to your cell.  \n\
Choose wisely.")
be_cook = Room("KITCHEN", "The king smiles his approval.  \"Good choice,\" he says as he walks out of the kitchen. \n\
\"And there better be a sandwich here when I get back,\" \n\
he calls back from the dining hall. \n\
(Press enter to continue)")
kitchen_search1 = Room("KITCHEN", "\"All right,\" you think to yourself.  \"Time to make a sandwich.  \n\
All I have to do is find the ingredients.  I'm going to look around.\" \n \n \
In the kitchen, there's a cupboard, a fridge, and a pantry.  \
There\'s a cutting board with two slices of bread on it, primed for sandwich-making.\n\
There's also an open trap-door leading DOWN. \
There is a room to your LEFT, but the door leading to it is locked. \n\
")
kitchen_search2 = Room("KITCHEN", """
You've got your lettuce.  All you need now is a sweet, juicy tomato.

In the kitchen, there's a cupboard, a fridge, and a pantry.
There\'s a cutting board with two slices of bread on it, primed for sandwich-making.\n\
The trap-door locks behind you, barring you from going back DOWN. \n

The room to your LEFT that was locked last time you were here is now ajar.
""")
kitchen_search3 = Room("KITCHEN", """
Re-entering the kitchen, you hear a familiar slow clapping. \n\
The king, initially smiling, looks at the food in your hands.\n\
However, his face quickly falls.   \n\
\"You're making me a Spam, lettuce, and tomato sandwich, without mayonaise?\" he screams, enraged.
\"How can you possibly forget the mayo!  For this, you shall be punished. \n
Prepare to meet your doom . . .\"\n
(Press enter to continue)""")
pre_king_battle = Room ("KITCHEN", "\"I guess you are crazy enough.  Prepare to meet your doom.\n\
(Press enter to continue)")
king_battle = Room ("", "The king has been dethroned.")
king_lose = Room ("GAME OVER", "The king's gaze hardens.  \n\"As you wish,\" he says through gritted teeth. \n\
He snaps his fingers, and guards pick you up from behind, carrying you back to your cell.  \n\n\
Why didn't you just take him up on his offer?")
#logan_game = Room ("HERES WHERE YOU CAN PUT YOUR GAME LOGAN", "description here")
#starting introduction paths
start_dialogue1.add_paths({"": start_dialogue2})
start_dialogue1.add_paths({"kitchen": kitchen_search1})
#start_dialogue1.add_paths({"asdf": dungeonC})
start_dialogue2.add_paths({"": start_dialogue3})
start_dialogue3.add_paths({"": start_dialogue4})
start_dialogue4.add_paths({"": start_dialogue5})
start_dialogue5.add_paths({"": start_dialogue6})
start_dialogue6.add_paths({"": start_dialogue7})
start_dialogue1.add_paths({"stay": start_dialogue1})
start_dialogue2.add_paths({"stay": start_dialogue2})
start_dialogue3.add_paths({"stay": start_dialogue3})
start_dialogue4.add_paths({"stay": start_dialogue4})
start_dialogue5.add_paths({"stay": start_dialogue5})
start_dialogue6.add_paths({"stay": start_dialogue6})
start_dialogue7.add_paths({"stay": start_dialogue7})
start_dialogue8.add_paths({"stay": start_dialogue8})
start_dialogue8.add_paths({"": battle1})
start_dialogue8.add_paths({"key": start_dialogue8})

battle1.add_paths({"": post_battle1})
battle1.add_paths({"stay": battle1})

post_battle1.add_paths({"go": need_to_hide})
post_battle1.add_paths({"enter": need_to_hide})
post_battle1.add_paths({"through": need_to_hide})
post_battle1.add_paths({"leave": need_to_hide})
post_battle1.add_paths({"exit": need_to_hide})
post_battle1.add_paths({"stay": post_battle1})

need_to_hide.add_paths({"closet": broom_closet})
need_to_hide.add_paths({"passageway": guards_find_you})
need_to_hide.add_paths({"stay": guards_find_you})
need_to_hide.add_paths({"further": guards_find_you})
need_to_hide.add_paths({"right": broom_closet})

dining_hall.add_paths({"left": armory})
dining_hall.add_paths({"right": art_room})
dining_hall.add_paths({"stay": dining_hall})
dining_hall.add_paths({"backwards": safe_passageway})

broom_closet.add_paths({"leave": safe_passageway})
broom_closet.add_paths({"exit": safe_passageway})
broom_closet.add_paths({"stay": broom_closet})

safe_passageway.add_paths({"right": broom_closet})
safe_passageway.add_paths({"forward": dining_hall})
safe_passageway.add_paths({"stay": safe_passageway})
safe_passageway.add_paths({"cell": new_cell})
safe_passageway.add_paths({"back": new_cell})
safe_passageway.add_paths({"enter": broom_closet})
safe_passageway.add_paths({"right": broom_closet})

new_cell.add_paths({"stay": new_cell})
new_cell.add_paths({"go": safe_passageway})
new_cell.add_paths({"enter": safe_passageway})
new_cell.add_paths({"through": safe_passageway})
new_cell.add_paths({"leave": safe_passageway})
new_cell.add_paths({"exit": safe_passageway})


art_room.add_paths({"exit": dining_hall})
art_room.add_paths({"leave": dining_hall})
art_room.add_paths({"stay": art_room})

armory.add_paths({"exit": dining_hall})
armory.add_paths({"leave": dining_hall})
armory.add_paths({"stay": armory})

inside_dining_hall.add_paths({"exit": dining_hall})
inside_dining_hall.add_paths({"leave": dining_hall})
inside_dining_hall.add_paths({"back": dining_hall})
inside_dining_hall.add_paths({"stay": dining_hall})

pre_kitchen_battle.add_paths({"": kitchen_battle})
pre_kitchen_battle.add_paths({"stay": pre_kitchen_battle})

kitchen_battle.add_paths({"": meet_king1})
kitchen_battle.add_paths({"stay": kitchen_battle})

meet_king1.add_paths({"": meet_king2})
meet_king1.add_paths({"stay": meet_king1})

meet_king2.add_paths({"cook": be_cook})
meet_king2.add_paths({"cell": king_lose})
meet_king2.add_paths({"stay": meet_king2})

be_cook.add_paths({"": kitchen_search1})
be_cook.add_paths({"stay": be_cook})

start_dialogue1.add_paths({'qwertyuiop': kitchen_search1, 'asdfghjkl': strange, 'zxcvbnm': dirt_room})
kitchen_search1.add_paths({"down": strange})
kitchen_search1.add_paths({"trap-door": strange})
kitchen_search1.add_paths({"stay": kitchen_search1})



kitchen_search2.add_paths({"down": strange})
kitchen_search2.add_paths({"trap": strange})
kitchen_search2.add_paths({"stay": kitchen_search2})
kitchen_search2.add_paths({"down": strange})
kitchen_search2.add_paths({"left": hell})
kitchen_search2.add_paths({"warm": hell})
kitchen_search2.add_paths({"room": hell})

kitchen_search3.add_paths({"": king_battle})
kitchen_search3.add_paths({"stay": kitchen_search3})

pre_king_battle.add_paths({"": king_battle})
pre_king_battle.add_paths({"stay": pre_king_battle})

start_dialogue7.add_item_path({"key": {"unlock": start_dialogue8, "open": start_dialogue8,
"use": start_dialogue8}})

dining_hall.add_item_path({"key-ring": {"unlock": inside_dining_hall, "open": inside_dining_hall,
"enter": inside_dining_hall, "use": inside_dining_hall}})

start_dialogue5.add_paths({"king": meet_king1})


start_dialogue7.add_items({"key": "It looks like it goes with the shackles in the cell"})
post_battle1.add_items({"rucksack": """
    With this rucksack, you can now carry multiple items around with you in the \
    dungeon.
    To see what items you have taken, type \"inventory\"
    You can also drop items by saying \"drop\" \
"""})
broom_closet.add_props({"pail": "Upon closer inspection, at the bottom of the pail, you see a key-ring with a dozen \
different keys on it.  You think to yourself, \"Huh, maybe I should look at things in rooms \
more often\""})
broom_closet.add_props({"water": "Upon closer inspection, at the bottom of the pail, you see a key-ring with a dozen \
different keys on it.  You think to yourself, \"Huh, maybe I should look at things in rooms \
more often.\""})
broom_closet.add_items({"key-ring": "Maybe one of these keys opens a door to somewhere important"})
armory.add_items({"paper": "The contents of the paper appear to be gibberish and are as follows \n\
\tMonday - pumpernickel\n\
\tTuesday - banana\n\
\tWednesday - dog\n\
\tThursday - aglet\n\
\tFriday - cumulonimbus\n\
\tSaturday - syzygy\n\
\tSunday - quixotic" })
dining_hall.add_props({"locks": "You should see if you can find a key-ring that might be able to unlock them."})
dining_hall.add_props({"door": "You should see if you can find a key-ring that might be able to unlock it."})
dining_hall.add_props({"entrance": "You should see if you can find a key-ring that might be able to unlock it."})

art_room.add_props({"portrait": "This king appears to have a very red face.  I wonder if he gets sunburned easily."})
art_room.add_items({"vase": "This piece of pottery feels lighter and more fragile than egg shells. It is probably very expensive."})
art_room.add_items({"sword": "Encrusted with diamonds, it's probably intended more for decoration than for practical use. \
Who knows when you might need it."})
dining_hall.add_items({"key-ring": "Maybe one of these keys opens a door to somewhere important"})
new_cell.add_items({"rucksack": "With this rucksack, you can now carry multiple items around with you in the \
dungeon.  \n\tTo see what items you have taken, type \"inventory\"  You can also drop items by saying \"drop\" \
."})
kitchen_search1.add_props({"fridge": "Nothing here except a surprising amount of \"I can't believe it\'s not butter.\""})
kitchen_search1.add_props({"refrigerator": "Nothing here except a surprising amount of \"I can't believe it\'s not butter.\""})
kitchen_search1.add_props({"pantry": "Oooh, there's sweet delicious Spam.  Nothing much you could put on a sandwich though."})
kitchen_search1.add_props({"cupboard": "There's just a bunch of Pam here.  Nothing else, just Pam.  What do the people here eat?"})
kitchen_search1.add_items({"Pam": "You never know when you might need a stick-free cooking surface"})
kitchen_search1.add_items({"Spam": "A classic.  Goes well with anything"})
kitchen_search1.add_items({"\"I can't believe it\'s not butter\"": "After trying it, you CAN believe it\'s not butter."})
kitchen_search1.add_props({"trap-door": "Maybe it leads somewhere with sandwich-making materials."})

kitchen_search2.add_props({"fridge": "Nothing here except a surprising amount of \"I can't believe it\'s not butter.\""})
kitchen_search2.add_items({"refrigerator": "Nothing here except a surprising amount of \"I can't believe it\'s not butter.\""})
kitchen_search2.add_items({"Spam": "A classic.  Goes well with anything"})
kitchen_search2.add_props({"cupboard": "What? Where'd the Pam go?"})
kitchen_search2.add_props({"trap-door": "Maybe it leads somewhere with sandwich-making materials."})

#ronil's rooms and stuff:
if True:
    hell.add_props({'stair': "a spiriling staircase that leads down somewhere", 'around': hell.description, 'river': "floating on the surface of the lava, there is a coin"})
    hell.add_items({'coin': "a golden coin that could be useful to pay someone off"})
    lava = Room("LAVA", "as you walk down the staircase you notice the river of lava flows next to you \nyou enter a room completely covered in lava \n\non the far side you notice a small opening but you have no way to cross the lava")

    lavaB = Room("LAVA", "you turn around and notice there is a boat resting on lava with a strange man sitting on it \nhe beckons you")
    hell.add_paths({'down': lava, 'stay': hell})
    lava.add_props({'around': lavaB.description})
    boat = Room("BOAT", "hello, my name is Charon, I ferry the dead, you are not dead pls go away")
    boatB = Room("BOAT", "ah I see, bribery, very nice, I shall take you to the other side\n\n(press enter)")
    lava.add_paths({'boat': boat, 'man': boat, 'up': hell, 'stay': lava})
    boat.add_item_path({'coin': {'bribe': boatB}})
    boat.add_paths({'stay': boat, 'leave': lava})
    dungeon = Room("DUNGEON", "hi you have reached the dungeon \nin the far corner you see a chest")
    dungeonA = Room("DUNGEON", "the only way to get to the chest is if you win the boss fight!! \n\n(press enter)")
    dungeonB = Room("DUNGEON",'dungeon')
    dungeonC = Room("DUNGEON", "ahhh Charon back here, pls leave hell, you are not dead \nI have no idea how you won \npls leave me alone \n\nUSE this PORTAL and leave me alone")
    dungeonA.add_paths({'': dungeonB,'stay': dungeonB})
    boatB.add_paths({'': dungeon, 'stay': dungeon})
    dungeon.add_paths({'chest': dungeonA})


#logans roooms and stuff:

#strange = Room('STRANGE ROOM', 'you are in a small stone room, \nit appears normal but you feel a ...strange... energy\n\na shriveled old human sleeps in the corner -\nsleep talking like an insane person')
old_man_scene = Room('The old person notices you and freaks out','\nthey stare at you, eyes widening until they begin to rip the skin\nthe old person lets out an ear piercing shriek, you cover your ears\nthe shrieking figure combusts, a strange pendant tumbles out from the rags \n\n(PRESS ENTER)\n')
strangeB = Room('STRANGE ROOM', 'you are in a small stone room, it appears normal but you feel a... strange... energy\n\na pile of rags lies in the corner \n there is a strange pendant at your feet')
take_pendant_scene = Room('as your fingers grasp the pendant, the strange object begins to glow',"""
you feel an energy run through your body
you experience the entire history of the universe and its
entire future all in a single moment
you feel yourself travelling, but your feet are not moving

with the pendant you have the power to travel \nto the FUTURE and the PAST, \nit is much easier to travel between rooms while in the present

(PRESS ENTER)

""")
strangeC = Room('STRANGE ROOM', 'you are in a small stone room\n\nin the corner a few threads of the rags remain... the rest have rotted away\n the EASTern wall has eroded away, crumbled rock lies on the ground beneath this new doorway')

door_room = Room('DOOR ROOM','3 doors lie on the northern wall, they are marked "alpha", "beta", and "gamma"\nthe dirt room lies to the south')
red_room = Room('RED ROOM','the room you are in is completely red\nred stone walls, a red carpet on the floor and a red glow in the air\n\nthe door room is back to the south')
red_roomB = Room('RED ROOM','the room you are in is completely red\nred stone walls, a red carpet shoved to the side, a red glow in the air\nand newly opened trap door... a staircase leads down\n\nthe door room is back to the south')
red_roomP = Room('RED ROOM PAST','the red walls are only partially painted and there seems to be a hole in \nthe center of the room that is partially dug,\nthe carpet and red feeling are not present')
blue_room = Room('BLUE ROOM','the room you are in is completely blue\nblue stone walls, a blue carpet on the floor and a blue glow in the air')
blue_roomP = Room('BLUE ROOM PAST','the blue walls are only partially painted \nthe carpet and blue feeling are not present')
green_room = Room('GREEN ROOM','the room you are in is completely green\ngreen stone walls, a green carpet on the floor and a green glow in the air')
green_roomP = Room('GREEN ROOM PAST','the green walls are only partially painted \nthe carpet and green feeling are not present')
boiler_room = Room('BOILER ROOM','pipes jut out from the ceiling, floor, and walls\nthere is a small tank in the corner, with just enough room underneath to hide \nsomething\n\nthe room is full of a hazy steam\n\nthere is a doorway to the north\n and a doorway to the east\n\non the western wall there is a long key rack with 13 hooks\nembedded in the southern wall is an incinerator\n')
trickster1 = Room("""
before you can do anything something knocks you to the floor

as you sit up you come face to face with a smiling gnome

he gleefully dances about, holding your pendant in his hand

(press enter)
""",'')
trickster2 = Room("""
the gnome nimbly prances past you as you try to grab him

he takes the 12 keys that were on the key rack and along with the pendant
throws them all in the incinerator

as he shuts the door the incinerator locks and a ten second countdown begins

you scream as he dances away saying "it's just a prank bro"

(press enter)
""",'')

trickster3 = Room("""
you need to get the incinerator key, but you can't time travel right now...
(press enter)
""",'')
oh_no = Room('BOILER ROOM', 'pipes jut out from the ceiling, floor, and walls\nthere is a small tank in the corner, with just enough room underneath to hide something\n\nthe room is full of a hazy steam\n\non the western wall there is a long key rack with 13 hooks\nembedded in the southern wall is an incinerator.\nyou need to unlock it or your \npendant will be destroyed')
unlock_room = Room('you unlock the incinerator and grab the pendant just as the flames turn on... \nthe i-key is permanently stuck in the door.. you jammed it in too frantically\n\nit was very LUCKY that the incinerator key was put under the tank by someone\nthat way the gnome couldn\'t take it \n\n(PRESS ENTER)\n','')
boiler_roomP = Room('BOILER ROOM PAST','pipes jut out from the ceiling, floor, and walls\nthere is a small tank in the corner, with just enough room underneath to hide something\n\nthe room is full of a hazy steam\n\nthere is a doorway to the north\n and a doorway to the east\n\non the western wall there is a long key rack with 13 hooks and 13 keys\nimbedded in the southern wall is an incinerator\n')
forest = Room('FOREST','you are in the woods\nyou see an acorn on the ground\n\nthe boiler room is to the west')
bunker = Room('BUNKER','you are in a large bunker\n\nthere is a LONGBOW perched against the wall\na staircase leads back up\nthere is a porthole')
bunkerP = Room('BUNKER PAST','you are in a large bunker\n\nthere is a porthole')
look_hole = Room('you look through the porthole','you see the forest, and the gnome lying dead on the floor \n\n(press enter)')
look_holeP = Room('you look through the porthole', 'you see the forest, and the gnome perched on top of yourself, strangling you to death')
shoot1 = Room("""
you let an arrow loose and it hits the gnome, killing him and saving yourself

way to wrap up that loop...
\n\n(press enter)
""",'')
attack1 = Room("""
before you can do anything you get knocked to the floor

the gnome punches you repeatedly
his hands grasp around your throat
he screams "it's just a prank bro"

(press enter)
""",'')
attack2 = Room("""
you can feel your life force fading

all of a sudden an arrow shoots through the air and kills the gnome

how LUCKY...

you get up, take the arrow, and spit on the bothersome fellow

(press enter)
""",'')
dirt_roomB = Room('DIRT ROOM',"""
\nyou've sealed your fate . . . \n
the ground is covered in dirt, there is an acorn planted in it
on the eastern wall there is a sign that reads:
    "Logan's Lettuce Dungeon -
        ye who enter shall not leave until obtaining the lettuce
        or thou shalt be smited"

10 feet above the sign there is a doorway

""")
dirt_roomBF = Room('DIRT ROOM FUTURE',"""
the ground is covered in dirt, there is a huge tree grown in it
on the eastern wall there is a sign that reads:
    "Logan's Lettuce Dungeon -
        ye who enter shall not leave until obtaining the lettuce
        or thou shalt be smited"

10 feet above the sign, next to a fat branch, there is a doorway

""")
lettuce_room = Room('LETTUCE ROOM', 'the center of the room hosts the treasured lettuce\n\nthe reason for why you entered this dungeon\n\nbut its heavily booby-trapped\n\nyou see lasers and motion sensors and magic energy and all sorts of bombs, gas, and weapons that will \nsurely kill you if you try to grab the lettuce\n\nyou\'ll have to go back into the past to when I placed the lettuce there')
lettuce_roomP1 = Room('LETTUCE ROOM PAST', """
a man walks into the room holding the lettuce
he acts surprised to see you, but he knew you would be coming

you brace yourself, ready to fight Logan, the benefactor of this letuce dungeon

"stop narrarating everything" you say "its getting really annoying"

I chuckle as I continue to narrate... "don't you recognize my voice?"
"I've been helping you this whole time"

(press enter)
""")
lettuce_roomP2 = Room("""
"then hand over the lettuce" you growl

"a a a ... not so fast" I inform you
"we have to make sure you've tied up all of your loose ends..."
"time travel is a messy thing after all" I cackle


"wha what do you mean?" you ask

"there's no luck in my dungeon... its all you, its all you"

(press enter)
""",'')

lettuce_roomP3 = Room("""
"now let's see... did you put the key under the tank for yourself to find?"
""",'')

lettuce_roomP4 = Room("""
"now let's see... did you kill the gnome and save yourself?"
""",'')

lettuce_roomP5 = Room('','')
lettuce_roomB = Room('LETTUCE ROOM','there is a doorway to the north leading out of the dungeon')
passageway = Room('PASSAGEWAY', 'the passageway runs east to west\nthe western door is labeled "employees only"')
museum = Room('MUSEUM', 'you are in a museum room\nthere is a sign that reads:\n"in this very room, 100 years ago, the great "percent s" \nplaced his time pendant in the light of the aligning planets\n and reached god status"')
museumP = Room('uh -oh, you travelled too far back, and your pendant isn\'t glowing anymore, \nyou\'ll have to wait here for a little while, \nbut what is a few years compared to an enternity of god-like power \n\n(press enter)','')
meet_self1 = Room('over the years you dig yourself a nice hole in the corner of the room\n to put your lettuce in\n\nyou are getting closer and closer to the day of your ascension,\n or so your dreams tell you\n\nsuddenly you are woken up by some rude dude \n\n(press enter)','')
meet_self2 = Room("""
wait a second.. thats no ordinary dude... thats you!
suddenly Logan appears behind yourself and says to you:
"sorry player, I don't like lying to people and getting their hopes
up about reaching god status, but I had to wrap up this last time loop...
no hard feelings?"

you shriek as he dissapears... was he ever there? have you gone insane?
is there any such thing as free will? who gave the first you the pendant?

these questions overload your puny mortal mind and you combust

(press enter)
""",'')
meet_self3 = Room("""
'or that's what would have happened if you had taken the pendant'
you think to yourself as you crush the pendant beneath your feet
it shatters into a million pieces

on a hunch you walk over to the corner... yup there it is.. the lettuce that
your past-future self didn't put there?... dont think about it

you take the lettuce and leave the room vowing to not come back
because you know the game will break if you do

out of the corner of your eye you almost catch a glimpse of Logan waving goodbye

(press enter)
""",'')

no_travel = Room('the energy in this room seems to stop you from travelling right now...\n\n(PRESS ENTER)','')

strange.add_paths({"old": old_man_scene, "human": old_man_scene, "man": old_man_scene, "wake": old_man_scene, "sleeping": old_man_scene,"stay": strange})
old_man_scene.add_paths({'': strangeB, 'stay': old_man_scene})
strangeB.add_paths({'x67e5': take_pendant_scene, 'stay': strangeB})
take_pendant_scene.add_paths({'': strangeC, 'stay': take_pendant_scene})
strangeC.add_paths({'east': dirt_room, 'stay': strangeC, 'past': no_travel, 'future': no_travel})
no_travel.add_paths({'stay': strangeC, '': strangeC})
dirt_room.add_paths({'north': door_room,'stay': dirt_room, 'south': boiler_room, 'past': dirt_roomP, 'future': dirt_roomF})
dirt_roomP.add_paths({'stay': dirt_roomP, 'future': dirt_room})
dirt_roomF.add_paths({'stay': dirt_roomF, 'past': dirt_room})
door_room.add_paths({'south': dirt_room, 'alpha': red_room, 'beta': red_room, 'gamma': red_room, 'stay': door_room})
red_room.add_paths({'south': door_room, 'stay': red_room, 'past': red_roomP, 'future': red_room, 'carpet': red_roomB})
red_roomP.add_paths({'future': red_room, 'past': red_roomP, 'stay': red_roomP, })
red_roomB.add_paths({'south': door_room, 'stay': red_roomB, 'past': red_roomP, 'future': red_roomB, 'down': bunker})
blue_room.add_paths({'south': door_room, 'stay': blue_room, 'past': blue_roomP, 'future': blue_room})
blue_roomP.add_paths({'future': blue_room, 'past': blue_roomP, 'stay': blue_roomP, })
green_room.add_paths({'south': door_room, 'stay': green_room, 'past': green_roomP, 'future': green_room})
green_roomP.add_paths({'future': green_room, 'past': green_roomP, 'stay': green_roomP, })
boiler_room.add_paths({'north': dirt_room, 'east': forest, 'stay': boiler_room, 'a789sy': trickster1, 'past': boiler_roomP, 'future': boiler_room})
trickster1.add_paths({'': trickster2, 'stay': trickster2})
trickster2.add_paths({'': trickster3, 'stay': trickster3})
trickster3.add_paths({'': oh_no, 'stay': oh_no})
oh_no.add_paths({'stay':oh_no})
unlock_room.add_paths({'': boiler_room, 'stay': boiler_room})
forest.add_paths({'08w': attack1, 'stay': forest, 'west': boiler_room})
attack1.add_paths({'':attack2,'stay':attack2})
attack2.add_paths({'':forest, 'stay':forest})
boiler_roomP.add_paths({'stay': boiler_roomP, 'future': boiler_room})
bunker.add_paths({'up': red_roomB, 'stay':bunker, 'past': bunkerP, 'future': bunker, 'wq76ef': look_hole})
bunkerP.add_paths({'stay':bunkerP, 'past': bunkerP, 'future': bunker, 'wq76ef': look_holeP})
look_holeP.add_paths({'stay': bunkerP, '': bunkerP, '9s8f7d': shoot1})
shoot1.add_paths({'stay': bunkerP})
look_hole.add_paths({'stay': bunker, '': bunker})
dirt_roomB.add_paths({'stay': dirt_roomB, 'future': dirt_roomBF})
dirt_roomBF.add_paths({'stay': dirt_roomBF, 'past': dirt_roomB, 'up': lettuce_room, 'climb': lettuce_room})
lettuce_room.add_paths({'past': lettuce_roomP1, 'stay': lettuce_room})
lettuce_roomP1.add_paths({'': lettuce_roomP2, 'stay': lettuce_roomP2})
lettuce_roomP2.add_paths({'': lettuce_roomP3, 'stay': lettuce_roomP3})
lettuce_roomP3.add_paths({'': lettuce_roomP4, 'stay': lettuce_roomP4})
lettuce_roomP4.add_paths({'': lettuce_roomP5, 'stay': lettuce_roomP5})
lettuce_roomP5.add_paths({'restart': dirt_room, 'yougfam': lettuce_roomB})
lettuce_roomB.add_paths({'north': passageway, 'stay': lettuce_roomB})
passageway.add_paths({'stay': passageway, 'west': museum, 'door': museum})
museum.add_paths({'stay': museum, 'past': museumP})
museumP.add_paths({'stay': meet_self1})
meet_self1.add_paths({'stay': meet_self2})
meet_self2.add_paths({'stay': meet_self3})
meet_self3.add_paths({'stay': kitchen_search2})


strangeB.add_items({'pendant': 'with the pendant you have the power to travel \nto the FUTURE and the PAST, \nit is much easier to travel between rooms while in the present'})
oh_no.add_items({'i-key': 'it unlocks the incinerator'})
boiler_roomP.add_items({'i-key': 'it unlocks the incinerator'})
bunker.add_items({'longbow': 'good for shootin thangs'})
forest.add_items({'acorn':'good for growin trees'})

oh_no.add_item_path({'i-key': {'unlock': unlock_room}})
dirt_room.add_item_path({'acorn': {'plant': dirt_roomB}})

strange.add_props({'old': 'they look like they\'ve been through a lot'})
strangeB.add_props({'rags': 'the rags are super stinky\nI would stay away from them if I were you'})
dirt_room.add_props({'sign':'the sign reads:\n\t"Logan\'s Lettuce Dungeon -\n\t\tye who enter shall not leave until obtaining the lettuce\n\t\tor thou shalt be smited', 'east': 'that doorway seems important but it is so high up...'})
oh_no.add_props({'tank': 'under the tank you see the i-key ... the key that opens the incinerator!','rack':'it looks like the missing key that the gnome \ndid not take was labeled i-key'})
boiler_roomP.add_props({'rack': 'the i-key is on the key rack', 'hooks': 'the i-key is on the key rack', 'keys': 'the i-key is on the key rack'})

red_room.add_props({'carpet': 'it is a red carpet...'})
dirt_roomBF.add_props({'tree': 'it\'s a nice sturdy tree'})



want_to_quit = Room('press enter to quit','press 1 to go back')
definite_quit = Room("\nCome again soon!\n", "")
start_screen = Room("THE SANDWICH KING","""
a game by Jack, Logan, and Ronil

    1. Start
    2. Quit
""")
start_screen.add_paths({'1': start_dialogue1, '2': want_to_quit, 'stay': start_screen})
want_to_quit.add_paths({'1': start_screen})
want_to_quit.add_paths({"": definite_quit})
want_to_quit.add_paths({"stay": want_to_quit})

#logan's special stuff
n = 0
a = 0
ikey_paradox = False
arrow_paradox = False
def special_destination(list_of_response, current_scene):
    global n
    global a
    global ikey_paradox
    global arrow_paradox

    if current_scene == dirt_roomB:
        if "acorn" in me.items:
            me.del_items('acorn')
    if current_scene == meet_self3:
        me.del_items('pendant')
        me.add_items({'lettuce': 'it will go great on a sandwich'})
    if current_scene == lettuce_roomP5:
        if ikey_paradox and arrow_paradox:
            print 'alright %s, looks like you are good to go' %me.name
            print """
            "and I know you were expecting a big boss battle and all,
            but I'm tired, wasn't this dungeon enough for you?

            anyways... here's the lettuce

            see ya! to leave the dungeon just go down that passageway"
            he gestures to the north
            """
            me.add_items({'lettuce':'it will go great on a sandwhich'})
            try:
                me.del_items('longbow')
            except:
                pass
            raw_input('(press enter)\n>')
            return 'yougfam'
        else:
            print "you still have some loose ends so this iteration of you will cease to exist in"
            time.sleep(2)
            print "3..."
            time.sleep(1)
            print "2..."
            time.sleep(1)
            n = 0
            a = 0
            ikey_paradox = False
            arrow_paradox = False

            if 'longbow' in me.items:
                me.del_items('longbow')
                bunker.add_items({'longbow': 'good for shootin thangs'})
            if 'arrow' in me.items:
                me.del_items('arrow')
            oh_no.add_items({'i-key': 'it unlocks the incinerator'})
            boiler_roomP.add_items({'i-key': 'it unlocks the incinerator'})
            forest.add_items({'acorn':'good for growin trees'})
            return 'restart'
    if current_scene == lettuce_roomP3:
        if ikey_paradox:
            print 'well according to my records it looks like you did'
        else:
            print 'well according to my records it looks like you did not'
        raw_input('(press enter)\n>')
        return ''

    if current_scene == lettuce_roomP4:

        if arrow_paradox:
            print 'well according to my records it looks like you did'
        else:
            print 'well according to my records it looks like you did not'
        raw_input('(press enter)\n>')
        return ''
    try:
        if current_scene == shoot1:
            me.del_items('arrow')
    except KeyError:
        print "Hmm, you don't have an arrow.  Try exploring some more to find one."

    if current_scene == look_holeP:
        if 'shoot' or 'kill' in list_of_response:
            if 'longbow' in me.items or 'arrow' in me.items:
                if 'longbow' in me.items or 'arrow' in me.items:
                    arrow_paradox = True
                    return '9s8f7d'

                else:
                    print 'you need a bow and arrow to shoot'
                    raw_input('(press enter)\n>')
                    return 'stay'
    if current_scene == bunker:
        if 'porthole' in list_of_response:
            for key in examine_list:
                for word in list_of_response:
                    if key == word:
                        return 'wq76ef'
    if current_scene == bunkerP:
        if 'porthole' in list_of_response:
            for key in examine_list:
                for word in list_of_response:
                    if key == word:
                        return 'wq76ef'
    if current_scene == attack2:
        me.add_items({'arrow':'good for shootin thangs'})
    if current_scene == boiler_roomP:
        if "i-key" in me.items:
            if 'i-key' in list_of_response:
                if 'tank' in list_of_response or 'under' in list_of_response or 'put' in list_of_response:
                    print "you put the i-key under the tank, where it will wait for you to find it in \nthe future"
                    raw_input('\n(PRESS ENTER) \n>')
                    me.del_items('i-key')
                    ikey_paradox = True
                    return 'stay'
    if current_scene == unlock_room:
        me.add_items({'pendant': 'with the pendant you have the power to travel \nto the FUTURE and the PAST, \nit is much easier to travel between rooms while in the present'})
        if 'i-key' in me.items:
            me.del_items('i-key')
    try:
        if current_scene == trickster1:
            me.del_items('pendant')
    except KeyError:
        print ""
    if current_scene == strangeB:
        if 'pendant' in list_of_response:
            for key in take_list:
                for word in list_of_response:
                    if key == word:
                        me.add_items({'pendant': 'with the pendant you have the power to travel \nto the FUTURE and the PAST, \nit is much easier to travel between rooms while in the present'})
                        return 'x67e5'
    if current_scene == dungeon:
        if "coin" in me.items:
            me.del_items('coin')

    #if current_scene == door_room:
    #    if 'alpha' in list_of_response or 'beta' in list_of_response or 'gamma' in list_of_response:
    #        bleh = True
    #        for key in examine_list:
    #            for word in list_of_response:
    #                if key == word:
    #                    bleh = False
    #        if bleh:
    #            rooms = ['qwit1','qwit2','qwit3']
    #            return random.choice(rooms)
    if current_scene == boiler_room:
        n += 1
    if current_scene == forest:
        a += 1
    if current_scene == boiler_room and n == 1:
        n == 3
        return 'a789sy'
    if current_scene == forest and a == 1:
        a == 3
        return '08w'
    return 'False'



me = Character('name')


def start():
    global current_scene
    # For play-testing. -NP
    # current_scene = kitchen_battle
    current_scene = start_screen
    while True:
        os.system('clear')
        print current_scene.name
        if current_scene == battle1:
            me.del_items("key")
        check_quit()
        print current_scene.description
        item_hint()
        user_lose()
        battle_check()
        make_hungry()
        hungry()
        wrong = guard_riddle()
        if current_scene == inside_dining_hall:
            if wrong != True:
                print "The guard shakes his head and asks you to leave; your answer is wrong. \n\
Maybe the passwords are written down somewhere."
        personalized_meet_king_text()
        if current_scene.description == start_dialogue4.description:
            user_name = raw_input('You rack your brains, wondering, \"What is my name?\"\n> ')
            me.name = user_name
            while user_name == "":
                print "(This is the part where you type your name)."
                user_name = raw_input ("> ")
                me.name = user_name

        while True:
            if current_scene.description == start_dialogue4.description:
                print "\"Ah yes,\" you think to yourself.  \"I\'m " + str(me.name) + ".\"" + "\n (press enter to continue)"
            current_scene.check_item_paths()
            user_response = raw_input("> ")
            user_response = user_response.lower()
            user_response = user_response.strip()
            global list_of_response
            list_of_response = user_response.split(" ")

            #'trying special_destination...' (important for logans to work)
            hold = current_scene
            sp_destination = special_destination(list_of_response, current_scene)
            if sp_destination != 'False':
                current_scene = current_scene.go(sp_destination)
                break
            else:
                # 'doing the normal thing'
                if interact(current_scene, user_response) == False:
                    destination = travel(current_scene)
                    current_scene = current_scene.go(destination)
                    break
                else:
                    print current_scene.name

def interact(current_scene, user_response):
    interact_list = user_response.split(" ")
    #looking
    for key in examine_list:
        if key == interact_list[0]:
            chosen_verb = key
            look(interact_list)

            return interact_list[0]
    #taking
    for key in take_list:
        if key == interact_list[0]:
            chosen_verb = key
            take(interact_list)

            return interact_list[0]
    #dropping
    for key in drop_list:
        if key == interact_list[0]:
            chosen_verb = key
            drop(interact_list)

            return interact_list[0]

    if 'inventory' in interact_list:
        if "at" in interact_list:
            for thing in me.items:
                print thing
                print me.items[thing]
        inventory_print()
        return True

    return False


def travel(current_scene):
    for key in current_scene.paths:
        for word in list_of_response:
            if key == word:
                destination = word
                return destination

    return "stay"

def look(interact_list):
    #items
    for key in interact_list:
        for word in current_scene.items:
            if key == word:
                print current_scene.items[word]
                return
    #props
    for key in interact_list:
        for word in current_scene.props:
            if key == word:
                print current_scene.props[word]
                return

    for key in interact_list:
        if key == "around":
            print current_scene.description
            #print "You also see the following"
            #for thing in current_scene.items:
                #print "\t" + thing
            return
    for word in current_scene.description.split(' '):
        for key in interact_list:
            if key == word:
                print "there is nothing to see here"
                return

    if len(interact_list) == 1:
        print "please specify what you want to look at"
        return
    print "quite a boring thing to look at, don't you think?"
        #possibly add random text function
    #print "I did what I was supposed to!"

def take(interact_list):
    if current_scene == post_battle1 or current_scene == start_dialogue7:
        for key in interact_list:
            for word in current_scene.items:
                if key == word:
                    print "you take the " + word
                    print current_scene.items[key]
                    me.add_items({word: current_scene.items[key]})
                    current_scene.del_items(word)
                    return

        for key in interact_list:
            if key in me.items:
                print "you already have that in your inventory"
                return
            for word in current_scene.props:
                if key == word:
                    print "you can't take that!"
                    return

        if len(interact_list) == 1:
            print "please specify what you want to take"
            return
        else:
            print "a valiant effort, but I don't think that you can take that"
    elif "rucksack" not in me.items:
        for key in interact_list:
            for word in current_scene.items:
                if word == 'rucksack':
                    print "you take the " + word
                    print current_scene.items[word]
                    me.add_items({word: current_scene.items[word]})
                    current_scene.del_items(word)
                    return
        for word in me.items:
            me.del_items(word)
            current_scene.add_items({word: word})
        print "Without your rucksack, you cannot carry items with you."
    else:
        #print 'taking item...'
        if len(me.items) < 5:
            for key in interact_list:
                #print key
                for word in current_scene.items:
                    #print word
                    if key == word:

                        print "you take the " + word
                        print current_scene.items[key]
                        me.add_items({word: current_scene.items[key]})
                        current_scene.del_items(word)
                        return

            for key in interact_list:
                if key in me.items:
                    print "you already have that in your inventory"
                    return
                for word in current_scene.props:
                    if key == word:
                        print "you can't take that!"
                        return

            if len(interact_list) == 1:
                print "please specify what you want to take"
                return
            else:
                print "a valiant effort, but I don't think that you can take that"
        else:
            print "Your back strains from the load you carry.  You can't take this item.\n\
            You should drop something if you want to take something in this room."
            return
def drop(interact_list):
    for key in interact_list:
        for item in me.items:
            if key == item:
                print "you drop the " + item
                me.del_items(item)
                current_scene.add_items({item: item})
                return


def inventory_print():
    print "INVENTORY:"
    for thing in me.items:
        print ""
        print "\t" + thing
        print "\t" + me.items[thing]
        print ""
    if len(me.items) < 1:
        print "\tnothing"






#Jack's special stuff
def battle_check():
    if current_scene == battle1 or current_scene == kitchen_battle or current_scene == king_battle or current_scene == dungeonB:
        monster_battle()

def winning():
    print "Congratulations you have won!"
    print "You unlock the chest.  Inside, you see a juicy, ripe tomato."
    dungeonB.add_items({'tomato': "A tomato which can be helpful in making your sandwich"})

    dungeonB.add_paths({'leave': dungeonC, 'around': dungeonC, '': dungeonC})
    dungeonC.add_paths({'portal': kitchen_search3, 'use': kitchen_search3})
    return
def win_dialogue():
    if current_scene == battle1:

        print "You emerge victorious. \n (Press enter to continue, or you can touch any other key to play again)\n"

    elif current_scene == kitchen_battle:

        print "The chef staggers and falls.  The kitchen is yours. \n\
        (Press enter to continue, or any other key to play again)"

    elif current_scene == king_battle:

        print "Soliders walk in as you put on the king's crown.  Seeing that you \
have defeated the despised king, they fall on their knees \
saying \"Long live " + me.name + "!\""
        print "Well, that's certainly one way to win the game."
        print "\n"
        print "YOU WIN!"
        quit()
    # I added the following. -NP
    elif current_scene == dungeonB:
        print "You have defeated the Monster! "
        print "(Press enter to continue, or any other key to play again)"
    # I added the following. -NP
    else:
        print "CASE MISSING IN WIN DIALOGUE. "

def monster_battle():
    enemy_name = "enemy"
    enemy_choices_list = ['charge']
    my_hp = 3
    enemy_hp = 5
    if current_scene == battle1:
        my_hp += 2
        enemy_hp -= 2
    if current_scene == kitchen_battle:
        my_hp += 1
        enemy_hp -= 1
    if current_scene == king_battle:
        my_hp -= 2
        enemy_hp += 5000
    if current_scene == dungeonB:
        my_hp += 6
        enemy_hp += 3
    my_ac = 0
    enemy_ac = 0
    my_power = 0
    enemy_power = 0
    os.system('clear')
    if current_scene == dungeonB:
        print "A large monster guards this chest and has challenged you to battle..."
    print "In combat, you have three options:\n\tblock\n\tcharge\n\tattack\n\theal\n\tpower\n"
    print "An attack will only work if you've charged it up first, also only if the other person wasn't blocking"
    print "If a player attacks while you are charging, your charge fails.\n"
    print "Over the course of the battle, you accumulate power.  Once your power meter reaches 5, \n\
you can either heal 2 health or deal 2 damage to your opponent.  Blocking is ineffective against a \'power\' attack."
    print "You have %d hitpoints and the %s has %d hitpoints." %(my_hp, enemy_name, enemy_hp)
    raw_input('\npress enter')
    rps()
    while my_hp > 0 and enemy_hp > 0:
        os.system('clear')
        print "Player HP: %d" %my_hp
        print "Player attack charges: %d" %my_ac
        print "Player power meter:  %d\n" %my_power
        print "Enemy HP: %d" %(enemy_hp)
        print "Enemy attack charges: %d" %(enemy_ac)
        print "Enemy power meter:  %d\n\n" %enemy_power
        if my_power < 5:
            print "What do you do? (block/charge/attack)"
        else:
            print "What do you do? (block/charge/attack/power/heal)"
        player_choice = raw_input("> ")
        player_choice = player_choice.strip()
        player_choice = player_choice.lower()
        if current_scene == king_battle:
            return
        if enemy_power == 5:
            enemy_choices_list = ['heal', 'power']
        elif enemy_ac > 0:
            enemy_choices_list = ['block','charge','attack','attack']
        elif my_ac > 0:
            enemy_choices_list = ['block','charge','block']
        else:
            enemy_choices_list = ['charge']
        enemy_choice = random.choice(enemy_choices_list)
        print "you %s" %player_choice
        #print enemy_ac
        print "the enemy %ss" %(enemy_choice)
        if enemy_choice == 'heal':
            enemy_hp += 1
            enemy_power = 0
        elif enemy_choice == 'power':
            enemy_power = 0
            my_hp -= 2
        if my_power == 5:
            if player_choice == 'heal':
                my_hp += 2
                my_power = 0
            elif player_choice == 'power':
                enemy_hp -=2
                my_power = 0
        elif my_power != 5:
            if player_choice == 'power' or player_choice == 'heal':
                print "Your power meter must be fully charged before you can power or heal!"
        if enemy_choice == 'attack' or player_choice == 'attack':
            if enemy_choice == 'attack':
                if player_choice == 'block':
                    print "You block the enemy's attack."
                    enemy_ac = enemy_ac - 1
                else:
                    print "The enemy's attack is successful."
                    my_hp = my_hp - 1
                    enemy_ac = enemy_ac - 1
            if player_choice == 'attack':
                if enemy_choice == 'block':
                    print "The enemy blocks your attack."
                    my_ac = my_ac - 1
                elif my_ac > 0:
                    print "Your attack is successful."
                    enemy_hp = enemy_hp - 1
                    my_ac = my_ac - 1
                else:
                    print "You need to charge before you attack!"
        elif player_choice == 'charge' or enemy_choice == 'charge':
            if player_choice == 'charge':
                print "Your charge is successful"
                my_ac += 1
            if enemy_choice == 'charge':
                print "The %s's charge is successful" %enemy_name
                enemy_ac += 1

        #print enemy_choices_list
        easy_win = raw_input('\npress enter')
        if current_scene == dungeonB and easy_win == "win":
            winning()
            break
        if easy_win == "win":
            win_dialogue()
            break
        if my_power < 5:
            my_power += 1
        if enemy_power < 5:
            enemy_power += 1
    if my_hp <= 0:
        print "You fall unconscious.  Guards carry you back to your cell. \n\
Perhaps some way you'll have another chance to escape."
        quit()
    elif easy_win == "win":
        print ""
    else:
        # win_dialogue()
        # I commented out the above and replaced with the following. -NP
        if current_scene == dungeonB:
            winning()
        else:
            win_dialogue()

def item_hint():
    if current_scene == post_battle1:
        if "rucksack" in current_scene.items:
            for key in current_scene.items:
                print "You also see a rucksack that the cell guard dropped when he fell."
    if current_scene == broom_closet:
        if "key-ring" in current_scene.items:
            print """
    There appears to be nothing in here except brooms and a pail of water,
    which has a strange metallic glint coming from the bottom."""
    if current_scene == start_dialogue7:
        if "key" in current_scene.items:
            print "You see a pewter key that appears to match the locks on your shackles resting on the wall \n\
just above your head.  What do you do?  \n(You can take specific objects by saying \"take,\" and look at them by saying \n\"look\".)"
    if current_scene == armory:
        if "paper" in current_scene.items:
            print "Someone appears to have dropped a slip of paper with notes scribbled on it."
    if current_scene == new_cell:
        if "rucksack" in current_scene.items:
            if "rucksack" not in me.items:
                print "You also see a rucksack that the cell guard dropped when he fell."
    if current_scene == kitchen_search2:
        if "Spam" in current_scene.items:
            if "Spam" not in me.items:
                print "You also see Spam laid out on the counter."
def user_lose():
    if current_scene == guards_find_you:
        quit()
    if current_scene == king_lose:
        quit()
def make_hungry():
    if current_scene == art_room or current_scene == armory:
        me.hungry = True
        return me.hungry
    if current_scene == inside_dining_hall:
        me.hungry = False
        return me.hungry
def hungry():
    if me.hungry == True:
        print "Your stomach rumbles.  Maybe there's food in the dining hall."
        return

def guard_riddle():
    if current_scene == inside_dining_hall:
        if me.riddle_yes == False:
            my_number = random.randint(0,6)
            dictionary_of_riddles = {"pumpernickel": "Monday", "banana": "Tuesday",
            "dog": "Wednesday", "aglet": "Thursday", "cumulonimbus": "Friday",
            "syzygy": "Saturday", "quixotic": "Sunday"}
            list_of_guard_riddles = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            print "However, a guard blocks your path."
            print "The guard looks at you and says: \"Today is " + list_of_guard_riddles[my_number] + ".  What is the password?\""
            user_response = raw_input("> ")
            user_response = user_response.lower()
            list_of_response = user_response.split()
            if "inventory" in list_of_response:
                inventory_print()
                print "You took too long to answer, so the guard asks you to leave.\n(Press enter to continue)"
                return True
            for key in dictionary_of_riddles:
                if key in user_response:
                    if dictionary_of_riddles[key] == list_of_guard_riddles[my_number]:
                        print "You answered correctly.  The guard looks stunned. \nYou can now go into the kitchen on your RIGHT.\n\
(Press any other key to return to the dining hall entrance.)"
                        inside_dining_hall.add_paths({"right": pre_kitchen_battle})
                        inside_dining_hall.add_paths({"enter": pre_kitchen_battle})
                        inside_dining_hall.add_paths({"kitchen": pre_kitchen_battle})

                        return True

def personalized_meet_king_text():
    if current_scene == meet_king1:
        print """
    "Well, well, well, if it isn't %s" he says in a dramatic voice.
    "That's right," he goes on with a wide grin, "I know your name...
    I know everyone's name in my kingdom."
    Gesturing to the chef, he remarks, "I see you've defeated my chef. Well done.
    I always make sure that my cooks are proficient in hand-to-hand combat."
    At this, you stare at him in puzzlement, and his face turns even redder.

    (Press enter to continue)""" %me.name
    if current_scene == king_battle:
        print "Soliders walk in as you put on the king's crown and fall on their knees \n\
cheering \"Long live " + me.name + "\"!"
        print "Well, that's certainly one way to win the game."
        print "\n"
        print "YOU WIN!"
        quit()


def rps():
    if current_scene == king_battle:
        print "\"Well,\" the king tells you, \"I'm not in the mood for another battle.\"  \n\
\"I challenge you to a rock-paper-scissors to the death.\""
        while True:
            print "1: rock"
            print "2: paper"
            print "3: scissors"
            player_choice = raw_input("> ")
            player_choice = player_choice.strip()
            player_choice = player_choice.lower()
            if player_choice == "1":
                print "The king chose paper."
                time.sleep(3)
                print "Good thing everyone knows rock destroys paper."
                time.sleep(3)
                print "Defeated, the king collapses."
                personalized_meet_king_text()
            if player_choice == "2":
                print "The king chose scissors."
                time.sleep(3)
                print "Good thing your paper gave the scissors a paper cut, ruining them."
                time.sleep(3)
                print "Defeated, the king collapses."
                personalized_meet_king_text()
            if player_choice == "3":
                print "The king chose rock."
                time.sleep(3)
                print "Good thing your scissors are made out of steel and you slice through the rock."
                time.sleep(3)
                print "Defeated, the king collapses."
                personalized_meet_king_text()

def check_quit():
    if current_scene.name == definite_quit.name:
        quit()
start()
