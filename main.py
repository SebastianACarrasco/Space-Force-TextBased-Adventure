import random
import sys
import time
import pickle


#global classes and functions
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.scrap = 10
        self.companion = ""
        # append any new items obtained
        self.item = []

    def display(self, name):
        print("Name:", self.name, "\nHealth:", self.health, "\nDamage:",
              "\nScrap:", self.scrap)

class Weapons:
    def __init__(self):
        self.pipe = "pipe"
        self.pipeHealth = 50
        self.glock = "glock"
        self.ammo = 10

weapons = Weapons()


class Boss:
    def __init__(self):
        self.health = 130
        self.damage = 13

boss = Boss()

class Infected:
    def __init__(self):
        self.health = 60
        self.damage = 5


# start
def main():
    b = " "
    print("Welcome to Space Force, a text-based RPG")
    print("press the number or the type the word")
    print(b)
    print("1) Start")
    print("2) Load")
    print("3) Exit")

    option = input("--> ").upper()
    if option in {"1", "START", "S"}:
        player_name()
    elif option in {"2", "LOAD", "L"}:
        whichLoad = input("Did you board the abandon ship or stay in? [board/stay]").upper()
        if whichLoad == "BOARD":
            load()
        elif whichLoad == "STAY":
            load2()
        else:
            main()
    elif option in {"3", "EXIT", "E"}:
        print("Your loss...")
        time.sleep(2)
        sys.exit()
    else:
        main()


# Player Name
def player_name():
    print("What will your name be?")
    option = input("-->  ")
    global user
    user = Player(option)
    print("{}? Alright then. Let's begin!".format(user.name))
    time.sleep(3)
    prologue()

def load():
    print("loading")
    time.sleep(3)
    openf = pickle.load(open("Save File", "rb"))
    openf.display(Player.display)
    return finally_inside_ship2()

def load2():
    print("loading")
    time.sleep(3)
    openf = pickle.load(open("Save File", "rb"))
    openf.display(Player.display)
    return going_to_command()

def stats():
    print("Name: ", user.name)
    print("Health: ", user.health)
    print("Items: ", user.item)
    print("Scrap: ", user.scrap)

    
#attacking function
def attack():
    if user.health > 0:
      for x in range(6):
          print("As you are running you hear something coming up.")
          doit = random.randint(0,1)
          if doit == 1:
            print("It's one of the infected!")
            print("You check your inventory: {}".format(user.item))
            print(" ")
            attack = input("Do you attack? [Y/N]").upper()
          
            if attack == "Y":
              print("You attack the enemy. As he attacks you, you blow its brains out and it falls to the ground")
              print("You take some damage")
              #user.item[0] -= 3
              dam = random.randint(7,16)
              user.health -= dam
              print(user.item, "/n", user.health)
            elif attack == "N":
              print("You ran away to avoid conflict.")
              user.health -= dam
              print(user.health)
            else:
              continue
          elif doit == 0:
            print("It was just a loose pipe. You continue")
            continue
    else:
      print("You died. Want to restart?")
      sys.exit()


def boss_fight():
    if user.health > 0:
      print("You use your {} and knock back the creature, but it rapidly gets up and lunges at you, pushing you back".format(user.item))
      boss.health -= 5
      user.health -= 3
      print("Your health: {} \n Creature health: {}".format(user.health,boss.health))
      for x in range(6):
          print("You take a step back and prepare to fight")
          doit = random.randint(0,1)
          if doit == 1:
            print("The creature lunges at you")
            print("You check your inventory: ", user.item)
            print(" ")
            attack = input("Do you attack? [Y/N]").upper()
          
            if attack == "Y":
                print("You attack the creature. The hit seems effective, but it doesn't flinch and hits you back")
                print("You take some damage")
                #user.item[1] -= 4
                user.health -= 15
                print(user.item, "/n", user.health)
            elif attack == "N":
                print("You take a couple of steps back to catch your breath and think about an attack plan. The creature runs at you and spits some green substance onto your face")
                dam = random.randint(5,10)
                user.health -= dam
                print("player health: {}".format(user.health))
            else:
              continue
          elif doit == 0:
              print("Your friend decides to take the fight and protects you for one of the attacks")
              continue
    else:
      print("You died. Want to restart?")
      sys.exit()
        
