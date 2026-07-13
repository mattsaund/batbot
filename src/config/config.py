
def config():

    ###
    # Main configuration file. DO NOT CHANGE THE VARIABLE NAMES!!!
    # Just change what is in the variable.###

    #AI SETTINGS:

    #String
    ai_url = "http://10.0.0.248:1234/v1"

    #String
    ai_model = "openai/gpt-oss-20b"

    #String
    system_prompt = "you are a helpfull assistant and you cut to the chase with responses. no filler words. you keep responses short and sweet"

    #Double
    temperature = 0.8

    ################################################################################################################

    #OUTPUT SETTINGS:

    #Double
    stream_speed = 0.03

    return ai_url, ai_model, system_prompt, temperature, stream_speed