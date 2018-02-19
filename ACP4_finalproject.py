import os
import time
from sys import exit
import random
from turtle import *
from pyfiglet import Figlet

# I added this to speed up play testing. -NP
pause = 0.1 # second
# I replaced time.sleep( with time.sleep(pause * -NP

### Pia's code starts here

class Scene(object):
    def enter(self):
        pass

class Death(Scene):
    response = [
        "You died! Next time pay for your movies!",
        "Looks like the FBI caught up with you... Try harder next time?",
        "Too bad so sad!",
        "Looks like you died fast... Now you're furious",
        "Do you want to be cremated? or buried?",
        "Oh no! :("
        "We hope to see you again!",
        "Looks like your fate might make you furious..."
    ]

    def enter(self):
        print Death.response[random.randint(0, len(self.response)-1)]
        play_again = raw_input("Would you like to try again? Type 'yes' if so.")
        if play_again == "yes":
            return 'opening'
        else:
            exit(1)

class Opening(Scene):
    language_key = False
    dog_name = ""
    def enter(self):
        print "The year is 3003."
        time.sleep(pause * 2)
        print "You are running from the FBI because you pirated Fast and Furious 348."
        time.sleep(pause * 2)
        print "You take your neighbor's spaceship 'The Green Falcon'"
        print " "
        return 'driving skill'

class Driving_Skill(Scene):
    def enter(self):
        setup()
        title("Can You Get Through?")
        clear()

        setup(width=800,height=800,startx=400,starty=400)

        def writing():
            write("Can you get through?", True, align="center")

        def path():
            speed(0)
            goto(0,0)
            penup()
            backward(400)
            pendown()
            color("red")
            forward(10)
            left(90)
            forward(200)
            right(90)
            forward(25)
            right(90)
            forward(210)
            left(90)
            forward(25)
            right(90)
            forward(120)
            left(90)
            forward(25)
            left(90)
            forward(210)
            right(90)
            forward(30)
            left(90)
            forward(30)
            left(90)
            forward(30)
            right(90)
            forward(60)
            right(90)
            forward(200)
            right(90)
            forward(140)
            left(90)
            forward(500)
            penup()
            backward(783)
            right(90)
            forward(45)
            forward(60)
            pendown()
            left(90)
            forward(15)
            right(90)
            forward(120)
            left(90)
            forward(120)
            left(90)
            forward(200)
            right(90)
            forward(35)
            left(90)
            forward(50)
            right(90)
            forward(70)
            right(90)
            forward(120)
            left(90)
            forward(650)
            penup()
            backward(890)
            pendown()

        writing()
        path()
        time.sleep(pause * 2)

        print "You are the arrowhead, offscreen on the left."
        print " "
        time.sleep(pause * 2)
        print "In increments of 10, type in a certain distance for the turtle to either travel 'forward' or 'backward'"
        print " "
        time.sleep(pause * 2)
        print "If you deem it necessary that the turtle rotates, first signify the direction of rotation ('left' or 'right')"
        print "as well as the degree of rotation (HINT: it will always be 90 or 180 ;) )"
        print " "
        time.sleep(pause * 2)
        print "An example of input would be: 'forward 50' or 'left 90'"
        print " "
        time.sleep(pause * 2)
        print "While you can stray outside the path, in order to win, you must end in the final confines of the path on the right edge of the screen."
        print " "
        time.sleep(pause * 2)
        print "It is best to center yourself in the path at the end-- you have enough moves to do so."
        print " "


        for i in range (35):

            if xcor() >= 350 and (ycor() >= -50 and ycor() <= 50):
                print "Congrats!"
                print "You now are able to drive!"
                time.sleep(pause * 2)
                print "Unfortunately, in learning how to drive you don't look where you're going..."
                print "You drive your car right through a wormhole and end up in the Psi Theta 7 Solar System."
                print " "
                time.sleep(pause * 2)
                print "The FBI chase you through the wormhole, and now are especially angry!"
                print "Can you make friends with"
                time.sleep(pause * 2)
                f = Figlet(font='isometric1')
                print f.renderText('THE ALIENS?')
                print ""
                time.sleep(pause * 2)
                break
            else:
                move = raw_input("Which way do you go? ")
                move = move.split(' ')
                if 'forward' in move:
                    color("blue")
                    forward(int(move[1]))
                    if ycor() <= -200:
                        print "You cannot go there."
                        penup()
                        setposition(-390, 0)
                        pendown()
                    if ycor() >= 200:
                        print "you cannot go there."
                        penup()
                        setposition(-390, 0)
                        pendown()
                elif 'backward' in move:
                    backward(int(move[1]))
                    if ycor() <= -200:
                        print "You cannot go there."
                        penup()
                        setposition(-390, 0)
                        pendown()
                    if ycor() >= 200:
                        print "you cannot go there."
                        penup()
                        setposition(-390, 0)
                        pendown()
                elif 'left' in move:
                    left(int(move[1]))
                    if ycor() <= -200:
                        print "You cannot go there."
                        penup()
                        setposition(-390, 0)
                        pendown()
                    if ycor() >= 200:
                        print "you cannot go there."
                        penup()
                        setposition(-390, 0)
                        pendown()
                elif 'right' in move:
                    right(int(move[1]))
                    if ycor() <= -200:
                        print "You cannot go there."
                        penup()
                        setposition(-390, 0)
                        pendown()
                    if ycor() >= 200:
                        print "you cannot go there."
                        penup()
                        setposition(-390, 0)
                        pendown()
                else:
                    print "Sorry I don't recognize that."
                    move = raw_input("Which way do you go? ")
                    move = move.split(' ')
                    if 'forward' in move:
                        color("blue")
                        forward(int(move[1]))
                        if ycor() <= -200:
                            print "You cannot go there."
                            penup()
                            setposition(-390, 0)
                            pendown()
                        if ycor() >= 200:
                            print "you cannot go there."
                            penup()
                            setposition(-390, 0)
                            pendown()
                    elif 'backward' in move:
                        backward(int(move[1]))
                        if ycor() <= -200:
                            print "You cannot go there."
                            penup()
                            setposition(-390, 0)
                            pendown()
                        if ycor() >= 200:
                            print "you cannot go there."
                            penup()
                            setposition(-390, 0)
                            pendown()
                    elif 'left' in move:
                        left(int(move[1]))
                        if ycor() <= -200:
                            print "You cannot go there."
                            penup()
                            setposition(-390, 0)
                            pendown()
                        if ycor() >= 200:
                            print "you cannot go there."
                            penup()
                            setposition(-390, 0)
                            pendown()
                    elif 'right' in move:
                        right(int(move[1]))
                        if ycor() <= -200:
                            print "You cannot go there."
                            penup()
                            setposition(-390, 0)
                            pendown()
                        if ycor() >= 200:
                            print "you cannot go there."
                            penup()
                            setposition(-390, 0)
                            pendown()
                    else:
                        return 'death'

        return 'omega_argosa_1'

