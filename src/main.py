#TODO
#Finish config structure to make configuration easier
#rebuild terminal UI using a TUI like texual
#Using the TUI create a chat box that can be scrolled up and down next to bat. look into better bat animations
#Maybe create a thinking bubble for Bat

#venv is located in venv file under home
#activate it using command: source /home/matt/venv/python/local_ai_friend_env/bin/activate.fish

#calling functions
from localaiservercall import server_call
from bat_idle import bat_idle
from bat_thinking import bat_thinking
from bat_talking import bat_talking
from printresponse import printresponse
from clearscr import clear_console

def main():

    #ai config
    ai_url = "http://10.0.0.248:1234/v1"
    ai_model = "openai/gpt-oss-20b"
    system_prompt = "you are a helpfull assistant and you cut to the chase with responses. no filler words. you keep responses short and sweet"
    temp = 0.8
    response = ""

    #output config
    stream_speed = 0.05


    while 1 == 1:
        clear_console()
        bat_idle()
        print(response)

        prompt = input("chat: ")
        response = server_call(ai_url, ai_model, prompt, system_prompt, temp)

        clear_console()
        bat_talking()
        printresponse(response, stream_speed)


if __name__ == "__main__":
    main()
