import random, time, sys, os, time, winsound
from threading import Thread
from playsound import playsound

stats = [{
    "str stat" : 10,
    "vit stat" : 10,
    "total damage" : 40,
    "total hp" : 100,
    "xp" : 0,
    "level requirement" : 100,
    "statpoint" : 0,
    "player level" : 1,
    "gold" : 0
}]

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
    "longsword" : 5,
    "greatsword" : 10
}]

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

def clear_console():
    command = "clear"
    if os.name in ("nt", "dos"):
        command = "cls"
    os.system(command)

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

def combat():
    if random.randrange(0, 100) < 99:
        random_enemy = random.randint(0, len(wild_enemies) - 1)
        print("You encountered a", wild_enemies[random_enemy]["name"] + "!")
        damaged_enemy = wild_enemies[random_enemy]["hp"]
        damaged_player = stats[0]["total hp"]
        gain_gold = wild_enemies[random_enemy]["gold"]
        while damaged_player > 0 or damaged_enemy > 0:
            action = str(input("\nDo you?\n\nA: Light Attack\nB: Heavy Attack (miss chance: 40%)\nC: Defend\n\nChoose: "))
            if action in answer_A or action in answer_B or action in answer_C:
                if action in answer_A:
                    damaged_enemy = damaged_enemy - stats[0]["total damage"]
                    if damaged_enemy <= 0:
                        print("\nYou attacked the", wild_enemies[random_enemy]["name"], "0 /", wild_enemies[random_enemy]["hp"])
                        play_attack_sound()
                    else:
                        print("\nYou attacked the", wild_enemies[random_enemy]["name"], damaged_enemy, "/", wild_enemies[random_enemy]["hp"])
                        play_attack_sound()
                        damaged_player = damaged_player - wild_enemies[random_enemy]["damage"]
                        if random.randrange(0, 100) > 30:
                            if damaged_player <= 0:
                                print("You were attacked by the", wild_enemies[random_enemy]["name"], "0 /", stats[0]["total hp"])
                                play_hurt_sound
                            else:
                                print("You were attacked by the", wild_enemies[random_enemy]["name"], damaged_player, "/", stats[0]["total hp"])
                                play_hurt_sound()
                        else:
                            print("They missed")
                    if damaged_player <= 0:
                        break
                    elif damaged_enemy <= 0:
                        break
                elif action in answer_B:
                    if random.randrange(0, 100) > 30:
                        damaged_enemy = damaged_enemy - (stats[0]["total damage"] * 1.5)
                        if damaged_enemy <= 0:
                            print("\nYou attacked the", wild_enemies[random_enemy]["name"], "0 /", wild_enemies[random_enemy]["hp"])
                            play_attack_sound()
                        else:
                            print("\nYou attacked the", wild_enemies[random_enemy]["name"], damaged_enemy, "/", wild_enemies[random_enemy]["hp"])
                            play_attack_sound()
                            damaged_player = damaged_player - wild_enemies[random_enemy]["damage"]
                            if random.randrange(0, 100) > 30:
                                if damaged_player <= 0:
                                    print("You were attacked by the", wild_enemies[random_enemy]["name"], "0 /", stats[0]["total hp"])
                                else:
                                    print("You were attacked by the", wild_enemies[random_enemy]["name"], damaged_player, "/", stats[0]["total hp"])
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
            gold = stats[0]["gold"] + wild_enemies[random_enemy]["gold"]
            xp = stats[0]["xp"] + wild_enemies[random_enemy]["xp"]
            print("\nYou defeated the", wild_enemies[random_enemy]["name"])
            print("\n\nXP:", xp, "/", level_requirement)
            if xp >= level_requirement:
                print('YOU LEVELED UP! +2 STAT POINTS')
                stat_change = str(input("Choose what attribute you want make stronger:\n\nA. Strength:\nVitality\n\nChoose: "))
                if stat_change in answer_A or stat_change in answer_B:
                    if stat_change in answer_A:
                        stats[0]["str stat"] += 1
                        stats[0]["total damage"] += 4
                        print("Your damage is now: ", stats[0]["total damage"])
                    elif stat_change in answer_B:
                        stats[0]["vit stat"] += 1
                        stats[0]["total hp"] += 10
                        print("Your hp is now: ", stats[0]["total hp"])
                stats[0]["player level"] += 1
                if stats[0]["player level"] + 1:
                    stats[0]["statpoint"] += 2
                    level_requirement = level_requirement + level_requirement
            stats[0]["gold"] += gain_gold
            print("GOLD: +", gain_gold, "(", stats[0]["gold"], ")")
            play_victory_sound()
    else:
        random_special = random.randint(0, len(special_enemies) - 1)
        print("ALERT, YOU ENCOUNTERED A SPECIAL ENEMY, THE", special_enemies[random_special]["name"] + "!")
        special_enemy_battlemusic()
combat()