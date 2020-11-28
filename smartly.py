import spacy
import requests
import time
import numpy as np


_wait = 0.5

def get_freq(term):
    response = None
    while True:
        try:
            response = requests.get('https://api.datamuse.com/words?sp='+term+'&md=f&max=1').json()
        except:
            print('Could not get response. Sleep and retry...')
            time.sleep(_wait)
            continue
        break
    if len(response)==0:
        freq = 0.0
    else:
        freq = float(response[0]['tags'][0][2:])
    return freq


#print(get_freq('fries'))

nlp = spacy.load('en_core_web_sm',disable=['ner','textcat'])

text = "Neurogenesis is the process by which new neurons are formed in the brain. Neurogenesis is crucial when an embryo is developing, but also continues in certain brain regions after birth and throughout our lifespan. The mature brain has many specialised areas of function, and neurons that differ in structure and connections. The hippocampus, for example, which is a brain region that plays an important role in memory and spatial navigation, alone has at least 27 different types of neurons. The incredible diversity of neurons in the brain results from regulated neurogenesis during embryonic development. During the process, neural stem cells differentiate—that is, they become any one of a number of specialised cell types—at specific times and regions in the brain."

doc = nlp(text)

frequencies = []

for token in doc:
    if token.pos_=='NOUN' or token.pos_=='ADJ':
    	frequencies.append(get_freq(token.text))
    	print(token.text, ': ', get_freq(token.text))

std_dev = np.std(frequencies)
mean = np.mean(frequencies)
quartile = np.percentile(frequencies, 25)

important_words = []

# for i in range(len(frequencies)):
# 	if()

print(std_dev)
print(mean)
print(quartile)