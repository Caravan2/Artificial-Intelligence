import requests, time, os, io
from os import system

print("\n" + "\n" + "type a word that you want to find rhyme word of: ")
y = input()
word = y
word = word.rstrip()
url = 'https://api.datamuse.com/words?rel_rhy=%s' % word
r = requests.get(url).json()
data = r[0]["word"]
data1 = r[1]["word"]
data2 = r[2]["word"]
data3 = r[3]["word"]
data4 = r[4]["word"]
data5 = r[5]["word"]
data6 = r[6]["word"]
data7 = r[7]["word"]
print(data + ", " + data1 + ", " + data2 + ", " + data3 + ", " + data4 + ", " + data5 + ", " + data6 + ", " + data7 + ", ")
os.system("python app.py")