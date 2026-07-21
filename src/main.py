#TODO
#Finish config structure to make configuration easier
#rebuild terminal UI using a TUI like texual
#Using the TUI create a chat box that can be scrolled up and down next to bat. look into better bat animations
#Maybe create a thinking bubble for Bat

#venv is located in venv file under home
#activate it using command: source /home/matt/venv/python/batbot_venv/bin/activate.fish

#TO RUN IN TERMINAL: /home/matt/.venv/python/batbot_venv/bin/python main.py

#calling functions
from localaiservercall import server_call
import output
from config.config import config
from clearscr import clear_console

def main():

    #load configuration
    ai_url, api_key, ai_model, system_prompt, temp, stream_speed = config()

    #initializing empty response and think
    think = ""

    #init chat histories
    user_chat_history = []
    batbot_chat_history = []

    #init chat history loop
    i = 0

    while 1 == 1:

        clear_console()
        output.bat_idle(i, user_chat_history, batbot_chat_history)

        prompt = input("chat: ")
        user_chat_history.append(prompt)

        #####################################################################

        clear_console()
        output.bat_thinking(think, i, user_chat_history, batbot_chat_history)

        response = server_call(ai_url, api_key, ai_model, prompt, system_prompt, temp)
        batbot_chat_history.append(response)

        #####################################################################

        clear_console()
        output.bat_talking(stream_speed, i, user_chat_history, batbot_chat_history)
        i += 1

if __name__ == "__main__":
    main()
