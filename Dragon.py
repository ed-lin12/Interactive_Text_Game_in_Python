import random
import os
import sys


# Class Setup
class warrior(object):
    hp = 24
    dmg = 5
    name = "Warrior"
    desc = "Warriors are mighty heavily armored masters of melee combat that are fueled by the \n" \
           "rage they generate in combat. If you like a straightforward approach, charging into \n" \
           "battle, and bashing heads toe to toe, then Warrior might be a good class choice for you."


class archer(object):
    hp = 18
    dmg = 6
    name = "Archer"
    desc = "Archers are woodsmen skilled at surviving in the wild. If you like a long distance \n" \
           "approach, and picking apart your enemies before they even hear you, the Archer class \n" \
           "might be a good class choice for you."


class mage(object):
    hp = 15
    dmg = 10
    name = "Mage"
    desc = "Students gifted with a keen intellect and unwavering discipline may walk the path of \n" \
           "the Mage. If you like controlling powerful arcane magic, the Mage class is the class to choose."


# Inventory Setup
inventory = {}

# items
sword = {"Bastard Sword": 1}
bow = {"Elven Bow": 1}
wand = {"Dark Staff": 1}
potion = {"Health Potion": 1}
stone = {"Rock": 1}


# Title Screen
def title_screen_options():
    # Allows the player to select the menu options, case-insensitive.
    option = input("> ")
    if option.lower() == ("play"):
        intro()
    elif option.lower() == ("quit"):
        sys.exit()
    elif option.lower() == ("help"):
        help_menu()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Invalid command, please try again.")
        option = input("> ")
        if option.lower() == ("play"):
            intro()
        elif option.lower() == ("quit"):
            sys.exit()
        elif option.lower() == ("help"):
            help_menu()


def title_screen():
    # Clears the terminal of prior code for a properly formatted title screen.
    # os.system('clear')
    print('#' * 45)
    print('# Welcome to this text-based puzzle RPG by #')
    print("#                  Ed Lin                  #")
    print("""             (\               /)
            __)\             /(__
           __)_ \  (\!~!/)  / _(__
          __)_ `.\  )d b(  /.' _(__
        ___)_ `.  \(  _  )// .' _(___
         )_  `. \  ((q_p))  / .'  _(_
         _)`.  \  ,-)\_/(-.  /  .'(_
          _) ,-._/ /vvvvv\ \_,-. (_
          _)/ /(._/v(___)v\_.)\ \(_
           \_ ___/v(_____)v\___ _/
              vvv\(_______)/vvv
             \ vv/v(_____)v\ vv/
             _\ v\ v(___)v / v/_
            '>_`  \`-._.-'/  '_<`
            ' >_,-'       `-._<` """)
    print('#' * 45)
    print("                 .: Play :.                  ")
    print("                 .: Help :.                  ")
    print("                 .: Quit :.                  ")
    title_screen_options()


# Help Menu
def help_menu():
    print("")
    print('#' * 45)
    print("This a game that will test your wits and imagination.")
    print("Play this game by entering the commands when prompted.")
    print("Each class their own advantages and disadvantages.")
    print("Good luck!")
    print('#' * 45)
    print("\n")
    print('#' * 45)
    print("    Please select an option to continue.     ")
    print('#' * 45)
    print("                 .: Play :.                  ")
    print("                 .: Help :.                  ")
    print("                 .: Quit :.                  ")
    title_screen_options()


def choosePath(numberOfPaths):
    choice = 0
    while choice < 1 or choice > numberOfPaths:
        print('1 to ' + str(numberOfPaths) + '> ', end='')
        choice = input()
        if choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5':
            choice = 0
        if choice == '1' or choice == '2' or choice == '3' or choice == '4' or choice == '5':
            choice = int(choice)
    print()
    return choice


def pause():
    print('Press enter to continue.')
    input()


