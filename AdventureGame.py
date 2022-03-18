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
    "name" : "Longsword",
    "str stat" : 10,
    "damage" : 40,
    "price" : 750
},{
    "name" : "Greatsword",
    "str stat" : 20,
    "damage" : 80,
    "drop" : 100
},{
    "name" : "Dagger",
    "str stat" : 5,
    "damage" : 20,
}]

def choose_class():
        class_choice = str(input('Choose between the classes to gain certain attributes: \n\nA: Warrior\n\nStrength: 20\nVitality: 10\n\nB: Tank\n\nStrength: 10\nVitality: 20\n\nC: Maidenless\n\nStrength: 1\nVitality: 10\n\nChoose: '))
        if class_choice in answer_A or class_choice in answer_B:
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
            game()

def inventory():
    inv = {
        "fists" : 0
    }

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


def combat(engage_fight):
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
        print("You encountered a", fighter["name"])
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
                        play_attack_sound()
                    else:
                        print("\nYou attacked the", fighter["name"], damaged_enemy, "/", fighter["hp"])
                        play_attack_sound()
                        damaged_player = damaged_player - fighter["damage"]
                        if random.randrange(0, 100) > 30:
                            if damaged_player <= 0:
                                print("You were attacked by the", fighter["name"], "0 /", stats["total hp"])
                                play_hurt_sound
                            else:
                                print("You were attacked by the", fighter["name"], damaged_player, "/", stats["total hp"])
                                play_hurt_sound()
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
                            play_attack_sound()
                        else:
                            print("\nYou attacked the", fighter["name"], damaged_enemy, "/", fighter["hp"])
                            play_attack_sound()
                            damaged_player = damaged_player - fighter["damage"]
                            if random.randrange(0, 100) > 30:
                                if damaged_player <= 0:
                                    print("You were attacked by the", fighter["name"], "0 /", stats["total hp"])
                                else:
                                    print("You were attacked by the", fighter["name"], damaged_player, "/", stats["total hp"])
                                    play_hurt_sound()
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
            xp = stats["xp"] + fighter["xp"]
            print("\nYou defeated the", fighter["name"])
            print("\n\nXP:", xp, "/", stats["level requirement"])
            if xp >= stats["level requirement"]:
                print('YOU LEVELED UP! +2 STAT POINTS')
                stat_change = str(input("Choose what attribute you want make stronger:\n\nA. Strength:\nVitality\n\nChoose: "))
                if stat_change in answer_A or stat_change in answer_B:
                    if stat_change in answer_A:
                        stats["str stat"] += 1
                        stats["total damage"] += 4
                        print("Your damage is now: ", stats["total damage"])
                    elif stat_change in answer_B:
                        stats["vit stat"] += 1
                        stats["total hp"] += 10
                        print("Your hp is now: ", stats["total hp"])
                stats["player level"] += 1
                if stats["player level"] + 1:
                    stats["statpoint"] += 2
                    stats["level requirement"] += stats["level requirement"]
            stats["gold"] += gain_gold
            print("GOLD: +", gain_gold, "(", stats["gold"], ")")
            play_victory_sound()
    else:
        random_special = random.randint(0, len(special_enemies) - 1)
        print("ALERT, YOU ENCOUNTERED A SPECIAL ENEMY, THE", special_enemies[random_special]["name"] + "!")
        special_enemy_battlemusic()

def movement():    
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
            "west" : "Dungeon Cell"
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
        else:
            print("\n{} was not a choice".format(move.capitalize()))
def game(engage_fight):
    print("You wake up in a unkown dark room stuck in a cell")
    time.sleep(2)
    print("The only thing you remember is your past occupation")
    time.sleep(4)
    print("\nWho are you?\n")
    choose_class()
    print("You look around the cell for something to break out with")
    time.sleep(2)
    print("You find nothing...")
    time.sleep(2)
    print("After a while you find an old lock pick in your pocket")
    time.sleep(2)
    print("\nYou pick the lock and open the cell door")
    time.sleep(2)
    print("However...")
    time.sleep(2)
    print("When you walk towards the door a guard opens it and sees you")
    time.sleep(2)
    print("He takes out his sword and engages in a fight")
    engage_fight += 1
    combat(engage_fight)

game(engage_fight)