class Victory(Scene):
    def enter(self):
        f = Figlet(font='isometric1')
        print f.renderText('congrats!')
        print "You managed to evade the FBI!"
        print "They're busy now chasing your neighbor who pirated Fast and Furious 349..."
        print "welp"
        quit(1)

### Chris's code starts here



class Omega_Argosa_1(Scene):

    #start of planet

    def enter(self):
        os.system('clear')
        print """You land the Green Falcon in the lush jungle of Omega Argosa 1.
            You step out onto the soft ground.
            You couldn't land on the planet's landing pad near the city because the FBI would know.
            Also, planet customs sucks.
            """
        time.sleep(pause * .5)
        print "There is a man with 2 heads and 6 eyeballs, sitting in a tree a couple feet away."
        print "Do you want to go talk to him?"

        choice = raw_input("> ")

        if choice.lower() == "yes":
            print "You walk towards the man and say 'Hello'"
            if Opening.language_key == False:
                print Translation.dialogue[1]
            else:
                print Translation.dialogue['old_man']
            print "You did not understand anything that he just said."
            print "You walk back to the ship."
            print "You are surrounded by jungle on all sides of you, but you can see faint"
            print "paths in these directions: east, west, and south."
            print "You can get back in your ship and leave(lame), or you can explore (Type direction)."


            while True:
                choice = raw_input("> ")
                if "ship" in choice.lower():
                    print "Ok you're not adventurous at all."
                    return 'space'
                    break
                elif "west" in choice.lower():
                    print "You start the trek through the eerie jungle."
                    return 'city'
                    break
                elif "east" in choice.lower():
                    print "You start walking on the path through the treachorous jungle."
                    return 'egohn_jungle'
                    break
                elif "south" in choice.lower():
                    print "You wander down the path and into the jungle."
                    return 'blagsek'
                    break
                else:
                    print "Please enter something that makes sense"
                    continue
        else:
            print "Ok well he seemed pretty nice to me."

            print "\nYou are surrounded by jungle on all sides of you, but you can see faint"
            print "paths in each direction: east, west, and south."
            print "You can get back in your ship and leave(lame), or you can explore."


            while True:
                choice = raw_input("> ")
                if "ship" in choice.lower():
                    print "Ok you're not adventurous at all."
                    return 'space'
                    break
                elif "west" in choice.lower():
                    print "You start the trek through the eerie jungle."
                    return 'city'
                    break
                elif "east" in choice.lower():
                    print "You start walking on the path through the treachorous jungle."
                    return 'egohn_jungle'
                    break
                elif "south" in choice.lower():
                    print "You wander down the path and into the jungle."
                    return 'blagsek'
                    break
                else:
                    print "Please enter something that makes sense"
                    continue

class City(Scene):

    def enter(self):
        print "You keep walking and the sounds of the jungle fill your ears with"
        print "screeches and growls from mysterious animals."
        print "The trail fades and grows into metallic surface you've never felt before."
        print "There are green lines down the middle of this metallic track."
        print "Do you want to keep walking on the track or walk on the side"

        choice = raw_input("> ")

        if "keep walking" in choice:
            print "You see a hover car in the distance, but its coming toward you fast."
            print "Quick! Dive or duck?"

            dude = raw_input("> ")
            if dude.lower() == "dive":
                print "You dive out the way of the hover car, and you hear a honk"
                print "and the alien gives you a dirty look, along with a peace sign."
                print "I heard that means peace among worlds, but I could be wrong."
                print "That was a close call, but you keep walking on the track."

                if 1==1:
                    print "Another car comes along, this one slowing down."
                    print "The window rolls down and a sweet looking lady, well as sweet"
                    print "as you can look with two heads, looks at you and gestures for you to get in."
                    if Opening.language_key == True:
                        print Translation.dialogue[2]
                    else:
                        print Translation.dialogue['lady_in_car']

                    choice = raw_input("> ")

                    if "get in" in choice:
                        print "You step in the car and it lurches forward with speed you've never seen before."
                        print "In the distance, you see a magnificent city-scape."
                        print"""        __   __                     ___      _
                                       |  | |  |      /|           |   |   _/ \_
                                       |  | |  |  _  | |__         |   |_-/     \-_     _
                                     __|  | |  |_| | | |  |/\_     |   |  \     /  |___|
                                    |  |  | |  | | __| |  |   |_   |   |   |___|   |   |
                                    |  |  |^|  | ||  | |  |   | |__|   |   |   |   |   |
                                    |  |  |||  | ||  | |  |   | /\ |   |   |   |   |   |
                                    """
                        time.sleep(pause * .5)
                        print "The lady startles you by taking your wallet and kicking you out the door."
                        print "Well I guess she really was two-faced."
                        print "You were going so fast that you died on impact with the road."
                        return 'death'
                    else:
                        print "You keep walking down the metallic road as the old lady speeds off."
                        print "After walking for 5 minutes, you see another 'car' coming down the road."
                        print "This one is going much faster than the old lady and is bright red."
                        print "It slows to a stop next to you, and as the window rolls down, you see a man with a dope haircut and sunglasses."
                        if Opening.language_key == True:
                            print Translation.dialogue[3]
                        else:
                            print Translation.dialogue['man_in_car']
                        print "Do you want to get in?"

                        choice = raw_input("> ")

                        if "get in" in choice or "yes" in choice:
                                print "You step in the car and it lurches forward with speed you've never seen before."
                                print "In the distance, you see a magnificent city-scape."
                                print"""        __   __                     ___      _
                                               |  | |  |      /|           |   |   _/ \_
                                               |  | |  |  _  | |__         |   |_-/     \-_     _
                                             __|  | |  |_| | | |  |/\_     |   |  \     /  |___|
                                            |  |  | |  | | __| |  |   |_   |   |   |___|   |   |
                                            |  |  |^|  | ||  | |  |   | |__|   |   |   |   |   |
                                            |  |  |||  | ||  | |  |   | /\ |   |   |   |   |   |
                                            """
                                time.sleep(pause * .5)
                                print "You enter the city through a magnificent gate."
                                return 'city_1'
                        elif "no" in choice:
                             print "You are left in the dust as the car speeds off."
                             print "There is nothing around you and you slowly starve to death."
                             return 'death'

            elif dude == "duck":
                    print "The hover car goes right over your head."
                    print "And its engines incinerate you on the spot."
                    print "Nice job!"
                    return 'death'
            else:
                    print "You were too indicisive, too bad."
                    print "The hover car hits you and you die."
                    print "Nice job!"
                    return 'death'
        else:
            print "The path leads right off a cliff."
            print "You were too busy looking around."
            print "Sad."
            return 'death'
