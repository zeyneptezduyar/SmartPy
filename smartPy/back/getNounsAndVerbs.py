# import spacy
import spacy
from .wordScore import *

def get_score_of_NV(text):
    wordFreq = []
    i = 0

    # load english language model
    nlp = spacy.load('en_core_web_sm', disable=['ner','textcat'])

    # create spacy 
    doc = nlp(text)

    for token in doc:
        if token.pos_=='NOUN' or token.pos_=='ADJ':
        	freq = get_freq(token.text)
        	if([token.text.lower(), freq] not in wordFreq):
        		wordFreq.append([token.text.lower(), freq])
        	i += 1

    return wordFreq

# print(get_score_of_NV("Neurogenesis is the process by which new neurons are formed in the brain. Neurogenesis is crucial when an embryo is developing, but also continues in certain brain regions after birth and throughout our lifespan. The mature brain has many specialised areas of function, and neurons that differ in structure and connections. The hippocampus, for example, which is a brain region that plays an important role in memory and spatial navigation, alone has at least 27 different types of neurons. The incredible diversity of neurons in the brain results from regulated neurogenesis during embryonic development. During the process, neural stem cells differentiate—that is, they become any one of a number of specialised cell types—at specific times and regions in the brain."))