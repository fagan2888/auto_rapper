from datamuse import datamuse
import requests
from rgenius_vars import *
api = datamuse.Datamuse()

url = "https://api.genius.com/songs/378195"
headers = {"Authorization": "Bearer " + rgenius_access_token}
r = requests.get(url, headers=headers)
print r.json()["response"]

def main():
    # TODO do the input stuff
    # parse args or something

    num_of_lines = 10
    topic = "topic"
    last_word = "word"
    while num_of_lines:
        sentence = make_sentence(topic, last_word)
        last_word = sentence[-1:]
        topic = new_topic(topic)
        num_of_lines -= 1


# returns a list of words that comprise a sentence
def make_sentence(topic, end_rhyme, syllables = None):
    returns

def new_topic(old_topic):
    t = api.words(topics = 'old_topic', max = 10)
