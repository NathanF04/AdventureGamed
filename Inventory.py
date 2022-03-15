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

items = [Greatsword, Longsword, Axe, Dagger]
inventory = []

def open_inventory():
    print('Name                Effect')