#ending
def finalBoss():
    print('''
    As soon as you walk in a person in black runs to the escape pod and escapes. The room turns red and you hear over the PA: 'Warning warning, core overheated. 
    Evecuate immediately. T minus 2 minutes until core overheat.' You get very nervous as you now have to choose who gets to live now that there is one pod
    ''')
    #if companion is alive
    if user.companion != "":
        print("Before anything you have to deal with the now-creature in the room. Your {} will not do, you need assistance from your companions".format(user.item))
        print(
          '''{} I need you to distract it while I sneak up from behind and cripple it. He agrees and decides to go around. He grabs the attention from the creature and it begins to follow. You decide to sneak up and hit it from the back.
          It suddenly turns around and throws you back a couple of feet
          '''.format(user.companion))
        user.health -= 21
        print("Health: ", user.health)

        print(
          '''As you get back up, you see {} is cornered and he gets biten by the creature. His head is ripped off and the creature eats it. On the spot he dies.
          '''. format(user.companion))
        user.companion = ""
        print(
            '''You are in disbelief but nothing can be done. On the other hand, you realize that the decision for choosing who gets to live is simplified.
            You and Jaimy are left and you still have the brute to fight and take command, all in under 2 minutes. The both of you approah the creature and decide to have a battle.
            ''')
        boss_fight()
        choices()
        
    #if companion is not alive
    else:
        print("Before anything you have to deal with the now-creature in the room. Your {} will not do, you need assistance from Jaimy".format(user.item))
        print(
          '''Jaimy I need you to distract it while I sneak up from behind and cripple it. He agrees and decides to go around. He grabs the attention from the creature and it begins to follow. You decide to sneak up and hit it from the back.
          It suddenly turns around and throws you back a couple of feet.
          ''')
        user.health -= 20

        print("Health: ", user.health)
        print("Jaimy helps you get up and you have a clear chance to fight the creature")
        boss_fight()
        choices()

def choices():
    print('''
          Now it's just you and Jaimy, the Boss is defeated. there's only 1 minute left before core meltdown. 
          You realize there is not enough time to fix it and you must leave now. Jaimy and you look at each other, you know one has to stay because there is only one escape pod. 
          Jaimy insists you go, after all you are the captain and you need to return to your crew. On the other hand, you are the captain and captains always stay last on their vessel.
          ''')
    time.sleep(4)
    help = input("Do you save Jaimy or yourself? [Jaimy, You]").upper()
    if help == "JAIMY" or help == "J":
        print('''
            You yell, 'Jaimy, go I'll stay and see what I can do to slow this down. Do not argue with me!' Jaimy begins to tear and gives you a hug and salute. 
            He boards the escape pod and launches himself to safety. You know that you cannot do anything to prevent the meltdown so you just look out into the deep space and see your planet as a little speck in the distance. 
            You immediately remember your childhood and all your men, they are all safe. Whoever the person in black was escaped. There is nothing you can do. Hopefully Jaimy reports it and they start a hunt. 
            'Why did they do this? What was on the ship?' You ask yourself. You will never know. As you take your last breath you feel the room heat up immensely and you close your eyes.
            ''')
        time.sleep(2)
        print("The End")
        sys.exit()
            
    elif help == "YOU" or help == "Y":
        print('''
            You decide it's best to save yourself, after all you are the captain of a ship and your men need you. Time is running out so you decide it is best to tell him quickly.
            You approach him, 'Hey Jaimy I know this is going to be hard but there is only one escape pod and it is best for everyone if I take it.' Jaimy looks at you disappointed but he understands,
            he seems to have taken it well compared to what you imagined. You give him a hug and he hands you his necklace, 'Give this to my daugther and wife.' You feel regret for what you did
            but you continue and ignore the feeling of regret. You board the pod, strap up, and press the eject button. The pod detaches and the both of you watch each other until the pod is out and flying.
            You see the ship blow up behind you and all you can think is about is Jaimy. 'I'm gonna find that person dressed in black. He was there for a reason, and probably a good one. 
            You return to your ship and your men look at you and do not say anything. You go into your cabin and immediately ask the navigators to direct the ship back home, you have some things to do.
            ''')
        time.sleep(2)
        print("The End")
        sys.exit()

            