def intro():
    inventory.clear()
    print("What is your name adventurer?")
    playerName = input()
    print("Well " + playerName + ", what type of adventurer are you?")
    print('  1 Warrior ')
    print('  2 Archer ')
    print('  3 Mage ')
    print('  4 Help')
    choice = choosePath(4)
    global player
    if choice == 1:
        player = (warrior)
    if choice == 2:
        player = (archer)
    if choice == 3:
        player = (mage)
    if choice == 4:
        print("Warriors are mighty heavily armored masters of melee combat that are fueled by the \n" \
              "rage they generate in combat. If you like a straightforward approach, charging into \n" \
              "battle, and bashing heads toe to toe, then Warrior might be a good class choice for you.")
        print()
        pause()
        print("Archers are woodsmen skilled at surviving in the wild. If you like a long distance \n" \
              "approach, and eliminating your enemies before they even hear you, the Archer class \n" \
              "will be a good class choice for you.")
        print()
        pause()
        print("Only those gifted with a keen intellect and unwavering discipline may walk the path of \n" \
              "the Mage. If you like controlling powerful arcane magic, the Mage class is the class to choose.")
        print()
        pause()
        print("Well " + playerName + ", what type of adventurer are you?")
        print('  1 Warrior ')
        print('  2 Archer ')
        print('  3 Mage ')
        choice = choosePath(3)

        if choice == 1:
            player = (warrior)
        if choice == 2:
            player = (archer)
        if choice == 3:
            player = (mage)
    print("Ah, good choice, " + playerName + ' the ' + player.name + "!")

    if player == (warrior):
        inventory.update(sword)
    if player == (archer):
        inventory.update(bow)
    if player == (mage):
        inventory.update(wand)
    inventory.update(potion)

    print('The journey ahead is dangerous, check your inventory before you go.')
    pause()
    print("You currently have:")
    for i in inventory.keys():
        print(i)
    pause()
    print('You have ventured to the realm of dragons, and have finally arrived at the Dragon Cave.')
    print('With your trusty weapon at your side and handy backpack on your back, you look upon the fearsome entrance '
          'to the cave.')
    print()
    print('Read carefully. The adventure changes each time you play.')
    print('Treasure or certain death await!')
    print()
    pause()
    front()


def front():
    print('You are standing in front of the entrance of the cave.')
    if skulls == 'present':
        print('There are a bunch of human skulls and bones lying around.')
    if skulls == 'absent':
        print('There is a sign here that reads, "Welcome, visitors!"')
    print()
    print('What will you do?')
    print('  1 Go into the cave.')
    print('  2 Climb on top of the cave.')
    path = choosePath(2)
    if path == 1:
        insideOfCave()
    if path == 2:
        topOfCave()


def topOfCave():
    print('After climbing up, you are standing on top of the cave.')
    print('There is a small hole that seems to be a chimney nearby.')
    if dragonLocation == 'upper':
        print('There is a lot of smoke coming out of the hole.')
    print()
    print('What will you do?')
    print('  1 Climb down the hole.')
    print('  2 Climb back down to the front entrance.')
    path = choosePath(2)
    if path == 1:
        goDownChimney()
    if path == 2:
        front()


