import requests, time, os, win32com.client
from os import system

speaker = win32com.client.Dispatch ("SAPI.SpVoice")
speaker.Rate = 3

print("\n" + "\n" + "type a word that you want to translate: ")
speaker.Speak ("type a word that you want to translate: ")
y = input()
word = y
word = word.rstrip()
url = 'https://www.translate.ge/api/%s' % word
print(url)
r = requests.get(url).json()
data = r['rows'][0]['value']['Text']
print(data)
speaker.Speak (data)
os.system("python app2.py")