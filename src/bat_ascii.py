import time
import os
import sys
from clearscr import clear_console

def bat_ascii(idle, thinking, talking, response, stream_speed):


    if idle:
        msg = response
        mouth = "\u23DD"

        print(" _______________ ")
        print("|               |")
        print("|               |")
        print("|   0       0   |")
        print("|       " + mouth + "       |")
        print("|_______________|")
        print("      |   |      ")
        print("     /|___|\     ")
        print("       | |       ")
        print(msg)



    elif thinking:
        msg = "Thinking..."

        print(" _______________ ")
        print("|               |")
        print("|  *            |")
        print("|   -       -   |")
        print("|       o       |")
        print("|_______________|")
        print("      |   |      ")
        print("     /|___|\     ")
        print("       | |       ")
        print(msg)

    elif talking:

        full_response = ""
        mswitch = True

        for char in response:

            full_response += char

            if len(full_response) % 3 == 0:
                mswitch = not mswitch

            if mswitch:
                mouth = "o"
            else:
                mouth = "-"

            print(" _______________ ")
            print("|               |")
            print("|               |")
            print("|   0       0   |")
            print(f"|       {mouth}       |")
            print("|_______________|")
            print("      |   |      ")
            print("     /|___|\     ")
            print("       | |       ")

            print(full_response)
            time.sleep(stream_speed)
            clear_console()

        #talking bat is located in printresponse.py