def insideOfCave():
    global hpPotion
    global goblin
    hpPotion = 'holding'
    print('You are inside front chamber of the cave. You can see the exit of the cave which would take you outside.')
    print('There are two paths that lead deeper into the cave, one that goes up and the other that goes down.')
    print()
    # random encounter
    if goblin == 'spawn':
        print('From the dark corner of the cave, you can just barely make out a figure of some creature... ')
        print('It\'s a Goblin! You raise your weapons to defend yourself....(press enter)')
        pause()
        print(
            'The goblin holds his hands up and speak, "Wait adventurer, my name is Frok and I do not wish to fight you!')
        print("What will you do?")
        print('  1 Sheath your weapons and listen to his story.')
        print('  2 Ignore the Goblin and attack him anyway.')
        goblin = 'dead'
        path = choosePath(2)
        if path == 1:
            print('Frok smiles as he sees you put away your weapon.')
            print(
                'He continunes with his story, "My people have been living in this cave for centuries in peace, but recently a mighty dragon has taken our home"')
            print(
                'As you Frok talks to you, you feel a rustling in your backpack - you reach behind you to see what it is... (press enter)')
            input()
            print('It\'s another goblin! He has stolen your health potion!')
            del inventory["Health Potion"]
            hpPotion = 'stolen'
            print(
                'You see Frok and the other goblin run away into the darkness! "You foolish human, thanks for the free potion!"...(press enter to check your inventory)')
            input()
            print("You currently have:")
            for i in inventory.keys():
                print(i)
            pause()
            print('That\'s unfortunate, but you continue on with your journey.')
        if path == 2:
            if player == (warrior):
                print(
                    'Trusting your warrior instinct over this goblin, you decide to cleave him in half with your mighty sword! (press enter)')
                input()
            if player == (archer):
                print(
                    'Trusting your survival instinct over this goblin, you decide to shoot two arrows into the goblin\'s head! (press enter)')
                input()
            if player == (mage):
                print(
                    'Without hesitation, you decide to disintegrate the goblin with a powerful destruction spell! (press enter)')
                input()
            print('You hear a yelp behind you - there are more goblins ready to set up an ambush!')
            print('You ready yourself for a battle...(press enter)')
            input()
            print('However, no fight comes as the goblins scatter and flee deeper into the caves.')
            print('Congrats, you made it out of your first encounter unscathed! (press enter)')
            input()

    print('What will you do now?')
    print('  1 Go outside of the cave.')
    print('  2 Take the upper path deeper into the cave.')
    print('  3 Take the lower path deeper into the cave.')
    path = choosePath(3)
    if path == 1:
        front()
    if path == 2:
        upperArea()
    if path == 3:
        lowerArea()


def goDownChimney():
    if dragonLocation == 'upper':
        print('You climb down into the smokey chimney. The smoke is really thick!... (press enter)')
        input()
        print('The smoke keeps getting thicker. It is getting hard to breathe... (press enter)')
        input()
        print('You have become lost in the smoke, and start coughing. You cannot get any air!... (press enter)')
        input()
        print('ACK! You have suffocated to death! It was kind of dumb to climb into that smokey chimney.')
        return
    if dragonLocation == 'lower':
        print('You climb down the chimney. It seems to lead you somewhere inside the cave.')
        upperArea()


def upperArea():
    print(
        'You are standing in a chamber near the top of the cave. There is a rope ladder to a chimney hole in the ceiling that leads outside.')
    if dragonLocation == 'upper':
        print(
            'The dragon is standing in the chamber! Smoke comes out of his nostrils and floats up and out the hole in the ceiling.')
        pause()
        faceDragon()
    if dragonLocation == 'lower':
        print()
        print('What will you do?')
        print('  1 Climb up and out of the hole.')
        print('  2 Go down to the front of the cave.')
        path = choosePath(2)
        if path == 1:
            topOfCave()
        if path == 2:
            insideOfCave()


def lowerArea():
    print('You are in the lower chamber of the cave. There is a path leading back to the front of the cave.')
    print('This chamber is very large, and there is an underground lake in the chamber. The water is dark and')
    print('murky. You cannot tell how deep it is or what may be in it. In the middle of the lake, you can barely')
    print('see a small island and something on it that is shiny.')
    print()
    if rock == 'present':
        print('There is a large rock near the shore.')
        print('There is a creaky old boat on the shore.')
    if rock == 'sunk':
        print('There is a submerged boat at the bottom of the water near the shore.')
    if rock == 'holding':
        print('There is a creaky old boat on the shore.')
    if rock == 'boat':
        print('There is a creaky old boat on the shore with a large rock in it.')
    print()
    print('What will you do?')
    print('  1 Go to back to the front of the cave.')
    print('  2 Swim the lake to the island.')
    print('  3 Take the creaky old boat to the island.')
    if rock == 'present':
        print('  4 Pick up the large rock.')
    if rock == 'holding':
        print('  4 Put the large rock in the boat.')
    print()
    path = choosePath(4)
    if path == 1:
        front()
        return
    if path == 2:
        swim()
        return
    if path == 3 and rock == 'sunk':
        print('That boat does not look like it is going anywhere.')
        print()
        pause()
        lowerArea()
        return
    if path == 3 and rock != 'sunk':
        rideBoat()
        return
    if path == 4 and rock == 'present':
        takeRock()
        return
    if path == 4 and rock == 'holding':
        putRockInBoat()
        return


