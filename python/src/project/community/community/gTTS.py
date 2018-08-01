from gtts import gTTS
from community.type import json_item

items = list(json_item().item)
title_item = []

for i in range(1,11):
   # title_item = (items[i])['title']
    title_item.append('number' + str(i))
    title_item.append((items[i])['title'])
    print(title_item)
    tts_en = gTTS(str(title_item), lang='en')
    tts_ko = gTTS(str(title_item), lang='ko')

tts_en.save('title(en).mp3')
tts_ko.save('title(ko).mp3')