#this function has bugs
#
#           
# Decided to board the ship
def finally_inside_ship2():
    print("{}, Jaimy, and you board the ship from the starboard side.".format(user.companion))
    print("As you enter you take your helmets off and there is a stench that stinks up the entire corridor. Jaimy throws up")
    print("'What the hell happened' Jaimy says. {} walks further down to see whats up ahead while you help Jaimy out".format(user.companion))
    print("'Hey I found something!' {} says. As you help Jaimy up you walk down the corridor".format(user.companion))
    print("You see medbay's door is breached and blood is leaking from the room")
    print("You guys decided one should go investigate")
    who = input("You are the leader so you decide who gets to go. Who should go? [Companion/You]").upper()
    if who == "COMPANION" or "C":
        print(
          '''{} goes. He opens the door and sees many dead bodies decapitated and there is blood everywhere. The smell is immesurable. You spot a small worm crawl inside one of the bodies
          Out of no where one of the bodies move, it's the one the worm was in! It looks like it needs help says {} and he approaches it and You and Jaimy both yell 'Don't go to it! It's infected!
          {} doesn't hear you and gets closer. Suddenly the body twitches and it bites {}'s neck. He dies on the spot and quickly his body is taken by the worm
          '''.format(user.companion, user.companion, user.companion, user.companion))
        time.sleep(4)
        print(
          '''{}, now dead but alive, rose up and tries to attack you but you defend yourself and give him mercy. You and Jaimy are left and you guys are scared. The hallway back to the shuttle closed and your only way is forward.
          '''.format(user.companion))
        user.companion = ""
        user.item.append("Flamethrower")
        print("You are running and pass by the armory and pick up some flamethrower as you decided it is best to blow up the ship.")
        stats()        
        attack()
        
        print("You finally reach the main entrance to the command room and you spot your heavy lifter inside wandering around.")
        print("He appears to be mutated and you see someone in a black uniform trying to override the terminal")
        print("You andJaimy decide to do something about it.")
        print("{} what are we going to do, says Jaimy.".format(user.name))
        print("'We fight', you say with bravery. The three of you open the door.")
        time.sleep(3)
        stats()
        finalBoss()

    elif who == "YOU" or "Y":
        print('''You decided to take the initiative and go first. After all you are in charge of the men with you.
            As you enter, you spot many bodies on the floor. The gore is immense and Jaimy can't look. Suddenly one begins to move; you think the person is still alive. They are face down and as you turn them over it attacks you!. It grasps you and scratches you, leaving a big scar
            ''')
        user.health -= 10
        print("Health: %s" % (user.health))
        print(
            '''Jaimy patches you up. 'What the hell is going on?' you say. The three of you look around and decide you should run back, little did you know that the doors behind you locked up due to lack of pressure from a hole that
            breached the ship.'{} I'm scared' says {}. The only option is to move forwards. Luckily for you, you see an emergency exit map on the wall and you are able to pick up some Flamethrower from a nearby armory to blow the ship. It shows that there is an escape pod a couple of hundred meters down the hall.
            You decide you need to get going. However, only you notice that the escape pod is only availble for one person to enter but there's two of them. You head out for them and stay quiet about the number
            '''.format(user.name, user.companion))
        time.sleep(3)
        user.item.append("Flamethrower")
        attack()
        print("You finally reach the main entrance to the command room and you spot your heavy lifter inside wandering around.")
        print("He appears to be mutated and you see someone in a black uniform trying to override the terminal")
        print("You, Jaimy, and {} decide to do something about it.".format(user.companion))
        print("{} what are we going to do, says Jaimy.".format(user.name))
        print("'We fight', you say with bravery. The three of you open the door.")
        time.sleep(3)
        stats()
        finalBoss()
    else:
        finally_inside_ship2()

def inside_ship2_intro():
    print("You decided to board, but first you need a team of three, including you, to enter")
    print("The only survivors that are closest to you are Jaimy, Jack, and Hugh.")
    print("Jaimy has been your friend since highschool so you have to bring him. Jack and Hugh are new recruits so you do not know their skills.")
    option = input("Who do you take? [Jack, Hugh]").upper()
    people = ["Jack", "Hugh"]
    if option == "JACK":
        user.companion = "Jack"
    elif option == "HUGH":
        user.companion = "Hugh"
    else:
        random.choice(people)

    print("You decided to take {} with you and three of you head off into the ship".format(user.companion))
    time.sleep(3)

    def ask_save():
        ask = input("You reached a checkpoint. Would you like to save your stats[Y/N] -->  ").upper()
        if ask == "Y":
            save = Player(user.name)
            pickle.dump(save, open("Save File", "wb"))
        elif ask == "N":
            print("If you die you will need to restart")
            return
        else:
            ask_save()

    ask_save()
    finally_inside_ship2()


