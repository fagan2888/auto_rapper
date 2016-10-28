import requests
from rgenius_vars import *
from bs4 import BeautifulSoup
import re

def make_markov_dict():
    song_to_lyrics = make_song_to_lyrics_dict()
    markov_dict = {}
    for song in song_to_lyrics:
        lyrics = song_to_lyrics[song]
        for line in lyrics:
            for i_word in range(0, len(line)):
                curWord = line[i_word]
                nextWord = "\END"
                if i_word + 1 < len(line):
                    nextWord = line[i_word + 1]

                if curWord not in markov_dict:
                    markov_dict[curWord] = []
                markov_dict[curWord].append(nextWord)

    for word in markov_dict:
        print word
        print markov_dict[word]
    #return markov_dict


def make_song_to_lyrics_dict():
    #returns songs of kendrick lamar
    base_url = "https://api.genius.com"
    end_point = "/artists/1421/songs?sort=popularity&per_page=5"
    url = base_url + end_point
    headers = {"Authorization": "Bearer " + rgenius_access_token}
    r = requests.get(url, headers=headers)
    json = r.json()
    songs = json["response"]["songs"]
    song_to_path = {}
    for song in songs:
        title = song["full_title"]
        path = song["path"]
        song_to_path[title] = path

    song_to_lyrics = {}
    for title in song_to_path:
        path = song_to_path[title]
        lyrics = scrape_and_clean_lyrics(path)
        song_to_lyrics[title] = lyrics
    return song_to_lyrics

#TODO remove the lines that correspond to album tracks etc.
def scrape_and_clean_lyrics(path):
    #scraping lyrics from rapgenius
    page_url = "http://genius.com" + path
    page = requests.get(page_url)
    html = BeautifulSoup(page.text, "html.parser")
    lyrics = html.find("lyrics").text

    #remove ascii characters
    lyrics = re.sub(r"[^\x00-\x7F]+","", lyrics)
    #remove extra characters
    lyrics = re.sub(r"[.,\'!_?\"-:;]+","", lyrics)
    lyrics = str(lyrics)
    lyrics = lyrics.split("\n")

    clean_lyrics = []
    #clean the lyrics
    for lyric in lyrics:
        if is_valid_line(lyric):
            #remove parenthesis that are in the middle of the line
            lyric = re.sub(r"[()]+","", lyric)
            lyric = lyric.split(" ")
            clean_lyrics.append(lyric)
    return clean_lyrics

def is_valid_line(lyric):
    if not lyric:
        return False
    if "[" in lyric or "]" in lyric:
        return False
    if "{" in lyric or "}" in lyric:
        return False

    # this removes background voices
    if "(" == lyric[0] and ")" == lyric[-1]:
        return False
    return True

def rgenius_request_url(end_point, **kwargs):
    base_url = "https://api.genius.com"
    request_url = base_url + end_point
    for k, v in kwargs.iteritems():
        request_url += "?" + k + "=" + v
    return request_url
