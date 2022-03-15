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

def choose_class():
    class_choice = str(input('Choose between the classes to gain certain attributes: \n\nA: Warrior\n\nStrength: 20\nVitality: 10\n\nB: Tank\n\nStrength: 10\nVitality: 20\n\nC: Maidenless\n\nStrength: 1\nVitality: 10\n\nChoose: '))
    if class_choice in answer_A or class_choice in answer_B:
        if class_choice in answer_A:
            global str_stat
            str_stat = str_stat + 10
            #strength is 20 now
            total_damage = total_damage + 40
            #damage is 80 now and hp is 100
        elif class_choice in answer_B:
            global vit_stat
            vit_stat = vit_stat + 10
            #vitality is 20 now
            global total_hp
            total_hp = total_hp + 100
            #hitpoints is 200 now and damage is 40
        elif class_choice in answer_C:
            str_stat = str_stat - 9
            #strength is now 1
            vit_stat = vit_stat - 5
            #vitality is now 5
            total_damage = total_damage - 30
            #damage is now 10
            total_hp = total_hp - 50
            #hitpoints is now 50

    else: 
        print('You need to choose between A and B.')
        choose_class()

choose_class()