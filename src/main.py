#TODO
#Finish config structure to make configuration easier
#rebuild terminal UI using a TUI like texual
#Using the TUI create a chat box that can be scrolled up and down next to bat. look into better bat animations
#Maybe create a thinking bubble for Bat

#venv is located in venv file under home
#activate it using command: source /home/matt/venv/python/local_ai_friend_env/bin/activate.fish

#calling functions
from localaiservercall import server_call
from bat_ascii import bat_ascii
from printresponse import printresponse
from clearscr import clear_console
from config.config import config

def main():

    #load configuration
    ai_url, ai_model, system_prompt, temp, stream_speed = config()

    #initializing empty response
    response = ""

    while 1 == 1:
        clear_console()
        bat_ascii(True, False, False)
        print(response)

        prompt = input("chat: ")
        clear_console()
        bat_ascii(False, False, True)
        response = server_call(ai_url, ai_model, prompt, system_prompt, temp)

        clear_console()
        bat_ascii(False, True, False)
        printresponse(response, stream_speed)

if __name__ == "__main__":
    main()
