import time
import os
import sys
from clearscr import clear_console
    
def bat_idle(i, user_chat_history, batbot_chat_history):

    #clear_console()
    
    terminal_width = os.get_terminal_size().columns
    mouth = "\u23DD"
    c = 0 #local counter

    while c < i:
        print("User")
        print(user_chat_history[c])
        print("Batbot".rjust(terminal_width))
        print(batbot_chat_history[c].rjust(terminal_width))
        c += 1

    print(" _______________ ".rjust(terminal_width))
    print("|               |".rjust(terminal_width))
    print("|               |".rjust(terminal_width))
    print("|   0       0   |".rjust(terminal_width))
    print(f"|      {mouth}        |".rjust(terminal_width))
    print("|_______________|".rjust(terminal_width))
    print("      |   |      ".rjust(terminal_width))
    print("     /|___|\     ".rjust(terminal_width))
    print("       | |       ".rjust(terminal_width))
    print()
    #print(response)

def bat_thinking(thinking, i, user_chat_history, batbot_chat_history):

    #clear_console()

    terminal_width = os.get_terminal_size().columns
    c = 0 #local counter

    while c < i:
        print("User")
        print(user_chat_history[c])
        print("Batbot".rjust(terminal_width))
        print(batbot_chat_history[c].rjust(terminal_width))
        c += 1

    print(" _______________ ".rjust(terminal_width))
    print("|               |".rjust(terminal_width))
    print("|  *            |".rjust(terminal_width))
    print("|   -       -   |".rjust(terminal_width))
    print("|       o       |".rjust(terminal_width))
    print("|_______________|".rjust(terminal_width))
    print("      |   |      ".rjust(terminal_width))
    print("     /|___|\     ".rjust(terminal_width))
    print("       | |       ".rjust(terminal_width))
    print()
    print("Thinking...".rjust(terminal_width))


def bat_talking(stream_speed, i, user_chat_history, batbot_chat_history):

    #clear_console()

    full_response = ""
    mswitch = True
    terminal_width = os.get_terminal_size().columns
    c = 0 #local counter
    
    for char in batbot_chat_history[i]:

        full_response += char

        if len(full_response) % 3 == 0:
            mswitch = not mswitch

        if mswitch:
            mouth = "o"
        else:
            mouth = "-"


        while c <= i:
            print("User")
            print(user_chat_history[c])
            print("Batbot".rjust(terminal_width))
            print(batbot_chat_history[c].rjust(terminal_width))
            c += 1

        if c >= i:
            c = 0

        #print("Batbot".rjust(terminal_width))
        #print(full_response.rjust(terminal_width))
        print(" _______________ ".rjust(terminal_width))
        print("|               |".rjust(terminal_width))
        print("|               |".rjust(terminal_width))
        print("|   0       0   |".rjust(terminal_width))
        print(f"|       {mouth}       |".rjust(terminal_width))
        print("|_______________|".rjust(terminal_width))
        print("      |   |      ".rjust(terminal_width))
        print("     /|___|\     ".rjust(terminal_width))
        print("       | |       ".rjust(terminal_width))
        print()

        time.sleep(stream_speed)
        clear_console()

