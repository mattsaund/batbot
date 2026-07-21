def config():

    ###
    # Main configuration file. DO NOT CHANGE THE VARIABLE NAMES!!!
    # Just change what is in the variable.###

    #AI SETTINGS:

    #String
    ai_url = ""

    #String - Write "not needed" if you dont need an api key
    api_key = "not needed"

    #String
    ai_model = ""

    #String
    system_prompt = "you are a helpfull assistant and you cut to the chase with responses. no filler words. you keep responses short and sweet"

    #Double DEFAULT 0.8
    temperature = 0.8

    ################################################################################################################

    #OUTPUT SETTINGS:

    #Double DEFAULT 0.03
    stream_speed = 0.03

    return ai_url, api_key, ai_model, system_prompt, temperature, stream_speed