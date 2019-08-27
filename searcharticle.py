import requests, time, os, win32com.client, webbrowser
from os import system

speaker = win32com.client.Dispatch ("SAPI.SpVoice")
speaker.Rate = 3

print("\n" + "\n" + "type a word that you want me to find: ")
speaker.Speak ("type a word that you want me to find: ")
y = input()
word = y
word = word.rstrip()
url = "http://eventregistry.org/api/v1/article/getArticles?articleBodyLen=300&articlesCount=48&includeArticleImage=true&includeArticleShares=true&includeArticleSentiment=true&titleType=news&query=%7B%22$query%22:%7B%22keyword%22:%22" + word + "%22,%22keywordSearchMode%22:%22simple%22%7D,%22$filter%22:%7B%22forceMaxtitleTimeWindow%22:%2231%22,%22startSourceRankPercentile%22:0,%22endSourceRankPercentile%22:100%7D%7D&resultType=articles&articlesConceptLang=eng&articlesSortBy=fq&includeArticleConcepts=true&articlesPage=1"
r = requests.get(url).json()
try:
    title0 = r["articles"]["results"][0]["title"] + " - " + r["articles"]["results"][0]["dateTime"]
    title1 = r["articles"]["results"][1]["title"] + " - " + r["articles"]["results"][1]["dateTime"]
    title2 = r["articles"]["results"][2]["title"] + " - " + r["articles"]["results"][2]["dateTime"]
    title3 = r["articles"]["results"][3]["title"] + " - " + r["articles"]["results"][3]["dateTime"]
    title4 = r["articles"]["results"][4]["title"] + " - " + r["articles"]["results"][4]["dateTime"]
    title5 = r["articles"]["results"][5]["title"] + " - " + r["articles"]["results"][5]["dateTime"]
    title6 = r["articles"]["results"][6]["title"] + " - " + r["articles"]["results"][6]["dateTime"]
    title7 = r["articles"]["results"][7]["title"] + " - " + r["articles"]["results"][7]["dateTime"]
    title8 = r["articles"]["results"][8]["title"] + " - " + r["articles"]["results"][8]["dateTime"]
    title9 = r["articles"]["results"][9]["title"] + " - " + r["articles"]["results"][9]["dateTime"]

    body0 = r["articles"]["results"][0]["body"]
    body1 = r["articles"]["results"][1]["body"]
    body2 = r["articles"]["results"][2]["body"]
    body3 = r["articles"]["results"][3]["body"]
    body4 = r["articles"]["results"][4]["body"]
    body5 = r["articles"]["results"][5]["body"]
    body6 = r["articles"]["results"][6]["body"]
    body7 = r["articles"]["results"][7]["body"]
    body8 = r["articles"]["results"][8]["body"]
    body9 = r["articles"]["results"][9]["body"]

    url0 = r["articles"]["results"][0]["url"]
    url1 = r["articles"]["results"][1]["url"]
    url2 = r["articles"]["results"][2]["url"]
    url3 = r["articles"]["results"][3]["url"]
    url4 = r["articles"]["results"][4]["url"]
    url5 = r["articles"]["results"][5]["url"]
    url6 = r["articles"]["results"][6]["url"]
    url7 = r["articles"]["results"][7]["url"]
    url8 = r["articles"]["results"][8]["url"]
    url9 = r["articles"]["results"][9]["url"]
except IndexError:
    os.system("python app.py")
print("1) " + title0 + "\n" + "2) " + title1 + "\n" + "3) " + title2 + "\n" + "4) " + title3 + "\n" + "5) " + title4 + "\n" + "6) " + title5 + "\n" + "7) " + title6 + "\n" + "8) " + title7 + "\n" + "9) " + title8 + "\n" + "10) " + title9)
speaker.Speak ("Here are the titles of recently added articles in the web space")
def articles():
    print("\n" + "If you want to learn more write a number of article")
    speaker.Speak ("If you want to learn more write a number of article")
    z = input()
    if z == "1":
        print(body0)
        speaker.Speak (body0)
    if z == "2":
        print(body1)
        speaker.Speak (body1)
    if z == "3":
        print(body2)
        speaker.Speak (body2)
    if z == "4":
        print(body3)
        speaker.Speak (body3)
    if z == "5":
        print(body4)
        speaker.Speak (body4)
    if z == "6":
        print(body5)
        speaker.Speak (body5)
    if z == "7":
        print(body6)
        speaker.Speak (body6)
    if z == "8":
        print(body7)
        speaker.Speak (body7)
    if z == "9":
        print(body8)
        speaker.Speak (body8)
    if z == "10":
        print(body9)
        speaker.Speak (body9)
    print("if you want me to open a website type yes or type ai")
    speaker.Speak ("if you want me to open a website type yes or type ai")
    w = input()
    if w == "Yes" or w == "yes":
        speaker.Speak ("Opening a website")
        url = r["articles"]["results"][int(z)-1]["url"]
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
        os.system("python app2.py")
    else:
        os.system("python app2.py")
articles()