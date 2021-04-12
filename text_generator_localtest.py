import json
from words import Words

def generate():    
    text = '''car
    cab
    arc
    bar
    bark
    arb
    carb
    pulp
    <span>test</span>'''

    state_size = 2
    minWordLen = 4

    w = Words(text, state_size, minWordLen)
    wordlist = []
    for i in range(50):
        word = w.generate_word()
        wordlist += [word]

    return wordlist



print generate()