class City_1(Scene):


    def enter(self):
        print "The vast city makes you feel small and insignificant."
        print "You see hundreds of aliens roaming the streets."
        print "The guy drops you off on a bustling street."
        print "The FBI is still after you, and although this city has millions of people,"
        print "you stand out in the crowd of aliens."
        print "Their heat signature gun will pick you up in an instant compared to all these cold-blooded aliens."
        print "Keep exploring the city or try to get back to the spaceship?"

        choice = raw_input("> ")

        if "keep exploring" in choice.lower():
            print "Adventurous, I like it."
            print "There are so many aliens around you, it reminds you of New York City."
            print "There's a quiet alleyway down a sidestreet."
            if Opening.language_key == True:
                print "It is labeled: 'Totally not a sketchy alleyway, we welcome you to walk down it.'"
            else:
                print "It is labeled: 'Gegsek geg sek gehsubeksubek sekgehphleg, subek subekgeg phleg geg sek kek agh.'"
            print "Wanna go down the alleyway?"

            choice = raw_input("> ")

            if "yes" in choice.lower():
                print "You walk down the quiet, scenic alleyway and enjoy the calmness."
                print "Yet you sense that something is not right."
                print "So you decide to go back to the street."
                print "Something is stopping you."
                print "A force field keeps you in place."
                print "You feel paralyzed."
                time.sleep(pause * 1)
                print "You wait for what seems like an eternity for someone to show up and help."
                print "You yell 'help me! I'm stuck!', but all you hear is an evil laugh."
                print "Looks like the FBI has finally caught up with you."
                print "The FBI agent says 'Scum like you don't deserve to live'"
                print "Her partner, a mean looking dude with ugly sideburns says 'You are the runt of the litter.'"
                print "'You pirated Fast and Furious 300 and you didn't even use a VPN'"
                print "'You thought you could get away'"
                print "The agents control the force field and make it slowly squeeze around you."
                print "You scream out, but no one can hear your cry."
                print "'I hope this hurts,' the agent says."
                print "He whips out his plasma gun and shoots me in the knee."
                print "Then, he says 'You're finished, no more free movies for you."
                time.sleep(pause * 5)

                print "And the world goes black..."
                return 'death'
            else:
                print "OK you can stay on the street."
                print "You see two agents coming toward you."
                print "Go back to your spaceship or try to fight them?"

                choice = raw_input("> ")

                if "fight" in choice:
                    print "They whip out their plasma guns and shoot at you"
                    # Mispelling below.  Argh!  -NP
                    # if Maze.aleinDog == True:
                    if Maze.alienDog == True:
                        print "%r starts attacking them, and kills them both." % Opening.dog_name
                        print "You quickly hail a taxi and point back to your spaceship."
                        time.sleep(pause * 5)
                        print "The drive is short because of these super fast cars."
                        print "Soon, you are surrounded by jungle on all sides of you, but you can see faint"
                        print "paths in each direction: west and south."
                        print "You can get back in your ship and leave, or you can keep exploring Omega Argosa 1."


                        while True:
                            choice = raw_input("> ")
                            if "ship" in choice.lower():
                                print "Ok you're not too adventurous."
                                return 'space'
                                break
                            elif "east" in choice.lower():
                                print "You start the trek through the eerie jungle."
                                return 'egohn_jungle'
                                break
                            elif "south" in choice.lower():
                                print "You wander down the path and into the jungle."
                                return 'blagsek'
                                break
                            else:
                                print "Please enter something that makes sense"
                                continue
                    else:
                        print "They shoot you right in the head and you die."
                        print "Nice job!"
                        return 'death'
                else:
                    print "You start running as fast as you can."
                    print "You can see they are coming after you, but they have jetpacks!"
                    print "Oh man, they are a step behind you."
                    print "There's a alien kid on a hoverboard, do you wanna take it?"


                    choice = raw_input("> ")

                    if choice == "yes":
                        print "Desperate times call for desperate measures."
                        print "Wow, you're flying on this hoverboard, woahhhh"
                        print "It's like that really, really old classic, Back to the Future."
                        print "Ha they were so primitive back then."
                        print "You ride over all the people on the street."
                        print "The FBI is flying right next to you."
                        print "What do you do?"

                        while True:

                            choice = raw_input("> ")

                            if "punch" in choice:
                                print "You try to punch the agents while staying on the hoverboard."
                                print "Ambitious."
                                print "You forgot that they are trained killers."
                                print "They whip out their plasma guns and shoot you."
                                print "You die."
                                print "Nice job!"
                                return 'death'
                                break
                            elif "keep" in choice:
                                print "You try to escape the agents."
                                print "Their jetpacks are too fast."
                                print "They shove you off the hoverboard, and you fall down and die."
                                print "Nice job!"
                                return 'death'
                                break
                            elif "jump" in choice:
                                print "You leap off the overboard, and the FBI agents are surprised."
                                print "They aren't looking and then they run into the building."
                                print "There is a large explosion!"
                                print "But you come out unscathed."
                                print "You take the hoverboard and ride it out of the city towards your spaceship."

                                print "\nYou are surrounded by jungle on all sides of you again, but you can see faint"
                                print "paths in each direction: east and south."
                                print "You can get back in your ship and leave, or you can keep exploring Omega Argosa 1."


                                while True:
                                    choice = raw_input("> ")
                                    if "ship" in choice.lower():
                                        print "Ok you're not too adventurous."
                                        return 'space'
                                        break
                                    elif "east" in choice.lower():
                                        print "You start the trek through the eerie jungle."
                                        return 'egohn_jungle'
                                        break
                                    elif "south" in choice.lower():
                                        print "You wander down the path and into the jungle."
                                        return 'blagsek'
                                        break
                                    else:
                                        print "Please enter something that makes sense"
                                        continue
                                break
                            else:
                                print "Please enter something that makes sense."
                                continue
                    else:
                        print "Well now the FBI catch up with you."
                        print "They shoot you."
                        print "The world goes black..."
                        return 'death'
class Egohn_jungle(Scene):

    def enter(self):
        print "The sounds of the jungle encompass you with fear."
        print "Screeches and cries from animals you've never heard fill your ears."
        print "But you are an adventurer so you keep going, unless you would like to go back to the spaceship"

        choice = raw_input("> ")

        if "go back" in choice.lower():
            print "Alright fine you can do that."
            print "You walk back to the spaceship"
            return 'space'
        else:
            print "Good choice. You trudge through the muddy grounds and keep walking for what seems like an hour."
            print "You are deep in the jungle now."
            print "You hear something like a dog's bark in the distance, but much deeper and with more growl."
            print "Do you walk toward it?"


            while True:
                choice = raw_input("> ")
                if "yes" in choice.lower():
                    print "You creep around the crunchy leaves and sticks of the jungle and walk toward the sound."
                    print "The bark grows louder."
                    return 'maze'
                    break
                elif "no" in choice.lower():
                    print "ok then back to the spaceship, we've got a sissy on our hands."
                    print "You walk back to the spaceship"
                    return 'space'
                    break
                else:
                    print "Please enter something normal."
                    continue

