import spacy
import requests
import time
import numpy as np
from .getNounsAndVerbs import * 
from .getDefinition import *


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


# text = "Neurogenesis is the process by which new neurons are formed in the brain. Neurogenesis is crucial when an embryo is developing, but also continues in certain brain regions after birth and throughout our lifespan. The mature brain has many specialised areas of function, and neurons that differ in structure and connections. The hippocampus, for example, which is a brain region that plays an important role in memory and spatial navigation, alone has at least 27 different types of neurons. The incredible diversity of neurons in the brain results from regulated neurogenesis during embryonic development. During the process, neural stem cells differentiate—that is, they become any one of a number of specialised cell types—at specific times and regions in the brain."
# print((get_word_and_definitions(text)))
