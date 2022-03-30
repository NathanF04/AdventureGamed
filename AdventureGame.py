#to run type pip install playsound==1.2.2 in terminal
import random, time, sys, os, time, winsound
from threading import Thread
from playsound import playsound

def clear_console():
    command = "clear"
    if os.name in ("nt", "dos"):
        command = "cls"
    os.system(command)

stats = {
    "str stat" : 10,
    "vit stat" : 10,
    "total damage" : 40,
    "total hp" : 100,
    "xp" : 0,
    "level requirement" : 100,
    "statpoint" : 0,
    "player level" : 1,
    "gold" : 0
}

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

story_enemies = [{
    "name" : "Guard",
    "hp" : 200,
    "damage" : 25,
    "xp" : 300,
    "gold" : 750
},{
    "name" : "Bandit Leader",
    "hp" : 750,
    "damage" : 45,
    "xp" : 1000,
    "gold" : 2000
}]

wild_enemies = [{
    "name" : "Bandit",
    "hp" : 400,
    "damage" : 25,
    "xp" : 100,
    "gold" : 150
},{
    "name" : "Wild Dog",
    "hp" : 100,
    "damage" : 10,
    "xp" : 50,
    "gold" : 50
},{
    "name" : "Thief",
    "hp" : 250,
    "damage" : 30,
    "xp" : 75,
    "gold" : 100
}]
special_enemies = [{
    "name" : "Ogre",
    "hp" : 2000,
    "damage" : 100,
    "xp" : 2000,
    "gold" : 10000
},{
    "name" : "Enchanted knight",
    "hp" : 1250,
    "damage" : 200,
    "xp" : 7500,
    "gold" : 3000
}]

items = [{
    "name" : "Longsword ",
    "str stat" : 10,
    "damage" : 40,
    "effect" : "+40 damage",
    "price" : 750,
    "type" : "Weapon"
},{
    "name" : "Greatsword",
    "str stat" : 20,
    "damage" : 80,
    "effect" : "+80 damage",
    "drop" : 100,
    "type" : "Weapon"
},{
    "name" : "Dagger    ",
    "str stat" : 5,
    "damage" : 20,
    "effect" : "+20 damage",
    "type" : "Weapon"
},{
    "name" : "Chestplate",
    "vit stat" : 10,
    "effect" : "+100 vitality",
    "hp" : 100,
    "price" : 500,
    "type" : "Torso "
}]

inv = []
equip = []

def choose_class():
        class_choice = str(input('Choose between the classes to gain certain attributes: \n\nA: Warrior\n\nStrength: 20\nVitality: 10\n\nB: Tank\n\nStrength: 10\nVitality: 20\n\nC: Maidenless\n\nStrength: 1\nVitality: 10\n\nChoose: '))
        if class_choice in answer_A or class_choice in answer_B or class_choice in answer_C:
            if class_choice in answer_A:
                stats["str stat"] += 10
                #strength is 20 now
                stats["total damage"] += 40
                #damage is 80 now and hp is 100
            elif class_choice in answer_B:
                stats["vit stat"] += 10
                #vitality is 20 now
                stats["total hp"] += 100
                #hitpoints is 200 now and damage is 40
            elif class_choice in answer_C:
                stats["str stat"] -= 9
                #strength is now 1
                stats["vit stat"] -= 5
                #vitality is now 5
                stats["total damage"] -= 30
                #damage is now 10
                stats["total hp"] -= 50
                #hitpoints is now 50
            print("\nCurrent stats:\n\nStrength: {}\nVitality: {}".format(stats["str stat"], stats["vit stat"]))
        else: 
            print('You need to choose between A and B.')
            time.sleep(3)
            clear_console()

def play_victory_sound():
    playsound("VictorySound.wav")

def play_attack_sound():
    playsound("AttackSound.wav")

def play_hurt_sound():
    playsound("HurtSound.mp3")

