from django.shortcuts import render, redirect
from django.contrib import messages
import requests
import time
import spacy
import numpy as np

_wait = 0.5


def register(request):
    if request.method == 'POST':

        res = request.POST['input']

        title = HaikalFunction(res)

        context = {
            'title': title,
        }
        return render(request, 'back/showquiz.html', context)
       
    else:
        context = {
            'title': "SmartPy"
        }
        return render(request, 'back/register.html', context)



def get_word_and_definitions(text):
    frequencies = []

    word_freq = get_score_of_NV(text)

    for word in word_freq:
        frequencies.append(word[1])

    std_dev = np.std(frequencies)
    mean = np.mean(frequencies)
    quartile = np.percentile(frequencies, 15)

    important_words = []

    for j in range(len(word_freq)):
        if(word_freq[j][1] < quartile):
            important_words.append(word_freq[j][0])

    word_N_def = []

    for i in important_words:
        word_N_def.append([i, get_definition(i)])

    return word_N_def


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
        for meanings in definition[0]['meanings']:
            for definition in meanings['definitions']:
                definitions.append(definition['definition'])

    return definitions


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


print(get_word_and_definitions("hello you there !"))
