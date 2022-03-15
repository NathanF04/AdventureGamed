import random, time, sys

global str_stat
str_stat = 10
global vit_stat
vit_stat = 10
global total_damage
total_damage = 40
global total_hp
total_hp = 100

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

Greatsword = 40
Longsword = 30
Axe = 20
Dagger = 10

Greatsword, Longsword, Axe, Dagger
items = {
    "Greatsword" : 40,
    "Longsword" : 30,
    "Axe" : 20,
    "Dagger" : 10
}

inventory = {

}

def itemdrop():
    random_drop = random.choice(list(items))
    item_drop = str(input("You found: " + random_drop + "\n\nDo you want to keep it?\n\nA: Yes\nB: No\n\nChoose: "))
    if item_drop in answer_A or item_drop in answer_B:
        if item_drop in answer_A:
            pass
        elif item_drop in answer_B:
            print('You dropped:', random_drop)
    else:
        print("You need to choose between A and B.")

itemdrop()