from openai import OpenAI
from bat_thinking import bat_thinking
from clearscr import clear_console

#Calling local AI and formatting message and response using the chat completions api

#structure
# - content
# - refusal
# - role
# - annotations
# - audio
# - function_call
# - tool_calls
# - reasoning


def server_call(ai_url, ai_model, prompt, system_prompt, temp):

    clear_console()
    bat_thinking()

    client = OpenAI(base_url=ai_url, api_key="not_needed") #client call to server

    completion = client.chat.completions.create(
        model=ai_model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature = temp,
    )

#    think = str(completion.choices[0].message.reasoning)#turning the thinking into string
    response = str(completion.choices[0].message.content) #turning response into string


    return response