def takeRock():
    global rock
    print('You pick up the large rock and put it in your trusty backpack. Ooof! It sure is heavy.')
    inventory.update(stone)
    print()
    pause()
    rock = 'holding'
    lowerArea()


def putRockInBoat():
    global rock
    print('You set the large rock down in the creaky old boat. The boat rocks from side to side, no pun intended.')
    del inventory["Rock"]
    print()
    pause()
    if boat == 'sinks':
        print('The creaky old boat begins to sink under the weight of the rock!')
        print('Whew! It is a good thing you did not try to take that boat to the island.')
        print()
        rock = 'sunk'
        pause()
        lowerArea()
        return
    if boat == 'floats':
        print('The creaky old boat seems to be holding up under the weight of the rock.')
        print()
        rock = 'boat'
        pause()
        lowerArea()
        return


def swim():
    print('You dive into the water. Yipes! It is icy cold!')
    pause()
    if rock == 'holding':
        print(
            'You begin to swim to the island, but the heavy rock you are holding begins to drag you down!... (press enter)')
        input()
        print('ACK! You cannot get the straps off of your backpack!... (press enter)')
        input()
        print('You begin to drown in the murky, dark waters of the underground lake... (press enter)')
        input()
        print('You have drowned! It was kind of dumb to swim the lake with that heavy rock in your backpack.')
        pause()
        return
    if rock != 'holding':
        print('You begin to swim to the island. The island is further away than you thought... (press enter)')
        input()
        print('You are getting tired from all that swimming. You are not sure you can make it... (press enter)')
        input()
        print('All of a sudden a monstrous flying bat appears seemingly out of nowhere and begins flying towards you '
              'at supersonic speed!.. (press enter) ')
        input()
        if player == (warrior):
            print(
                'Although the currents are tough, you are able to use your warrior strength to dive underwater and avoid'
                ' the evil bat! ... (press enter)')
            input()
            print(
                'You finally get to the shore of the island. Whew! You do not think it is a good idea to try that swim again!')
            pause()
            island()
        else:
            print("Oh no, the bat quickly closes the distance and prepares to take a huge bite out of your face!")
            print("What will you do now?")
            print('  1 Stop swimming and prepare to attack!')
            print('  2 Try and avoid the bat by diving underwater')
            path = choosePath(2)
            if path == 1:
                print(
                    "You ready your weapon to fend off the bat, but the current is way too strong for you!.. (press enter)")
                input()
                print(
                    "The rushing current knocks your weapon out of your hands and before you can even reach it, the bat"
                    " dives down and rips your face off. Your world fades to black. (press enter)")
                pause()
                return
            if path == 2:
                print(
                    "You know there's no way you can both swim and fight the monstrous bat so you quickly dive under water.... (presss enter)")
                input()
                print(
                    "However, the rushing current is way too strong for you and you begin to drown in the dark and murky waters... (press enter)")
                input()
                print("Your world fades to black. (press enter)")
                pause()
                return


