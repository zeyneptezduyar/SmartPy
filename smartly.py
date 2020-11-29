import spacy
import requests
import time
import numpy as np
import getNounsAndVerbs as gf
import getDefinition as gd


def get_word_and_definitions(text):
    frequencies = []

    word_freq = gf.get_score_of_NV(text)

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
    	print(i)
    	word_N_def.append([i, gd.get_definition(i)])

    return word_N_def


# text = "Neurogenesis is the process by which new neurons are formed in the brain. Neurogenesis is crucial when an embryo is developing, but also continues in certain brain regions after birth and throughout our lifespan. The mature brain has many specialised areas of function, and neurons that differ in structure and connections. The hippocampus, for example, which is a brain region that plays an important role in memory and spatial navigation, alone has at least 27 different types of neurons. The incredible diversity of neurons in the brain results from regulated neurogenesis during embryonic development. During the process, neural stem cells differentiate—that is, they become any one of a number of specialised cell types—at specific times and regions in the brain."
text = 'The radial nerve, which is from the fifth cervical spinal nerve to the first thoracic spinal nerve, originates as the continuation of the posterior cord of the brachial plexus. This nerve enters the lower triangular space (an imaginary space bounded by, amongst others, the shaft of the humerus and the triceps brachii) of the arm and lies deep to the triceps brachii. Here it travels with the deep artery of the arm, which sits in the radial groove of the humerus. This fact is very important clinically as a fracture of the shaft of the bone here can cause lesions or even transections in the nerve.'
print((get_word_and_definitions(text)))
