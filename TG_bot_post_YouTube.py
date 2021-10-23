# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import youtube_dl

import telebot
import re, os, sys, time
import random
import requests
import urllib
from tqdm import tqdm
from urllib import request
from urllib.parse import quote

TOKEN = "" #Токен бота
CHAT_ID = "" # @chanel

search = "видео приколы" #Запрос в ютубе

dir = "/home/Downloads"  #Путь сохранения видео

to_wait = 45 #Перерыв между сообщениями в минутах

def main():

    mylist = [1,2,3,4,5,6,7,8,9,10]

    wait = to_wait * 60

    while True:
        try:
            def findyoutube(x):
                mas = []
                sq = 'http://www.youtube.com/results?search_query=' +quote(x) + "&sp=CAISBggCEAEYAQ%253D%253D"
                doc = urllib.request.urlopen(sq).read().decode('cp1251', errors='ignore')
                match = re.findall("\?v\=(.+?)\"", doc)
                if not(match is None):
                    for ii in match:
                        if(len(ii)<25):
                            mas.append(ii)
                mas=dict(zip(mas,mas)).values()
                mas2=[]
                for y in mas: mas2.append("https://www.youtube.com/watch?v="+y)
                return mas2

            print(u"Видео определенно")

            ydl_opts = {'outtmpl': dir + 'video.mp4'}
            os.chdir(dir)

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([findyoutube(search)[0]])

            print(u"Видео скачано")

            bot = telebot.TeleBot(TOKEN)

            print(u"Видео отправляется на канал")

            url = "https://api.telegram.org/bot" + TOKEN + "/sendVideo";
            files = {'video': open( dir + 'video.mp4', 'rb')}
            data = {'chat_id' : CHAT_ID}

            for i in tqdm(mylist):
                r = requests.post(url, files=files, data=data)

            files = "" #Костыль, его не трогать!

            print(u"Видео отправленно")

            os.system("rm video.mp4")

            print(u"Видео удаленно")

            time.sleep(wait)

            os.system("clear")

        except:
            time.sleep(600.0)

if __name__ == "__main__":
    main()
