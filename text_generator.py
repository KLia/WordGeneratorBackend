import json
from words import Words

def generate(event, context):    
    text = event['body-json']['corpus']
    state_size, min_word_len = check_parameters(event)

    w = Words(text, state_size, min_word_len)
    wordlist = []
    for i in range(int(event['body-json']['noOfWords'])):
        word = w.generate_word()
        wordlist += [word]
        print word

    return json.dumps(wordlist)

def check_parameters(event):
    #Check if 'state_size' is passed, otherwise take default
    try:
        state_size = event['body-json']['state_size'] 
    except:
        state_size = 2

    #Check if 'min_word_len' is passed, otherwise take default
    try:
        min_word_len = event['body-json']['min_word_len'] 
    except:
        min_word_len = 2

    return state_size, min_word_len