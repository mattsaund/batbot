def bat_ascii(idle, talking, thinking):


    if idle:
        mouth = "\u23DD"

        print(" _______________")
        print("|               |")
        print("|               |")
        print("|   0       0   |")
        print("|       " + mouth + "       |")
        print("|_______________|")
        print("      |   |")
        print("     /|___|\     ")
        print("       | |")




    elif thinking:
        msg = "Thinking..."

        print(" _______________")
        print("|               |")
        print("|  *            |")
        print("|   -       -   |")
        print("|       o       |")
        print("|_______________|")
        print("      |   |")
        print("     /|___|\     ")
        print("       | |")
        print(msg)


        #talking bat is located in print response