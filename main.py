from datamuse import datamuse
from learn_rap_structures import *
import random
api = datamuse.Datamuse()

def main():
    # TODO do the input stuff
    # parse args or something

    num_of_lines = 10
    rap = []
    # topic = "topic"
    # last_word = "word"
    markov_dict = make_markov_dict()
    for count in range(0, num_of_lines):
        sentence = make_sentence(markov_dict)
        rap.append(sentence)
        #last_word = sentence[-1:]
        #topic = new_topic(topic)

    #print rap
    for line in rap:
        print line


# returns a list of words that comprise a sentence
def make_sentence(markov_dict, topic = None, end_rhyme = None, syllables = None):
    sentence = ""
    word = random.choice(markov_dict.keys())
    count = 0
    while word != "\END" and count < 10:
        sentence += " " + word
        word = random.choice(markov_dict[word])
        count += 1
    return sentence

def new_topic(old_topic):
    t = api.words(topics = 'old_topic', max = 10)