# Decided to stay on board
def going_to_command():
    print("You're running down a corridor")
    attack()
    print("You finally reach the main entrance to the command room and you spot your heavy lifter inside wandering around.")
    print("He appears to be mutated and you see someone in a black uniform trying to override the terminal")
    print("You, Jaimy, and {} decide to do something about it.".format(user.companion))
    print("{} what are we going to do, says Jaimy.".format(user.name))
    print("'We fight', you say with bravery. The three of you open the door.")
    time.sleep(3)
    finalBoss()


def inside_ship_ending():
    print("You reach the mess hall and find Jaimy fighting Curie. Everyone but you and Jaimy seem to have survived. Jaimy slices off Curies head")
    print("We need to get to the command room and call for help you tell Jaimy.")
    print("Jaimy in shock, 'y-y-yes we need to g-g-et back'")
    print("Before heading out you check your stats on your smart watch")
    time.sleep(2)
    stats()
    print("you head out to take the ship back")
    def ask_save():
        ask = input("You reached a checkpoint. Would you like to save your stats[Y/N] -->  ").upper()
        if ask == "Y":
            save = Player(user.name)
            pickle.dump(save, open("Save File", "wb"))
        elif ask == "N":
            print("If you die you will need to restart \n \n")
            return
        else:
            ask_save()

    ask_save()
    going_to_command()


#keep or float people
def float_people():
    print("You run to command and order Jaimy to release the sector")
    print("'{} are you sure?' Jaimy says. You give him a look that scares him and he floats them.".format(user.name))
    time.sleep(5)
    print("After the incident you go into a state depression as you just killed half your men. You stayed in your cabin for hours the next day until you get a call from Jaimy...")
    time.sleep(5)
    print("Sir! more people are starting to get infected and react like the others that we floated.")
    print("This is a nightmare you say to yourself. You run to the mess hall and see what is happening. While running there you stop by the sector that was disconnnected and you see a finger from the dead you floated. 'Oof' you say to yourself and grab a pipe because you know it is going to get messy")

    user.item.append(weapons.pipe)
    user.item.append(weapons.pipeHealth)
    time.sleep(4)
    inside_ship_ending()


def keep_people():
    print("You can't have such a death toll on you so you keep the men.")
    print("'Jaimy leave them inside and set guards to block the sector' you say")
    time.sleep(5)
    print("a couple of hours passed and you passed by the abandoned ship. Suddenly sirens start to go off and you listen to the PA, 'Attention all personnel, the quarantine sector has been breached and the men appear to be running around eating our members. All healthy people please report to the mess hall'")
    print("You run to the mess hall and pick up a gun from the armory on the way there")

    user.item.append(weapons.glock)
    user.item.append(weapons.ammo)
    stats()
    print("You run towards the mess hall and see Drake, a member from the R & D team. He starts to run towards you and you have no choice but to shoot him. You are in disbelief and stop for a moment to see Drakes's body. His skin is beaten, his eyes are black, and he has bumps all over him. The epidemic somehow escaped the quarantine zone")

    inside_ship_ending()


