import re
from time import sleep
import urllib
import telebot
bot=telebot.Telebot('1422038752:AAHIEkNVXQVgt7_05O3IWniuyLbwLCCoq0A')
import requests as req

url='https://www.youtube.com/results?'
regexp='href=\"/watch\?v=(.{11})'
pattern= re.compile(regexp)

@bot.message_handler(content_types=['text'])
def get(message):
    global url, regexp, pattern
    query_string=urllib.parse.urlencode({"search_query": message.text})
    res = req.get(url+query_string)
    if res.ok:
        body=res.text
        links = pattern.findall(body)[:5]
        for link in links:
            answer = 'https://www.youtube.com/watch?v='+link
            bot.send_message(message.from_user.id, answer)

bot.polling(none_stop=True, interval=0)