def rideBoat():
    print('You get into the creaky old boat and begin to row towards the island... (press enter)')
    input()
    print('Half way to the island, you notice that the boat has a small leak!... (press enter)')
    input()
    print('You row faster and faster as the boat slowly begins to sink.... (press enter)')
    input()

    if boat == 'sinks':
        print('The boat is sinking, and you decide you must swim the rest of the way there.')
        pause()
        swim()

    if boat == 'floats':
        print(
            'The boat sinks a bit, but stays afloat. Whew!... (press enter)')
        input()
        print('All of a sudden a monstrous flying bat appears seemingly out of nowhere and begins flying towards you '
              'at supersonic speed!.. (press enter) ')
        input()
        if player == (archer):
            print(
                'Although the bat looks tough, you ready your Elven Bow and fire a mighty arrow into the heart of the evil bat! ... (press enter)')
            input()
            print(
                "A direct hit! The wounded bat falls into the water and is washed away by the powerful current!.. (press enter)")
            input()
            print(
                'With no more enemies in your way, you finally get to the shore of the island,')
            pause()
            island()
        if player == (mage):
            print(
                'Although the bat looks tough, you ready your fire spell and launch a burning fireball at the evil bat! ... (press enter)')
            input()
            print(
                "A direct hit! The burning bat screams out as it's body is disintegrated by your mighty spell!.. (press enter)")
            input()
            print(
                'With no more enemies in your way, you finally get to the shore of the island.')
            pause()
            island()
        if player == (warrior):
            print(
                'You ready your mighty sword in preparation for the demon bat\'s attack, but no attack comes... (press enter)')
            input()
            print('The monstrous bat licks his lips and glares at you with his menacing eyes.'
                  ' Its almost as he knows you can\'t reach him with your sword... (press enter)')
            input()
            print(
                "The bat calls out with a blood-curdling cry and soon more bats begin to circle your small boat... (press enter)")
            input()
            print(
                "The bats dive onto you and despite your great strength as the mighty warrior, you alone are no match for the bats... (press enter)")
            pause()
            print("The bats rip your flesh from your bone and with one last scream, your vision turns black.")
            return


def island():
    print(
        'You are standing on the island in the middle of the underground lake. The shiny glint comes from a large pile of gold and jewels!')
    print('You see there is a rope ladder from the ceiling above the island.')
    pause()
    if dragonLocation == 'upper':
        print('You start putting as much treasure as your backpack can hold.')
        print(
            'You climb the rope ladder, and you see that it leads to a hole in the ceiling that goes outside of the cave.')
        print()
        print('You have escaped from the Dragon Cave with the treasure! Congratulations! You have won the game!')
        pause()
        return
    if dragonLocation == 'lower':
        print('But in front of the treasure is the dragon!')
        pause()
        faceDragon()
        return


