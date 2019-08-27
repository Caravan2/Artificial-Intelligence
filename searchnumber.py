import requests, time, os, win32com.client
from os import system

speaker = win32com.client.Dispatch ("SAPI.SpVoice")
speaker.Rate = 3

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def parser():
    print("type the number you want me to find")
    speaker.Speak ("type the number you want me to find")
    number = input()
    r = requests.post("https://simpleapi.info/apps/numbers-info/info.php?log_note=nomrebi.com", data={"number": number}, headers=headers )
    data = r.content
    print(data)
    speaker.Speak (data)
    os.system("python app2.py")
parser()

