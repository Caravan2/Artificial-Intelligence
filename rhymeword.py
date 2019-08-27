import requests, time, os, win32com.client
from os import system

speaker = win32com.client.Dispatch ("SAPI.SpVoice")
speaker.Rate = 3

print("\n" + "\n" + "type a word that you want to find rhyme word of: ")
speaker.Speak ("type a word that you want to find rhyme word of: ")
y = input()
word = y
word = word.rstrip()
url = 'https://api.datamuse.com/words?rel_rhy=%s' % word
r = requests.get(url).json()
try:
    data = r[0]["word"]
    data1 = r[1]["word"]
    data2 = r[2]["word"]
    data3 = r[3]["word"]
    data4 = r[4]["word"]
    data5 = r[5]["word"]
    data6 = r[6]["word"]
    data7 = r[7]["word"]
    alldata = [data, data1, data2, data3, data4, data5, data6, data7]
except IndexError:
    print("")

print(alldata)
speaker.Speak (alldata)
os.system("python app2.py")