def faceDragon():
    global dragonHP
    global hpPotion
    dragonHP = 25
    print()
    print('The dragon is huge! He stands ten feet tall, and has tough green scales and giant claws.')
    print(
        'His leathery wings are folded back over his massive body, and he smiles at you with giant teeth as whisps of smoke come out of his nostrils.')
    pause()
    print('With your trusty weapon is at your side, you remind yourself to breath to steady your composure.')
    print()
    print('The dragon smiles at you, and then speaks...')
    pause()
    print()
    print(
        '"Welcome adventurer. You have come a long way to my cave. Seeking treasure and fortune, are you? Well, I have plenty of it myself."')
    pause()
    print()
    print(
        '"I have spent eons gathering all this material wealth, and yet I no longer have a need for them. However, I only share my hoard of treasure to those I deem worthy."')
    print(
        'The dragon rises from the floor of the cave and makes his way towards you, shaking the cave with each step. The dragon taunts you, "Show me your worth adventurer!"')
    print()
    print('What will you do?')
    print('  1 Fight the massive dragon before you.')
    print('  2 Talk to the dragon. ')
    path = choosePath(2)
    if path == 1:
        print('You ready your weapon and prepare to fight the final boss in your long journey.')
        pause()
        print(
            'The dragon roars out, "I have killed many adventurers like you, what makes you think you can stand a chance?"')
        while dragonHP > 0 and player.hp > 0:
            print("(Press enter to attack)")
            input()
            if player.hp < 7 and hpPotion == 'holding':
                print("Your health is getting low! (Press Enter to use your Health Potion!)")
                input()
                healHP = int(random.randint(3, 6))
                player.hp = player.hp + healHP
                del inventory["Health Potion"]
                hpPotion = 'stolen'
                print("You have healed " + str(healHP) + " HP!")
                print()
                print("(Press enter to attack)")
            fightDragon()
            if dragonHP < 1:
                break
            if player.hp < 1:
                break
    if path == 2:
        print()
        print('You put away your weapon and hold up your hands to the dragon... (press enter)')
        input()
        print('The dragon looks perplexed, yet intrigued. "What is the meaning of this adventurer?"')
        print('What do you say?')
        print('  1 (Persuasion) "I have travelled a long distance to meet you dragon. Please, let us have meaningful dialogue."')
        print('  2 (Intimidate) "I have killed many dragons before you and you will not be the last. Give me your treasure and I will spare your life dragon."')
        print('  3 (Lie) "I am not even here for the treasure, mighty Dragon. I simply got lost on my way back to my village."')
        path = choosePath(3)
        if path == 1:
            print("You dive into a frank and meaningful dialogue with the dragon, validating his right to hoard treasure but not pigeonholing him into a stereotype, \n"
                  "in the hopes of restructuring the traditional adventurer/monster antagonistic relationship into something more positive and mutually beneficial. ")
            pause()
            print("The dragon is moved by your rhetoric. He walks closer to you and invites you you to join him in a brain-storming session about ways to revitalise \n"
                  "the decaying subterranean infrastructure and society of the dungeon.")
            pause()
            print("While the dragon is distracted, do you wish to attack the dragon?")
            print('  1 Yes.')
            print('  2 No, that\'s terrible!')
            path = choosePath(2)
            if path == 1:
                if player == (warrior):
                    print("As the dragon delves deeper into his life story in hopes to create a form of connection with you, you slash his head off in a surprise attack, instantly killing him.")
                if player == (archer):
                    print("As the dragon delves deeper into his life story in hopes to create a form of connection with you, your fire arrows into his heart as a surprise attack, instantly killing him.")
                if player == (mage):
                    print("As the dragon delves deeper into his life story in hopes to create a form of connection with you, you cast a powerful destruction spell on the dragon, instantly killing him.")
                pause()
                print('With the dragon slain, you stuff as much gold and jewels into your trusty backpack as it can hold.')
                print('You have survived the Dragon Cave with enough treasure to retire. Congratulations!')
                print('I hope this victory was worth it to you.')
                return
            if path == 2:
                print("You continue to speak with the dragon for hours about ways to positively change the relationship between dragons and adventurers.")
                print("The dragon, pleased with your companionship, offers you his treasures. He states that he no longer needs it as friendship was the ultimate treasure all along.")
                pause()
                print('With the dragon as your new friend, you stuff as much gold and jewels into your trusty backpack as it can hold.')
                print('You have survived the Dragon Cave with enough treasure to retire. Congratulations!')
                return
        if path == 2:
            print("The Dragon laughs and calls your bluff.")
            print('You ready your weapon and prepare to fight the final boss in your long journey...(press enter)')
            input()
            print(
                'The dragon roars out, "I have killed many adventurers like you, what makes you think you can stand a chance?"')
            while dragonHP > 0 and player.hp > 0:
                print("(Press enter to attack)")
                input()
                if player.hp < 5 and hpPotion == 'holding':
                    print("Your health is getting low! (Press Enter to use your Health Potion)")
                    input()
                    healHP = int(random.randint(2, 5))
                    player.hp = player.hp + healHP
                    del inventory["Health Potion"]
                    hpPotion = 'stolen'
                    print("You have healed " + str(healHP) + " HP!")
                fightDragon()
                if dragonHP < 1:
                    break
                if player.hp < 1:
                    break
        if path == 3:
            print("The dragon laughs at your absurd statement. The whole cave shakes from the sounds of his hearty chuckle...(press enter)")
            input()
            print("You have come a far way adventurer, next time you should make the left at the fork instead of walking into my home.")
            print("Since you have made me laugh the hardest I have laughed in centuries. Have some of my treasure!")
            pause()
            print(
                'With the dragon as your new friend, you stuff as much gold and jewels into your trusty backpack as it can hold.')
            print('You have survived the Dragon Cave with enough treasure to retire. Congratulations!')
            return


