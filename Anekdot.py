# -*- coding: utf-8 -*-
import telebot
import requests
import bs4
bot = telebot.TeleBot("1822080825:AAGxDLr0pGRz6bhpRgsSJKR4_3uSBZOHSgw")

def getanekdot():
    z=''
    s=requests.get('http://anekdotme.ru/random')
    b=bs4.BeautifulSoup(s.text, "html.parser")
    p=b.select('.anekdot_text')
    for x in p:
        s=(x.getText().strip())
        z=z+s+'\n\n'
    return s
@bot.message_handler(content_types=["text"])
def handle_text(message):
    msg=message.text
    msg=msg.lower()
    if (u'анекдот' in msg):
        try:
            bot.send_message(message.from_user.id, getanekdot())
        except:
            pass
    else:
        bot.send_message(message.from_user.id, u'Напишите мне слово Анекдот')

bot.polling(none_stop=True, timeout=123)

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.send_message(message.from_user.id, u'Напишите мне слово Анекдот')

bot.polling(none_stop=True, interval=0)