def special_enemy_battlemusic():
    playsound("Battlemusic.wav")

def death_screen():
    clear_console()
    print(' __     ______  _    _   _____ _____ ______ _____  ')
    print(' \ \   / / __ \| |  | | |  __ \_   _|  ____|  __ \ ')
    print('  \ \_/ / |  | | |  | | | |  | || | | |__  | |  | |')
    print('   \   /| |  | | |  | | | |  | || | |  __| | |  | |')
    print('    | | | |__| | |__| | | |__| || |_| |____| |__| |')
    print('    |_|  \____/ \____/  |_____/_____|______|_____/ ')
    print('                                                   ')
    playsound("deathsound.mp3")

engage_fight = 0
fighter = ""

gained_levels = 0
gained_stats = 0
gained_damage = 0
gained_hp = 0

def combat(engage_fight, gained_levels, gained_stats, gained_damage, gained_hp):
    if engage_fight == 1:
        fighter = story_enemies[0]
    elif engage_fight == 2:
        fighter = story_enemies[1]
    elif engage_fight == 3:
        random_enemy = random.randint(0, len(wild_enemies) - 1)
        fighter = wild_enemies[random_enemy]
    else:
        print("No one to fight?")

    if random.randrange(0, 100) < 99:
        random_enemy = random.randint(0, len(wild_enemies) - 1)
        print("\nYou encountered a", fighter["name"])
        damaged_enemy = fighter["hp"]
        damaged_player = stats["total hp"]
        gain_gold = fighter["gold"]
        while damaged_player > 0 or damaged_enemy > 0:
            action = str(input("\nDo you?\n\nA: Light Attack\nB: Heavy Attack (miss chance: 40%)\nC: Defend\n\nChoose: "))
            if action in answer_A or action in answer_B or action in answer_C:
                if action in answer_A:
                    damaged_enemy = damaged_enemy - stats["total damage"]
                    if damaged_enemy <= 0:
                        print("\nYou attacked the", fighter["name"], "0 /", fighter["hp"])
                        #play_attack_sound()
                    else:
                        print("\nYou attacked the", fighter["name"], damaged_enemy, "/", fighter["hp"])
                        #play_attack_sound()
                        damaged_player = damaged_player - fighter["damage"]
                        if random.randrange(0, 100) > 30:
                            if damaged_player <= 0:
                                print("You were attacked by the", fighter["name"], "0 /", stats["total hp"])
                                #play_hurt_sound
                            else:
                                print("You were attacked by the", fighter["name"], damaged_player, "/", stats["total hp"])
                                #play_hurt_sound()
                        else:
                            print("They missed")
                    if damaged_player <= 0:
                        break
                    elif damaged_enemy <= 0:
                        break
                elif action in answer_B:
                    if random.randrange(0, 100) > 30:
                        damaged_enemy = damaged_enemy - (stats["total damage"] * 1.5)
                        if damaged_enemy <= 0:
                            print("\nYou attacked the", fighter["name"], "0 /", fighter["hp"])
                            #play_attack_sound()
                        else:
                            print("\nYou attacked the", fighter["name"], damaged_enemy, "/", fighter["hp"])
                            #play_attack_sound()
                            damaged_player = damaged_player - fighter["damage"]
                            if random.randrange(0, 100) > 30:
                                if damaged_player <= 0:
                                    print("You were attacked by the", fighter["name"], "0 /", stats["total hp"])
                                else:
                                    print("You were attacked by the", fighter["name"], damaged_player, "/", stats["total hp"])
                                    #play_hurt_sound()
                            else:
                                print("They missed!")
                    else:
                        print("You missed...")
                    if damaged_player <= 0:
                        break
                    elif damaged_enemy <= 0:
                        break
                elif action in answer_C:
                    print("You take out your shield and block the oppononents attack.")
            else:
                print("You need to choose between A, B and C.")
        if damaged_player <= 0:
            clear_console()
            death_screen()
        elif damaged_enemy <= 0:
            gold = stats["gold"] + fighter["gold"]
            stats["xp"] = stats["xp"] + fighter["xp"]
            print("You defeated the", fighter["name"])
            print("\n\nXP:", stats["xp"], "/", stats["level requirement"])
        if stats["xp"] >= stats["level requirement"]:
            while stats["xp"] >= stats["level requirement"]:
                stats["total hp"] = stats["total hp"]
                gained_levels += 1
                gained_stats += 2
                gained_damage += 8
                gained_hp += 20
                stats["xp"] -= stats["level requirement"]
                stats["level requirement"] = stats["level requirement"] * 1.5
            print('YOU GAINED {} LEVELS! +{} STAT POINTS'.format(gained_levels, gained_stats))
            stat_change = str(input("Choose what attribute you want make stronger:\n\nA. Strength:\nB. Vitality\n\nChoose: "))
            if stat_change in answer_A or stat_change in answer_B:
                if stat_change in answer_A:
                    stats["str stat"] += gained_stats
                    stats["total damage"] += gained_damage
                    print("Your damage is now: ", stats["total damage"])
                elif stat_change in answer_B:
                    stats["vit stat"] += gained_stats
                    stats["total hp"] += gained_hp
                    print("Your hp is now: ", stats["total hp"])
            gained_stats -= gained_stats
            gained_levels -= gained_levels
            gained_damage -= gained_damage
            gained_hp -= gained_hp
        else:
            pass
        stats["gold"] += gain_gold
        print("GOLD: +", gain_gold, "(", gold, ")")
        #play_victory_sound()
    else:
        random_special = random.randint(0, len(special_enemies) - 1)
        print("ALERT, YOU ENCOUNTERED A SPECIAL ENEMY, THE", special_enemies[random_special]["name"] + "!")
        special_enemy_battlemusic()

