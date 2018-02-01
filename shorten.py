import requests
import json
from data import google_key

headers = {'Content-type':'application/json'}

def shorten(s):
    r = requests.post("https://www.googleapis.com/urlshortener/v1/url?key="+google_key,
                      data = json.dumps({"longUrl":s}),
                      headers={'Content-type':'application/json'})
    json_data = json.loads(r.text)
    return json_data.get('id')