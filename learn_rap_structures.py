import requests
from rgenius_vars import *

def make_rgenius_request():
    #returns songs of kendrick lamar
    end_point = "/artists/1421/songs"


    headers = {"Authorization": "Bearer " + rgenius_access_token}

    r = requests.get(url, headers=headers)
    print r.json()["response"]

def rgenius_request_url(end_point, **kwargs):
    base_url = "https://api.genius.com"
    request_url = base_url + end_point
    for k, v in kwargs.iteritems():
        request_url += "?" + k + "=" + v
    return request_url
