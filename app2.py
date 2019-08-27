import requests, time, os, win32com.client
from os import system

speaker = win32com.client.Dispatch ("SAPI.SpVoice")
speaker.Rate = 3


print("What should I do next?")
speaker.Speak ("what should I do next?")
x = input()
if x == "Translate" or x == "translate":
    speaker.Speak ("All right")
    os.system('python translatetogeo.py')
elif x == "Rhyme" or x == "rhyme":
    speaker.Speak ("All right")
    os.system("rhymeword.py")
elif x == "Search" or x == "search":
    speaker.Speak ("All right")
    os.system('python searchword.py')
elif x == "Number" or x == "number":
    speaker.Speak ("All right")
    os.system("python searchnumber.py")
elif x == "Articles" or x == "articles":
    speaker.Speak ("All right")
    os.system("python searcharticle.py")
else:
    speaker.Speak ("Unfortunately I can't do that")
    os.system("python app2.py")