class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = _Getch()
#allows for me to get one character from input without enter
class Maze(Scene):

    a = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', ' ', ' ', ' ', 'a']
    b = ['8', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8']
    c = ['8', ' ', ' ', ' ', '8', ' ', ' ', ' ', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', ' ', ' ', ' ', '8', ' ', ' ', ' ', 'a', 'a', 'a', 'a', 'a', ' ', ' ', ' ', 'a', 'a', 'a', 'a', '8', 'a', 'a', 'a', 'a', ' ', ' ', ' ', 'a', 'a', 'a', 'a', '8', ' ', ' ', ' ', 'a', 'a', 'a', 'a', 'a', ' ', ' ', ' ', 'a', 'a', 'a', 'a', 'a', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8']
    d = ['8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8']
    e = ['8', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', ' ', ' ', ' ', 'a', ' ', ' ', ' ', '8', 'a', 'a', 'a', 'a', 'a', 'a', 'a', '8', ' ', ' ', ' ', '8', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', ' ', ' ', ' ', '8', 'a', 'a', 'a', 'a', ' ', ' ', ' ', 'a', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', 'a', 'a', 'a', 'a', 'a', 'a', 'a', '8', ' ', ' ', ' ', '8']
    f = ['8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8']
    g = ['8', ' ', ' ', ' ', 'a', ' ', ' ', ' ', '8', 'a', 'a', 'a', '8', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', ' ', ' ', ' ', 'a', ' ', ' ', ' ', '8', ' ', ' ', ' ', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', '8', ' ', ' ', ' ', '8', 'a', 'a', 'a', '8', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8']
    h = ['8', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8']
    i = ['8', ' ', ' ', ' ', '8', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', ' ', ' ', ' ', '8', 'a', 'a', 'a', '8', ' ', ' ', ' ', '8', 'a', 'a', 'a', 'a', ' ', ' ', ' ', '8', ' ', ' ', ' ', 'a', 'a', 'a', 'a', 'a', ' ', ' ', ' ', '8', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', ' ', ' ', ' ', '8', ' ', ' ', ' ', 'a', 'a', 'a', 'a', '8', ' ', ' ', ' ', '8']
    j = ['8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8']
    k = ['8', ' ', ' ', ' ', 'a', 'a', 'a', 'a', 'a', ' ', ' ', ' ', '8', 'a', 'a', 'a', 'a', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', 'a', 'a', 'a', 'a', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', 'a', 'a', 'a', 'a', 'a', 'a', 'a', '8', ' ', ' ', ' ', 'a', ' ', ' ', ' ', 'a', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', '8']
    l = ['8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8']
    m = ['8', 'a', 'a', 'a', 'a', 'a', 'a', 'a', '8', 'a', 'a', 'a', 'a', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', ' ', ' ', ' ', 'a', 'a', 'a', 'a', '8', 'a', 'a', 'a', 'a', ' ', ' ', ' ', '8', ' ', ' ', ' ', 'a', 'a', 'a', 'a', '8', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', 'a', 'a', 'a', 'a', ' ', ' ', ' ', '8', 'a', 'a', 'a', 'a', ' ', ' ', ' ', '8']
    n = ['8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8']
    o = ['8', ' ', ' ', ' ', 'a', 'a', 'a', 'a', 'a', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', ' ', ' ', ' ', '8', 'a', 'a', 'a', 'a', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', 'a', 'a', 'a', 'a', ' ', ' ', ' ', '8', 'a', 'a', 'a', '8', ' ', ' ', ' ', 'a', 'a', 'a', 'a', '8', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', ' ', ' ', ' ', '8']
    p = ['8', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8']
    q = ['8', ' ', ' ', ' ', '8', ' ', ' ', ' ', 'a', 'a', 'a', 'a', '8', 'a', 'a', 'a', 'a', ' ', ' ', ' ', 'a', ' ', ' ', ' ', '8', 'a', 'a', 'a', 'a', ' ', ' ', ' ', 'a', 'a', 'a', 'a', '8', 'a', 'a', 'a', 'a', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8']
    r = ['8', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8']
    s = ['8', ' ', ' ', ' ', '8', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', 'a', 'a', 'a', '8', ' ', ' ', ' ', '8', 'a', 'a', 'a', 'a', 'a', 'a', 'a', '8', ' ', ' ', ' ', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', 'a', 'a', 'a', 'a', 'a', 'a', 'a', '8']
    t = ['8', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8']
    u = ['8', ' ', ' ', ' ', '8', ' ', ' ', ' ', 'a', 'a', 'a', 'a', '8', ' ', ' ', ' ', '8', 'a', 'a', 'a', '8', ' ', ' ', ' ', 'a', 'a', 'a', 'a', 'a', ' ', ' ', ' ', '8', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', ' ', ' ', ' ', '8', 'a', 'a', 'a', '8', ' ', ' ', ' ', 'a', ' ', ' ', ' ', '8', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', ' ', ' ', ' ', 'a', ' ', ' ', ' ', '8']
    v = ['8', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', '8']
    w = ['8', ' ', ' ', ' ', '8', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', '8', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', '8', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', '8', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', '8', 'a', 'a', 'a', '8']

    x = "start"

    y = "X"
    alienDog = False
    rows = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v,w]
    first = -1
    second = 2
    score = 0
    rows[first][second] = y

    def enter(self):
        print "You have to make it through this maze to get to the dog."
        print "You can't run into the edge more than 5 times or else the creature comes at you and attacks."
        time.sleep(pause * 3)
        def Draw():
            os.system('clear')
            for i in Maze.rows:
                print ''.join(i)
        while True:
            try:
                if Maze.score == 6:
                    os.system('clear')
                    print "You lose!!!"
                    print "Nice job"
                    return 'afterdog'
                    break
                Draw()
                z = getch()
                if z == 'w':
                    Maze.rows[Maze.first][Maze.second] = ' '
                    if Maze.rows[Maze.first - 1][Maze.second] == 'a' or Maze.rows[Maze.first - 1][Maze.second] == '8':
                        print "You can't go that way"
                        Maze.score += 1
                        time.sleep(pause * 1)
                        Draw()
                        continue
                    Maze.first -= 1
                    Maze.rows[Maze.first][Maze.second] = Maze.y
                    Draw()
                    continue
                elif z == 'd':
                    Maze.rows[Maze.first][Maze.second] = ' '
                    if Maze.rows[Maze.first][Maze.second + 1] == 'a' or Maze.rows[Maze.first][Maze.second + 1] == '8':
                        print "You can't go that way"
                        Maze.score += 1
                        time.sleep(pause * .5)
                        Draw()
                        continue
                    Maze.second += 1
                    Maze.rows[Maze.first][Maze.second] = Maze.y
                    Draw()
                    continue
                elif z == 'a':
                    Maze.rows[Maze.first][Maze.second] = ' '
                    if Maze.rows[Maze.first][Maze.second - 1] == 'a' or Maze.rows[Maze.first][Maze.second - 1] == '8':
                        print "You can't go that way"
                        Maze.score += 1
                        time.sleep(pause * .5)
                        Draw()
                        continue
                    Maze.second -= 1
                    Maze.rows[Maze.first][Maze.second] = Maze.y
                    Draw()
                    continue
                elif z == 's':
                    Maze.rows[Maze.first][Maze.second] = ' '
                    if Maze.rows[Maze.first + 1][Maze.second] == 'a' or Maze.rows[Maze.first + 1][Maze.second] == '8':
                        print "You can't go that way"
                        Maze.score += 1
                        time.sleep(pause * .5)
                        Maze.rows[Maze.first][Maze.second] = Maze.y
                        Draw()
                        continue
                    Maze.first += 1
                    Maze.rows[Maze.first][Maze.second] = Maze.y
                    Draw()
                    continue
            except IndexError:
                print "You win!"
                Maze.alienDog = True
                print Maze.alienDog
                return 'afterdog'
                break

class AfterDog(Scene):

    def enter(self):
        print Maze.alienDog
        if Maze.alienDog == True:
            print "You find the dog at the end of the jungle, and it pledges its loyalty to you with a head nod. "
            print "Your dog is quite cute, with 3 eyes and large teeth."
            print "What do you want to name it?"

            Opening.dog_name = raw_input("> ")

            print "Aww that's a cute name, %r, I like it." % Opening.dog_name
            print "Your new dog can help you with later adventures!"
            print "You should probably go back to your spaceship before another creature shows up."
            print "So you walk back to your ship."

            print "\nYou are surrounded by jungle on all sides of you, but you can see faint"
            print "paths in each direction: west and south."
            print "You can get back in your ship and leave, or you can keep exploring Omega Argosa 1."


            while True:
                choice = raw_input("> ")
                if "ship" in choice.lower():
                    print "Ok you're not too adventurous."
                    return 'space'
                    break
                elif "west" in choice.lower():
                    print "You start the trek through the eerie jungle."
                    return 'city'
                    break
                elif "south" in choice.lower():
                    print "You wander down the path and into the jungle."
                    return 'blagsek'
                    break
                else:
                    print "Please enter something that makes sense"
                    continue

        elif Maze.alienDog == False:
            print "The alien dog comes after you."
            print "It's large teeth sink into your arm and you realize you messed up."
            print "It barks a vicious bark, and you see its friends coming toward you."
            print "You are going to die."
            print "No need to resist it."
            print "These alien dogs are much stronger and faster."
            return 'death'



class Blagsek(Scene):

    def enter(self):
        print "You keep walking through the jungle for a good hour."
        print "As you're walking, the dense jungle crowds around you."
        print "But, you see a pathway!"
        print "Do you follow the pathway?"

        choice = raw_input("> ")

        if "yes" in choice.lower():
            print "You walk down the path like a fearless adventurer!"
            print "Soon, you start to see houses in the giant green trees."
            if Opening.language_key == True:
                print "You see a sign labeled 'Welcome to Blagsek Village, Population: 300'"
            else:
                print "You see a sign labeled 'Subekgeg geg Buseksubek Aghseksubek, Gegbaksekaghbu: 300'"


            print "The beautiful treehouses are between 50ft and 200ft up in the trees, "
            print "with various ways to climb them."
            print "Which treehouse do you want to go into?"
            print "1 is a large wooden one, with amazing flowers all around it"
            print "2 is painted blue, and is designed like a sphere."

            choice = raw_input("> ")

            if choice == '1':
                return 'dope_treehouse'
            elif choice == '2':
                return 'blue_treehouse'
        if "no" in choice.lower():
            print "Ok you can walk back then."
            print "You start walking back."
            print "You are surrounded by jungle on all sides of you, but you can see faint"
            print "paths in each direction: west and east."
            print "You can get back in your ship and leave, or you can keep exploring Omega Argosa 1."

            while True:
                choice = raw_input("> ")
                if "ship" in choice.lower():
                    print "Ok you're not too adventurous."
                    return 'space'
                    break
                elif "west" in choice.lower():
                    print "You start the trek through the eerie jungle."
                    return 'city'
                    break
                elif "east" in choice.lower():
                    print "You wander down the path and into the jungle."
                    return 'egohn_jungle'
                    break
                else:
                    print "Please enter something that makes sense"
                    continue

class Blue_treehouse(Scene):

    def enter(self):
        print "You have to climb a 100 ft rope to get into the treehouse."
        print "You decide to do it because why not?"
        print "Press w to climb"
        thing = 0
        for i in range(3):
            print """   |||
                        |||
                        |||
                        |||
                        |||
                        |||"""
        while True:
            bruh = getch()
            if bruh == "w":
                thing += 1
            if thing == 50:
                print "oh man you start to get tired, and you finally let go of the rope."
                print "You fall to your death."
                break
        return 'death'
class Dope_treehouse(Scene):

    def enter(self):
        print "You have to climb a longggg ladder to get to it."
        print "Press w to climb the ladder."
        time.sleep(pause * 3)
        thing = 0
        for i in range(2):
            print"""    ||   ||
                        ||===||
                        ||   ||
                        ||===||
                        ||   ||
                        ||===||
                        ||   ||
                        ||===||
                        ||   ||
                        ||===||
                        ||   ||
                        ||===|| """
        while True:
            bruh = getch()
            if bruh == "w":
                thing += 1
            if thing == 25:
                print "Wow that was a workout."
                break
        print "You are now inside the treehouse!"
        print "It is one large room with a couch, a king size bed, and a desk."
        print "A man is working at the desk. His eyes literally pop out from his head."
        print "He looks like he is very focused."
        print "When he sees you standing there, he isn't surprised at all, he looks almost happy."
        time.sleep(pause * 3)
        if Opening.language_key == True:
            print Translation.dialogue[4]
        else:
            print Translation.dialogue['man_in_treehouse']
        print "A portal appears!"
        print """
                         .,-:;//;:=,
                 . :H@@@MM@M#H/.,+%;,
              ,/X+ +M@@M@MM%=,-%HMMM@X/,
             -+@MM; $M@@MH+-,;XMMMM@MMMM@+-
            ;@M@@M- XM@X;. -+XXXXXHHH@M@M#@/.
          ,%MM@@MH ,@%=            .---=-=:=,.
          -@#@@@MX .,              -%HX$$%%%+;
         =-./@M@M$                  .;@MMMM@MM:
         X@/ -$MM/                    .+MM@@@M$
        ,@M@H: :@:                    . -X#@@@@-
        ,@@@MMX, .                    /H- ;@M@M=
        .H@@@@M@+,                    %MM+..%#$.
         /MMMM@MMH/.                  XM@MH; -;
          /%+%$XHH@$=              , .H@@@@MX,
           .=--------.           -%H.,@@@@@MX,
           .%MM@@@HHHXX$$$%+- .:$MMX -M@@MM%.
             =XMMM@MM@MM#H;,-+HMM@M+ /MMMX=
               =%@M@M#@$-.=$@MM@@@M; %M%=
                 ,:+$+-,/H#MMMMMMM@- -,
                       =++%%%%+/:-.
                """
        print "Do you accept his offer?"

        choice = raw_input("> ")

        if choice == "yes":
            print "Ok, he pushes you toward the portal and you jump in!"
            print "You are never heard from again, that's too bad."
            print "Nice job!"
            return 'death'
        else:
            print "You slowly back out as the man comes towards you."
            print "You speed down the ladder, but you can see he is right behind you."
            print "As you get down, he is just steps behind you."
            if Maze.alienDog == True:
                print "But, your trusty companion %r, starts barking and the man is scared away." % Opening.dog_name
                print "You walk back towards the spaceship and out of that terrible village."
                print "You are surrounded by jungle on all sides of you, but you can see faint"
                print "paths in each direction: west and east."
                print "You can get back in your ship and leave, or you can keep exploring Omega Argosa 1."


                while True:
                    choice = raw_input("> ")
                    if "ship" in choice.lower():
                        print "Ok you're not too adventurous."
                        return 'space'
                        break
                    elif "west" in choice.lower():
                        print "You start the trek through the eerie jungle."
                        return 'city'
                        break
                    elif "east" in choice.lower():
                        print "You wander down the path and into the jungle."
                        return 'egohn_jungle'
                        break
                    else:
                        print "Please enter something that makes sense"
                        continue
            else:
                print "The man grabs you with his scaly arms and brings you back up to the treehouse."
                print "He then shoves you into the portal."
                print "The world goes black..."
                return 'death'


class Translation(object):
    dialogue = {
        'old_man' : """Old man: Hello, my name is Gelkgo and this is Omega Argosa 1.
        Looks like you just landed here! This is a wonderful planet,
        with jungles that stretch the entire planet, and an interesting
        variety of species that live in those jungles. I live in this tree.
        I never liked living in the city. It is too crowded. The city, Uecliucaberg,
        is to the west by the way. To the east is the Egohn Jungle, where many dangerous
        creatures live. South is where the small village, Blagsek, is located.
        Have a good day!
        """,
        1 : """Old man: Sikgeg, ee seksubek agh Subekgeg agh lekagh agh Gegsubeksek Sekgeg 1.
        Fla aghsubek phleg bakkek aghsubek flasubek! Lekagh agh sek buflabak phlegaghsubek,
        aghlek bakkesubek leksek kekkesubek sik lekaghke phlegaghsubek, agh agh gehflasubekkekka
        seklek geg aghsubeklek leksek aghsubek geh lekgegsubek bakkesubek. Agh aghsubek geh
        lekagh kesubek. Agh subekfla aghsubek aghka geh sik agh. Agh agh fla flakeksubek.
        Sik agh, Baksubeklekaghsekfla, agh geg sik subekkek ee sik phleg. Geg sik ogkek
        agh sik Subekgeg Bakkesubek, gegflasubek agh aghflaphleg kesekbaksubek aghsubek.
        Geglek agh aghgeglekfla bakkesubek, gegflasubek sik bakgeg agh sek baksubek
        seksubek lek, agh agh subekphleggegfla kegeg sekphlegbu sik bakaghflasubek
        seksubek kaseksubek geg. Phleglek agh gegflasubek sik subeksek aghseksubek, Buseksubek, agh gegseksubek.
        Seksubek sek fla phleg!
        """,
        'lady_in_car': " Sik, sik, subek geh sik sek gegaghfla! Agh gegsubek sekka aghsubekfla. Sekgeg, Agh seksubek agh...",
        2: "Hey, hey, get in the car stranger! I love taking hitchhikers. Also, I have candy...",
        'man_in_car': """He says: Sikgeg sekbak Agh' Kegegbak agh Agh agh seksubek phleg geg sik agh.
         Agh kek sek sik sekkeksubek phlegsubek sekphlegbu sik agh.""",
        3: "Heyo wassup I'm Glogsuk and I can take you to the city. I know all the fastest routes around the city.",
        'man_in_treehouse': """He says:  Flasubek! Phleg agh subek ee aghkek subekkek
                            baksubek geg ee subekgegsekaghbu gegsek!
                            Bakkek bak geh agh agh agh subekgeg phleg geg sik agh.
                            Lekflasubek' sek sekaghsik subekaghsubek agh phleg agh phleg,
                            bak subek agh aghgegke leksek, aghsik? """,
        4: """Perfect! You can be my first test subject for my teleportation portal!
            Just jump in and it will teleport you to the city.
            There's a slight chance it may kill you, but we can ignore that, right? """




    }
    def __init__(self, words):
        self.words = words


class Space(Scene):
    def enter(self):
        print "You see your spaceship about 100 feet away."
        print "The bridge of the Green Falcon slowly goes down to create a doorway for you."
        print "It has sensing capibilities just like the flying Priuses back on Earth."
        print "You walk up the steps, and walk down the hall."
        if Maze.alienDog == True:
            print "%r follows you and looks like he's shedding all over the interior aw man." % Opening.dog_name
        time.sleep(pause * 1)
        print "You get to the control room and attempt to start up the engine."
        print "You hear the slight rumble of the ship's engines starting up."
        print "You fly up and out of atomsphere!!!"
        print "Wow, that feeling never gets old."
        print "You start watching Fast and Furious 348 and let autopilot do its thing."

        return 'explore'
        #print "You forgot to get gas though. Remember, your spaceship runs on ion crystals."
        #print "You'll have to go back out to explore."

## Alex's code starts here


y = 100

health = y

t = 0.2

class Scene(object):
    def enter(self):
        pass

class Explore(Scene):
    def enter(self):
        print "..........."
        time.sleep(pause * t)
        print "This is the planet THETA INDRI 7"
        time.sleep(pause * t)
        print "You arrive at a small dock in the middle of nowhere."
        time.sleep(pause * t)
        print "Water surrounds the dock for as far as you can see."
        time.sleep(pause * t)
        print "The Seaweed Forest lies a mile to the west."
        time.sleep(pause * t)
        print "To the north, the waves are rough, lightning flashes, and"
        print "thunder roars.  A storm is approaching.  You must act fast"
        time.sleep(pause * t)
        print "To the south, the water is calm, and there is a faint sight of"
        print "land in the distance."
        time.sleep(pause * t)
        print "To the east, a submarine sits by the dock."
        return 'travel'

class Travel(Scene):
    inventory = []
    def enter(self):

        print "You stand at the dock, contemplating your decision."

        decide = raw_input("> ").lower()

        if "east" in decide:
            print "You enter the submarine."
            time.sleep(pause * t)
            print "The submarine looks like it hasn't been used in years."
            time.sleep(pause * t)
            print "Rust has formed on most of the walls and a diving suit"
            time.sleep(pause * t)
            print "lies in the corner."
            time.sleep(pause * t)
            print "You are hesistant, but the door slams down on you.  There is"
            time.sleep(pause * t)
            print "no going back now."
            return 'intro'
            time.sleep(pause * t*2)
        elif "north" in decide:
            print "As you move north, you slip on the wet wood and fall into the"
            print "water.  The waves throw you around as you attempt to climb"
            print "back onto the dock.  You get stuck in a whirlpool and tumble"
            print "into darkness."
            health = y - 40
            return 'intro'
            time.sleep(pause * t*2)
        elif "south" in decide:
            print "As you move south, the shaky wood on the platform crumbles"
            print "and you fall into the water.  As you attempt to climb back"
            print "onto the dock, a group of white sharks attacks you."
            return 'death'
        elif "west" in decide:
            print "You try to walk in the west direction, but you are stopped by"
            print "an invisible wall."
            return 'travel'
        else:
            print "Choose a different direction."
            return 'travel'

class Intro(Scene):
    def enter(self):
        print "Welcome to the underwater city of Aquilean"
        time.sleep(pause * t)
        return 'city_2'


class City_2(Scene):
    def enter(self):
        time.sleep(pause * 2)
        print "This is the town square.  You see the Aquilean harbor to the"
        print "left, the suburbs directly in front of you, and shops to the"
        print "right."
        print "When you're ready, enter where you want to go.(l, f, q, or p)"

        place = raw_input("> ").lower()

        if "l" in place:
            return 'hunter'
        elif "harbor" in place:
            return 'hunter'
        elif "f" in place:
            return 'resort'
        elif "b" in place:
            return 'resort'
        elif "right" in place:
            return 'wood'
        elif "p" in place:
            return 'wood'
        elif place == "q":
            return 'school'
        else:
            print "That doesn't seem to be a valid direction."
            return 'city_2'


class Hunter(Scene):
    def enter(self):
        time.sleep(pause * t)
        print "At the harbor, you encounter a shark hunter."
        time.sleep(pause * t)
        print "The shark hunter leads you to his lair."
        time.sleep(pause * t)
        if Opening.language_key == True:
            print "SHARK HUNTER: Subek, geh subekgeh bak gehaghka sik baklek geggeh"
            print "lek.  Bak, Geg geg geg geh!"
        else:
            print "SHARK HUNTER: Hello, you have walked straight into my trap."
            print "HA HA HA stupid!"
        time.sleep(pause * t)
        print "The shark hunter latches the door, trapping you inside with him."
        time.sleep(pause * t)
        print "He picks up a club and moves menacingly towards you."
        time.sleep(pause * t)
        print "You see three objects on a table: a sword, a shovel, and a key."
        print "Choose one: "

        choice = raw_input("> ").lower()

        if "w" in choice:
            print "You attempt to fight the shark hunter."
            time.sleep(pause * t)
            print "He lets you win, but you take a lot of damage."
            health = y - 25
            Travel.inventory.append("sword")
            time.sleep(pause * t)
            print "You exit the room."
            return 'city_2'
        elif "h" in choice:
            print "You use the shovel to dig a hole in the wall and you escape."
            Travel.inventory.append("shovel")
            return 'city_2'
        elif "k" in choice:
            print "The doors cannot be opened with keys."
            time.sleep(pause * t)
            print "You are forced to fight the shark hunter and lose badly."
            health = y - 35
            Travel.inventory.append("key")
            time.sleep(pause * t)
            print "You exit the room."
            return 'city_2'
        else:
            print "That object is not present in the room.  You probably"
            print "should have picked up one of the given objects."
            time.sleep(pause * t)
            print "You are forced to fight the shark hunter and lose badly."
            time.sleep(pause * t)
            print "You exit the room."
            return 'city_2'


class Resort(Scene):
    def enter(self):
        time.sleep(pause * t)
        print "Here, you encounter a mermaid."
        time.sleep(pause * t)
        print "The mermaid leads you to the underwater resort of Aclantis."
        time.sleep(pause * t)
        if Opening.language_key == True:
            print "MERMAID: Gehbaklek subekgeh geg gehkek lek lek baklek.  Subeklek"
            print "agh!"
        else:
            print "MERMAID: Hello this is the spa Aclantis. I hope you have fun here."
        time.sleep(pause * t)
        print "You can choose from three activities: swimming, diving, or surfing."

        activity = raw_input("> ").lower()

        if "m" in activity:
            print "You go for a relaxing swim in the pool."
            time.sleep(pause * t)
            print "You exit the resort."
            return 'city_2'
        elif "d" in activity:
            print "You dive among the strange underwater creatures at the bottom of"
            print "the sea."
            time.sleep(pause * t)
            print "While diving, you find a very rare pearl on the ocean floor."
            Travel.inventory.append("pearl")
            time.sleep(pause * t)
            print "You exit the resort."
            return 'city_2'
        elif "f" in activity:
            print "You ride the huge waves on the outskirts of the city."
            time.sleep(pause * t)
            print "It is a lot of fun, but you fall once and scrape your knee."
            health = y - 10
            time.sleep(pause * t)
            print "You exit the resort."
            return 'city_2'
        else:
            print "Are you really going to come to this resort and do nothing?"
            time.sleep(pause * t)
            print "You exit the resort."
            return 'city_2'

class Wood(Scene):
    def enter(self):
        time.sleep(pause * t)
        print "This is the Aquilean woodworking shop."
        time.sleep(pause * t)
        if Opening.language_key == True:
            print "CARPENTER: Geg subek lekkek sek geg geglekgeg kaleklek."
            print "Phlegsubeklek fia lek!"
        else:
            print "CARPENTER: Hello I am the carpenter and here you can"
            print "make some cool things!"
        time.sleep(pause * t)
        print "He offers you three objects: a hammer, a drill, and a chainsaw."

        tool = raw_input("> ").lower()

        if "m" in tool:
            print "You use the hammer to help the carpenter build a small box."
            time.sleep(pause * t)
            print "As a reward, the carpenter lets you keep the box."
            Travel.inventory.append("box")
            time.sleep(pause * t)
            print "You exit the shop."
            return 'city_2'
        elif "d" in tool:
            print "You use the drill to help the carpenter build a bottle."
            time.sleep(pause * t)
            print "As a reward, the carpenter lets you keep the bottle."
            Travel.inventory.append("bottle")
            time.sleep(pause * t)
            print "You exit the shop."
            return 'city_2'
        elif "c" in tool:
            print "You use the chainsaw to get wood for the carpenter."
            time.sleep(pause * t)
            print "As a reward, the carpenter lets you keep some of the wood."
            time.sleep(pause * t)
            print "However, you have no use for the wood, so you drop it."
            time.sleep(pause * t)
            print "You exit the shop."
            return 'city_2'
        else:
            print "You did not pick up an available object."
            time.sleep(pause * t)
            print "The carpenter is very disappointed in you."
            time.sleep(pause * t)
            print "You exit the shop."
            time.sleep(pause * t)
            return 'city_2'

class School(Scene):

    Travel.inventory_list = ["sword", "shovel", "key", "pearl", "box", "bottle"]
    item_one = (random.choice(Travel.inventory_list))
    item_two = (random.choice(Travel.inventory_list))
    item_three = (random.choice(Travel.inventory_list))

    def enter(self):
        print Travel.inventory
        time.sleep(pause * t)
        print "Welcome to Aquilean University."
        time.sleep(pause * t)
        print "On a holographic 4D SMART device, you see three words, which may"
        print "or may not match items you have picked up."

        print School.item_one
        time.sleep(pause * t)
        print School.item_two
        time.sleep(pause * t)
        print School.item_three


        if Travel.inventory == []:
            print "You don't own any items!"
            print "You must return to the city."
            return 'city_2'

        for i in range(0,len(Travel.inventory)):
            if Travel.inventory[0] == School.item_one:
                print "You own one of the selected items!"
                return 'hangman'
            elif Travel.inventory[0] == School.item_two:
                print "You own one of the selected items!"
                return 'hangman'
            elif Travel.inventory[0] == School.item_three:
                print "You own one of the selected items!"
                return 'hangman'
            elif Travel.inventory[1] == School.item_one:
                print "You own one of the selected items!"
                return 'hangman'
            elif Travel.inventory[1] == School.item_two:
                print "You own one of the selected items!"
                return 'hangman'
            elif Travel.inventory[1] == School.item_three:
                print "You own one of the selected items!"
                return 'hangman'
            elif Travel.inventory[2] == School.item_one:
                print "You own one of the selected items!"
                return 'hangman'
            elif Travel.inventory[2] == School.item_two:
                print "You own one of the selected items!"
                return 'hangman'
            elif Travel.inventory[2] == School.item_three:
                print "You own one of the selected items!"
                return 'hangman'
            else:
                print "You do not own one of the selected items!"
                print "You must return to the city."
                return 'city'

class Hangman(Scene):
    def enter(self):
        import random

        print "Because you own a selected item, you now have the chance to gain"
        print "mastery of the Aquilean language."
        time.sleep(pause * t)
        if Opening.language_key == True:
            print "TEACHER: Gehgeg geh lek bakkeksik lek fia lekgeh leklek.  Phlegog "
            print "gehgeg subeklek geg Geg geg lekgehbak geh geggeh fia baklek lek fia "
            print "Subekphleggeglekgeg gegaghsubeklek."
        else:
            print "TEACHER: You want to become fluent in our language? Alright all"
            print "you need to do is complete this game and you will be completely"
            print "fluent. I love teaching even though I don't get paid enough."
        time.sleep(pause * t)
        print "Complete this game of Hangman to learn the Language skill."

        word_list = ["crypt",
        "curacao",
        "daiquiri",
        "dirndl",
        "espionage",
        "fuchsia",
        "kilobyte",
        "nightclub",
        "quixotic",
        "stronghold",
        "topaz",
        "triphthong",
        "voyeurism",
        "whomever"]

        secret_word = random.choice(word_list)
        dashes = ["-"] * len(secret_word)
        guesses_left = 10

        def get_guess():
            while True:
                guess = raw_input("Guess a letter: ")
                try:
                    if len(guess) != 1:
                        print "That guess is more than 1 letter!"
                        continue
                    elif not guess.islower():
                        print "That is not a lowercase letter!"
                        continue
                    else:
                        return guess
                except:
                    continue

        def update_dashes():
            for i in range(len(dashes)):
                if secret_word[i] == guess:
                    dashes[i] = guess
                else:
                    dashes[i] = dashes[i]
            return dashes


        while "".join(dashes) != secret_word and guesses_left != 0:
            print "".join(dashes)
            print "You have " + str(guesses_left) + " incorrect guesses left."
            guess = get_guess()
            if guess in secret_word:
                dashes = update_dashes()
            if guess not in secret_word:
                guesses_left = guesses_left - 1


        if guesses_left == 0:
            print "You lose. The word was: " + str(secret_word)
            print "You must try again."
            return 'hangman'
        else:
            print "Congrats! You win. The word was: " + str(secret_word)
            time.sleep(pause * t)
            print "You now have the ability to use LANGUAGE"
            Opening.language_key = True
            print "You can either complete the game, or play again, now that you have mastered language."
            play_again = raw_input("What do you do? ")
            if 'complete' in play_again:
                return 'victory'
            else:
                return 'opening'




class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        #prints current scene
        current_scene.enter()

class Map(object):

    # add your scenes here
    scenes = {
        'opening' : Opening(),
        'omega_argosa_1' : Omega_Argosa_1(),
        'death' : Death(),
        'space' : Space(),
        'egohn_jungle' : Egohn_jungle(),
        'city_2' : City_2(),
        'city_1': City_1(),
        'maze': Maze(),
        'blagsek': Blagsek(),
        'afterdog': AfterDog(),
        'dope_treehouse': Dope_treehouse(),
        'driving skill' : Driving_Skill(),
        'blue_treehouse' : Blue_treehouse,
        'explore' : Explore(),
        'travel' : Travel(),
        'intro' : Intro(),
        'city' : City(),
        'hunter' : Hunter(),
        'resort' : Resort(),
        'wood' : Wood(),
        'school' : School(),
        'hangman' : Hangman(),
        'victory' : Victory()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('opening')
a_play = Engine(a_map)
a_game = a_play
a_game.play()
