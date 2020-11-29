import spacy
import requests
import time
import numpy as np
import getNounsAndVerbs as gf



_wait = 0.5

'''def get_freq(term):
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
    return freq'''


#print(get_freq('fries'))

#nlp = spacy.load('en_core_web_sm',disable=['ner','textcat'])

text = "Neurogenesis is the process by which new neurons are formed in the brain. Neurogenesis is crucial when an embryo is developing, but also continues in certain brain regions after birth and throughout our lifespan. The mature brain has many specialised areas of function, and neurons that differ in structure and connections. The hippocampus, for example, which is a brain region that plays an important role in memory and spatial navigation, alone has at least 27 different types of neurons. The incredible diversity of neurons in the brain results from regulated neurogenesis during embryonic development. During the process, neural stem cells differentiate—that is, they become any one of a number of specialised cell types—at specific times and regions in the brain."
#text ='We can deﬁne similar axioms for belief (often denoted by B) and other modalities. However, one problem with the modal logic approach is that it assumes logical omniscience on the part of agents. That is, if an agent knows a set of axioms, then it knows all consequences of those axioms. This is on shaky ground even for the somewhat abstract notion of knowledge, but it seems even worse for belief, because belief has more connotation of referring to things that are physically represented in the agent, not just potentially derivable. There have been attempts to deﬁne a form of limited rationality for agents; to say that agents believe those assertions that can be derived with the application of no more than k reasoning steps, or no more than s seconds of computation. These attempts have been generally unsatisfactory.'

#doc = nlp(text)

frequencies = []
'''word_freq = []
i = 0

for token in doc:
    if token.pos_=='NOUN' or token.pos_=='ADJ':
    	#frequencies.append(get_freq(token.text))
    	#print(token.text, ': ', get_freq(token.text))
    	if()
    	word_freq.append([token.text, get_freq(token.text)])
    	print(word_freq[i][0], ': ', word_freq[i][1])
    	i += 1
    	
for j in range(len(word_freq)):
	frequencies.append(word_freq[j][1])'''

word_freq = gf.get_score_of_NV(text)

for word in word_freq:
	frequencies.append(word[1])

std_dev = np.std(frequencies)
mean = np.mean(frequencies)
quartile = np.percentile(frequencies, 15)

important_words = []

for j in range(len(word_freq)):
	if(word_freq[j][1] < quartile):
		important_words.append(word_freq[j])

print(std_dev)
print(mean)
print(quartile)
print(important_words)