def movement(engage_fight):    
    rooms = {
        "Dungeon Cell" : {
            "name" : "Dungeon Cell",
            "north" : "Dungeon Hallway"
        },
        "Dungeon Hallway" : {
            "name" : "Dungeon Hallway",
            "north" : "Staircase",
            "east" : "Armory",
            "south" : "Dungeon Cell"
        },
        "Armory" : {
            "name" : "Armory",
            "west" : "Dungeon Hallway"
        },
        "Staircase" : {
            "name" : "Staircase",
            "south" : "Dungeon Hallway",
            "go up" : "Dungeon Mainfloor"
        },
        "Dungeon Mainfloor" : {
            "name" : "Dungeon Mainfloor",
            "exit" : "Exit Dungeon",
            "east" : "Dungeon Mainfloor Room 1",
            "west" : "Dungeon Mainfloor Room 2",
            "go down" : "Staircase"
        },
        "Exit Dungeon" : {
            "name" : "Exit Dungeon",
            "north" : "Sign",
            "enter" : "Dungeon Mainfloor",
        },
        "Dungeon Mainfloor Room 1" : {
            "name" : "Dungeon Mainfloor Room 1",
            "west" : "Dungeon Mainfloor"
        },
        "Dungeon Mainfloor Room 2" : {
            "name" : "Dungeon Mainfloor Room 2",
            "east" : "Dungeon Mainfloor"
        },
        "Sign" : {
            "name" : "Sign",
            "east" : "Forest",
            "south" : "Exit Dungeon",
            "west" : "Bandit Camp"
        },
        "Bandit Camp" : {
            "name" : "Bandit Camp",
            "north" : "Bandit House Entrance",
            "east" : "sign"
        },
        "Bandit House Entrance" : {
            "name" : "Bandit House Entrance",
            "enter" : "Bandit House Floor 1",
            "south" : "Bandit Camp"
        },
        "Bandit House Floor 1" : {
            "name" : "Bandit House Floor 1",
            "exit" : "Bandit House Entrance",
            "north" : "Bandit Floor 1 Staircase",
            "east" : "Bandit Floor 1 Room 1",
            "west" : "Bandit Floor 1 Room 2"
        },
        "Bandit House Floor 1 Room 1" : {
            "name" : "Bandit House Floor 1 Room 1",
            "west" : "Bandit House Floor 1"
        },
        "Bandit Floor 1 Room 2" : {
            "name" : "Bandit House Floor 1 Room 2",
            "east" : "Bandit House Floor 1"
        },
        "Bandit Floor 1 Staircase" : {
            "name" : "Bandit House Floor 1 Staircase",
            "go down" : "Bandit House Floor 2",
            "south" : "Bandit House Floor 1"
        },
        "Bandit House Floor 2" : {
            "name" : "Bandit House Floor 2",
            "go up" : "Bandit House Floor 1 Staircase",
            "north" : "Bandit House Floor 2 Bandit Leader Room",
            "east" : "Bandit House Floor 2 Room 1",
            "west" : "Bandit House Floor 2 Room 1"
        },
        "Bandit House Floor 2 Room 1" : {
            "name" : "Bandit House Floor 2 Room 1",
            "west" : "Bandit House Floor 2"
        },
        "Bandit House Floor 2 Room 2" : {
            "name" : "Bandit House Floor 2 Room 2",
            "east" : "Bandit House Floor 2"
        },
        "Bandit House Floor 2 Bandit Leader Room" : {
            "name" : "Bandit House Floor 2 Bandit Leader Room",
            "south" : "Bandit House Floor 2"
        },
        "Forest" : {
            "name" : "Forest",
            "east" : "Village",
            "west" : "Sign"
        },
        "Village" : {
            "name" : "Village",
            "north" : "Village Plaza",
            "west" : "Forest"
        },
        "Village Plaza" : {
            "name" : "Village Plaza",
            "north" : "Villager Quest",
            "east" : "Shop",
            "south" : "Village"
        },
        "Shop" : {
            "name" : "Shop",
            "west" : "Village Plaza"
        },
        "Villager Quest" : {
            "name" : "Villager Quest",
            "south" : "Village Plaza"
        }
    }
    directions = ["north", "east", "south", "west", "go up", "go down", "enter", "exit"]
    current_room = "Dungeon Cell"
    drop_chance = random.randrange(0, 100)

    while True:
        print("\nYou are in the {}.".format(current_room))
        print("\nWhere do you want to move?\n")
        if "north" in rooms[current_room]:
            print("North - {}".format(rooms[current_room]["north"])) 
        if "east" in rooms[current_room]:
            print("East - {}".format(rooms[current_room]["east"]))
        if "south" in rooms[current_room]:
            print("South - {}".format(rooms[current_room]["south"]))
        if "west" in rooms[current_room]:
            print("West - {}".format(rooms[current_room]["west"])) 
        if "go up" in rooms[current_room]:
            print("Go up - {}".format(rooms[current_room]["go up"]))
        if "go down" in rooms[current_room]:
            print("Go down - {}".format(rooms[current_room]["go down"]))
        if "enter" in rooms[current_room]:
            print("Enter - {}".format(rooms[current_room]["enter"])) 
        if "exit" in rooms[current_room]:
            print("Exit - {}".format(rooms[current_room]["exit"]))
        move = input("\nChoose: ")
        if move in rooms[current_room]:
            current_room = rooms[current_room][move]
            if "Armory" in current_room:
                engage_fight += 3
                combat(engage_fight, gained_levels, gained_stats, gained_damage, gained_hp)
                engage_fight -= 3
                if drop_chance > 30:
                    print("You found a chestplate!")
                    inv.append(3)
                    inventory(inv, equip)
                else:
                    print("You might want to come back later....")
                #do_what()
            elif "Dungeon Mainfloor" in current_room:
                engage_fight += 3
                combat(engage_fight, gained_levels, gained_stats, gained_damage, gained_hp)
                engage_fight -= 3
                #do_what()
            elif "Dungeon Mainfloor Room 1" in current_room:
                engage_fight += 3
                combat(engage_fight, gained_levels, gained_stats, gained_damage, gained_hp)
                engage_fight -= 3
                #do_what()
            elif "Dungeon Mainfloor Room 2" in current_room:
                engage_fight += 3
                combat(engage_fight, gained_levels, gained_stats, gained_damage, gained_hp)
                engage_fight -= 3
                #do_what()
        else:
            print("\n{} was not a choice".format(move.capitalize()))

