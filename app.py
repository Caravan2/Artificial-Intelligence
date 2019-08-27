import requests, time, os, win32com.client
from os import system

speaker = win32com.client.Dispatch ("SAPI.SpVoice")
speaker.Rate = 3
speaker.Voice = speaker.GetVoices("Name=Microsoft Zira").Item(1)

print("Welcome Mirian! It's your AI: " + "\n 1)Translate" + "\n 2)Rhyme" + "\n 3)Word" + "\n 4)Number" + "\n 5)Articles")
speaker.Speak ("Welcome Mirian! It's your Artificial Intelligence: For this moment I can translate, find a rhyme of a word, find a definition of a word, find the owner of a number and find some articles. Which one would you like?")
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
    os.system("python app.py")


    