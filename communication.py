import requests
import json
from time import sleep
import shutil
import playaudio

def get_audio(id):
    url = f"https://play.ht/api/v1/articleStatus?transcriptionId={id}"

    headers = {
        "accept": "application/json",
        "AUTHORIZATION": "92c24db85b264d0486f4389e02b5ca71",
        "X-USER-ID": "cv1rSYAb7DgkE2OPosbaEoPHsgY2"
    }

    response = requests.get(url, headers=headers)
    sleep(3)
    json_object_audio = json.loads(response.text)
    sleep(2)
    r = requests.get(json_object_audio["audioUrl"], stream=True)
    #print(r)

    if r.status_code == 200:
        with open(r"C:\Users\emanu\Documents\Projetos\NinaGPT\audiotemp\id2.mp3", 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)

    playaudio.playaudio(r"C:\Users\emanu\Documents\Projetos\NinaGPT\audiotemp\id2.mp3")
    #print(response.text)

def create_audio(sentence):
    payload = {
        "content": [sentence],
        "voice": "Matilde",
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "AUTHORIZATION": "92c24db85b264d0486f4389e02b5ca71",
        "X-USER-ID": "cv1rSYAb7DgkE2OPosbaEoPHsgY2"
    }

    url = "https://play.ht/api/v1/convert"

    response = requests.post(url, json=payload, headers=headers)
    sleep(1)
    json_object = json.loads(response.text)

    get_audio(json_object["transcriptionId"])
