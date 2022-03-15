import random, time, sys

global str_stat
str_stat = 5
global vit_stat
vit_stat = 5

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

def cell():
    print("You wake up in a dark cell in what looks like a basement.")
    #time.sleep(2)
    print("The only things you remember is being attacked by a group of bandits.")
    #time.sleep(2)
    print("Everything that you had on you has been taken away from you except a lockpick.")
    #time.sleep(2)
    cell_choice = str(input("\nDo you?\n\nA: Pick the lock\nB: Wait and die\n\nChoose: "))
    if cell_choice in answer_A or cell_choice in answer_B:
        if cell_choice in answer_A:
            print('You broke out.')
        elif cell_choice in answer_B:
            print('\n2 hours later...')
            #time.sleep(2)
            print('A guard does a daily check up on you.')
            #time.sleep(2)
            cell_guard_choice = str(input('\nDo you?\n\nA: Fake your death\nB: Starve to death\n\nChoose: '))
            if cell_guard_choice in answer_A or cell_guard_choice in answer_B:
                if cell_guard_choice in answer_A:
                    print('You fake your death and the guard reacts immediately.')
                    #time.sleep(2)
                    print('He opens the cell door and checks on your condition.')
                    #time.sleep(2)
                    print('You attack him and subdue him.')
                    #time.sleep(2)
                    print('You take this weapon and keys.')
                elif cell_guard_choice in answer_B:
                    #time.sleep(2)
                    sys.exit('\nYou died bozo')
                    
    else: 
        print('You need to choose between A and B.')