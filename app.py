import requests, time, os, io
from os import system


print("Welcome Mirian! How can I help you?")
x = input()
if x == "Translate" or x == "translate":
    os.system('python translatetogeo.py')
if x == "Rhyme" or x == "rhyme":
    os.system("rhymeword.py")
if x == "Search" or x == "search":
    os.system('python searchword.py')
if x == "Number" or x == "number":
    os.system("python searchnumber.py")
if x == "Articles" or x == "articles":
    os.system("python searcharticle.py")



    