def stay_in_ship():
    print("You decided to stay on board and let curiosity get the best of you")
    time.sleep(5)
    print("You get back to work and send robots back to gather more supplies from other planets. You need at least 50 from every planet you visit")

    def scrap_gather2(option):
        if option == "Y":
            user.scrap += 10
            print("Currently have: ", user.scrap)
            option2 = input("Do you send the robot back? [Y/N] ").upper()
            scrap_gather2(option2)

        elif option == "N" and user.scrap < 50:
            print("Sorry you do not have enough supplies")
            again = input("Do you send the robot back? [Y/N] ").upper()
            scrap_gather2(again)
        elif option == "N" and user.scrap >= 50:
            print("You have enough supplies and head back out into the deep unknown.")
            return;
        else:
            ree = input("Do you send the robot back? [Y/N] ").upper()
            scrap_gather2(ree)

    do_it = input("Do you send the robot? [Y/N] ").upper()
    scrap_gather2(do_it)

    time.sleep(3)
    print("After some time of working some of your crew members get sick out of no where. You put them at sick bay.")
    print("After three days the sick start to develop bumps and are coughing up blood. You decided to quarantine them.")
    print(
        "You decide to check the robot since the sick ones were working on it after it got damaged. You see something strange move on the robot and seconds later you hear screaming coming from the quarantine zone and you run to it. Everyone is dead.")
    time.sleep(5)
    print(
        "'What is happening?' you say to yourself. Minutes into your grieving you see that the dead people start to move. Now you are really confused.")
    print(
        "They start to scream and eventually they turn around, their eyes are black and something is crawling out of their mouth.")
    print("'F*#k F*#k F*#k' you say. You must react quick. The quarantine zone is in its own detachable section from the ship")
    ohNah = input("Do you float the sick to save the others or keep them to see what happens? [FLOAT,KEEP]").upper()

    if ohNah == "FLOAT":
        float_people()
    elif ohNah == "KEEP":
        keep_people()
    else:
        stay_in_ship()


# ship encounter start
def ship_encounter():
    time.sleep(7)
    print("The following day while travelling, your crew spots a ship.")
    print("'Captain {} the ship appears to be abandoned' says Jaimy. Your crew says you should check it out. 'Alright, I say...'".format(user.name))
    option = input("Do you go and explore the ship or leave it and proceed on your current mission? [GO/STAY]").upper()

    if option == "GO":
        inside_ship2_intro()
    elif option == "STAY":
        stay_in_ship()
    else:
        ship_encounter()


# part 1
def part_one():
    time.sleep(5)
    print("Some time has passed ever since your departure and you are running low on supplies. Luckily there's a planet nearby which contains material needed for the ship.")
    print("You have a robot and send it down to collect material...")
    time.sleep(5)
    user.scrap += 10
    print("Gathered + %s" % (user.scrap))

    # function lets player gather supplies. Cannot proceed unless player has >= 50 scrap
    def scrap_gather(option):
        if option == "Y":
            user.scrap += 10
            print("Currently have: %s" % (user.scrap))
            option2 = input("Do you send the robot back? [Y/N] ").upper()
            scrap_gather(option2)

        elif option == "N" and user.scrap < 50:
            print("Sorry you do not have enough supplies")
            again = input("Do you send the robot back? [Y/N] ").upper()
            scrap_gather(again)
        elif option == "N" and user.scrap >= 50:
            print("You have enough supplies and head back out into the deep unknown.")
            user.scrap -= 50
            print("Scrap left: ", user.scrap)
            time.sleep(3)
            ship_encounter()
        else:
            ree = input("Do you send the robot back? [Y/N] ").upper()
            scrap_gather(ree)

    print("You need fifty to repair the ship which took damage from a meteor shower.")
    do_it = input("Do you send the robot back? [Y/N] ").upper()
    scrap_gather(do_it)


# Prologue
def prologue():
    print("Welcome Captain {}".format(user.name))
    print(
        "You have been selected to operate the ship USS HitOrMiss. The ship is a patrol ship which can also act as a supply gatherer.")
    print(
        "You board the ship and meet your crew members. They seem to be like nice people but you can't be as nice because you need to assert dominance as captain.")
    print("One of your members approaches you.")
    print(
        "Jack: Hey Capt'n! It's a pleasure to finally meet you. Everyone here is friendly and we all hope we can get along. I am in charge of supplies and I keep track of our scrap metal through this tablet.")
    print("You take the tablet and familiarize yourself with it.")
    print(
        "Jack: You can keep that one we got more spares in our department. Can't wait to set out and look at new galaxies and stop any pirates that might interfere with our ship.")
    print(
        "You set off and begin to set your room. You have dinner with the rest of the crew and have a wonderful night. Afterwards, you return to your room.")
    print("You go to your room and decide if you should look into your inventory.")
    time.sleep(4)
    option = input("Do you wish to see your stats? [Y/N]").upper()
    if option == "Y":
        stats()
        part_one()
    elif option == "N":
        part_one()
    else:
        prologue()

# start of program
main()