def inventory(inv, equip):
    tal = 1
    print("\n   Name:            Type:            Damage:            ")
    
    for i in range(0, len(inv)):
        print("{}. {}       {}           {}".format(tal, items[inv[i]]["name"],items[inv[i]]["type"],items[inv[i]]["effect"]))
        if len(inv) > 0:
            tal += 1
        else:
            pass
    tal = 1
    while True:
        do_what_inv = input("\nWhat do you want to do?\n\nA. Equip\nB. Unequip\nC. Exit Inventory\n\nChoose: ")
        if do_what_inv in answer_A or do_what_inv in answer_B or do_what_inv in answer_C:
            if do_what_inv in answer_A:
                length_inv = len(inv) - 1
                print("What do you want to equip? (0-{})".format(length_inv))
                choose_equip = int(input("Choose: "))
                if "Weapon" in equip:
                    print("\nYou already have a weapon equipped, unequip to equip.")
                if "Torso " in equip:
                    print("\nYou already have a torso equipped, unequip to equip.")
            elif do_what_inv in answer_B:
                pass
            elif do_what_inv in answer_C:
                do_what()
        else:
            print("Choose between A, B and C")
def game(engage_fight, inv):
    print("You wake up in a unkown dark room stuck in a cell")
    #time.sleep(2)
    print("The only thing you remember is your past occupation")
    #time.sleep(4)
    print("\nWho are you?\n")
    choose_class()
    print("You look around the cell for something to break out with")
    #time.sleep(2)
    print("You pick up a dagger\n")
    equip_weapon = str(input("Do you want to equip it?\n\nA. Yes\nB. No\n\nChoose: "))
    if equip_weapon in answer_A or equip_weapon in answer_B:
        if equip_weapon in answer_A:
            stats["total damage"] += items[2]["damage"]
            print("\n{}".format(items[2]["effect"]))
            inv.append(2)
            inv.append(1)
            equip.append(items[2]["type"])
            inventory(inv, equip)
        elif equip_weapon in answer_B:
            print("...")
    #time.sleep(2)
    print("\nAfter a while you find an old lock pick in your pocket")
    #time.sleep(2)
    print("\nYou pick the lock and open the cell door")
    #time.sleep(2)
    print("However...")
    #time.sleep(2)
    print("When you walk towards the door a guard opens it and sees you")
    #time.sleep(2)
    print("He takes out his sword and engages in a fight")
    engage_fight += 1
    combat(engage_fight, gained_levels, gained_stats, gained_damage, gained_hp)
    engage_fight -= 1
    #time.sleep(2)
    print("\nTime to move on")

def do_what():
    do_choice = str(input("What do you want to do?\n\nA. Move\nB. Check inventory\nC. Check stats\n\nChoose: "))
    if do_choice in answer_A or do_choice in answer_B or do_choice in answer_C:
        if do_choice in answer_A:
            movement(engage_fight)
        elif do_choice in answer_B:
            inventory(inv, equip)
            do_what()
        elif do_choice in answer_C:
            print("\nStrength: {}".format(stats["str stat"]))
            print("Vitality: {}".format(stats["vit stat"]))
            do_what()
    else:
        print("Choose between A, B and C")
        do_what()

game(engage_fight, inv)
do_what()

#add chance of finding chestplate in armory