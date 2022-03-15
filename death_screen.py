from playsound import playsound
import os, time

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
death_screen()