import requests, time, os, win32com.client
from os import system

speaker = win32com.client.Dispatch ("SAPI.SpVoice")
speaker.Rate = 3

print("\n" + "\n" + "type a word that you want me to find: ")
speaker.Speak ("type a word that you want me to find: ")
y = input()
word = y
word = word.rstrip()
url = 'https://googledictionaryapi.eu-gb.mybluemix.net/?define=%s' % word
r = requests.get(url).json()
data = r[0]

def inputer():
    if "origin" in data:
        print("ORIGIN")
    if "noun" in r[0]["meaning"]:
        print("NOUN")
    if "verb" in r[0]["meaning"]:
        print("VERB")
    print("AI")
    print("WHICH ONE WOULD YOU LIKE?")
    speaker.Speak ("which one would you like?")
    z = input()
    if z == "VERB" or z == "verb":
        try:
            if r[0]["meaning"]["verb"][0] is not None:
                print(r[0]["meaning"]["verb"][0]["definition"])
                speaker.Speak (r[0]["meaning"]["verb"][0]["definition"])                
            if r[0]["meaning"]["verb"][1] is not None:
                print(r[0]["meaning"]["verb"][1]["definition"])
                speaker.Speak (r[0]["meaning"]["verb"][1]["definition"])
            if r[0]["meaning"]["verb"][2] is not None:
                print(r[0]["meaning"]["verb"][2]["definition"])
                speaker.Speak (r[0]["meaning"]["verb"][2]["definition"])
            if r[0]["meaning"]["verb"][3] is not None:
                print(r[0]["meaning"]["verb"][3]["definition"])
                speaker.Speak (r[0]["meaning"]["verb"][3]["definition"])
            if r[0]["meaning"]["verb"][4] is not None:
                print(r[0]["meaning"]["verb"][4]["definition"])
                speaker.Speak (r[0]["meaning"]["verb"][4]["definition"])
            if r[0]["meaning"]["verb"][5] is not None:
                print(r[0]["meaning"]["verb"][5]["definition"])
                speaker.Speak (r[0]["meaning"]["verb"][5]["definition"])
        except IndexError:
            print("")
        inputer()
    if z == "NOUN" or z == "noun":
        try:
            if r[0]["meaning"]["noun"][0] is not None:
                print(r[0]["meaning"]["noun"][0]["definition"])
                speaker.Speak (r[0]["meaning"]["noun"][0]["definition"])
            if r[0]["meaning"]["noun"][1] is not None:
                print(r[0]["meaning"]["noun"][1]["definition"])
                speaker.Speak (r[0]["meaning"]["noun"][1]["definition"])
            if r[0]["meaning"]["noun"][2] is not None:
                print(r[0]["meaning"]["noun"][2]["definition"])
                speaker.Speak (r[0]["meaning"]["noun"][2]["definition"])
            if r[0]["meaning"]["noun"][3] is not None:
                print(r[0]["meaning"]["noun"][3]["definition"])
                speaker.Speak (r[0]["meaning"]["noun"][3]["definition"])
            if r[0]["meaning"]["noun"][4] is not None:
                print(r[0]["meaning"]["noun"][4]["definition"])
                speaker.Speak (r[0]["meaning"]["noun"][4]["definition"])
            if r[0]["meaning"]["noun"][5] is not None:
                print(r[0]["meaning"]["noun"][5]["definition"])
                speaker.Speak (r[0]["meaning"]["noun"][5]["definition"])
        except IndexError:
            print("")
        inputer()
    if z == "ORIGIN" or z == "origin":
        try:
            if r[0]["origin"] is not None:
                print(r[0]["origin"])
                speaker.Speak (r[0]["origin"])
        except IndexError:
            print("")
        inputer()
    if z == "AI" or z == "ai":
        os.system("python app2.py")

inputer()