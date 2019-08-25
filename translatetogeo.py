import requests, time, os, io
from os import system

print("\n" + "\n" + "type a word that you want to translate: ")
y = input()
word = y
word = word.rstrip()
url = 'https://www.translate.ge/api/%s' % word
print(url)
r = requests.get(url).json()
data = r['rows'][0]['value']['Text']
print(data)
os.system("python app.py")