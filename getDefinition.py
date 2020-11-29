import requests
import time

_wait = 0.5

def get_definition(word):
    while True:
        try:
            response = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/'+word).json()
        except:
            print('Could not get response. Sleep and retry...')
            time.sleep(_wait)
            continue
        break

    definitions = []
    if len(response)==0:
        definition = ""
    else:
        definition = response
        error = {"title":"No Definitions Found","message":"Sorry pal, we couldn't find definitions for the word you were looking for.","resolution":"You can try the search again at later time or head to the web instead."}
        if(definition != error):
            for meanings in definition[0]['meanings']:
                for definition in meanings['definitions']:
                    definitions.append(definition['definition'])

    return definitions

# print(get_definition("brachii"))