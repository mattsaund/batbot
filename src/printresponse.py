import time
import os
import sys
from clearscr import clear_console

def printresponse(response, stream_speed):

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

###OLD
#       #sys.stdout.write(char)
        #sys.stdout.flush()
        #time.sleep(stream_speed)###