def fightDragon():
    global dragonHP
    global combat
    if dragonHP > 0 and player.hp > 0:
        if player == (warrior):
            attack = int(random.randint(-1, 1) + player.dmg)
            dragonHP = dragonHP - attack
            print('You just slash the dragon for ' + str(attack) + ' damage!')
        if player == (archer):
            attack = int(random.randint(-2, 2) + player.dmg)
            dragonHP = dragonHP - attack
            print('You just fired two powerful arrows at the dragon for ' + str(attack) + ' damage!')
        if player == (mage):
            attack = int(random.randint(-5, 1) + player.dmg)
            dragonHP = dragonHP - attack
            print('You just unleashed a powerful spell on the dragon for ' + str(attack) + ' damage!')
        dragonAttack = int(random.randint(-3, 3) + 3)
        player.hp = player.hp - dragonAttack
        if dragonAttack == 0:
            print("The Dragon's attack missed! ")
        else:
            print("The dragon slashed you with his claws for " + str(dragonAttack) + " damage!")
    if player.hp < 1:
        print(
            'The dragon\'s attacks are too strong! He taunts you, "Puny adventurer, you stood no chance against me!" ... (press enter)')
        input()
        print("Your vision fades to black. Game over.")
        return
    if dragonHP < 1:
        print()
        print(
            'After an intense battle, the dragon begins to succumb to his wounds. With a pained breath, he speaks, "Mighty adventurer, you have bested me in combat. You...are...worthy."')
        print(
            'The great dragon falls to the ground, his breathing becoming more labored. You want to say one last thing to him.')
        print()
        print("What do you say?")
        print('  1 Be a gracious adventurer and say something respectful.')
        print('  2 Trash talk and be a dick.')
        path = choosePath(2)
        if path == 1:
            print(
                "You walk up to the dragon and say, 'Mighty Dragon, you have been a fine and worthy adversary. I am humbled to be deemed worthy by you.'")
            print("With one last breath, the dragon smiles faintly and slowly closes his eyes.")
            pause()
            print('With the dragon slain, you stuff as much gold and jewels into your trusty backpack as it can hold.')
            print('You have survived the Dragon Cave with enough treasure to retire. Congratulations!')
            return
        if path == 2:
            print('You yell at the dragon, "GG 2 EZ, git gud scrub" and dab on the poor dragon.')
            pause()
            print('With the dragon slain, you stuff as much gold and jewels into your trusty backpack as it can hold.')
            print('You have survived the Dragon Cave with enough treasure to retire. Congratulations!')
            return


while True:
    # Randomly generate the game variables
    if random.randint(1, 2) == 1:
        dragonLocation = 'upper'
    else:
        dragonLocation = 'lower'

    if random.randint(1, 2) == 1:
        skulls = 'present'
    else:
        skulls = 'absent'

    if random.randint(1, 2) == 1:
        boat = 'sinks'
    else:
        boat = 'floats'

    if random.randint(1, 2) == 1:
        goblin = 'spawn'
    else:
        goblin = 'no'

    rock = 'present'
    hpPotion = 'safe'

    # Start the game
    title_screen()

    print()
    print('Would you like to play again? Y/N')
    playAgain = input()
    if playAgain == 'Y' or playAgain == 'y':
        continue
    if playAgain == 'N' or playAgain == 'n':
        break