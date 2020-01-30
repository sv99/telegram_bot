# -*- coding: utf-8 -*-
import telebot
from telebot import apihelper

#
# https://groosha.gitbook.io/telegram-bot-lessons/ - Пишем ботов для Telegram на языке Python
#

# using Tor proxy
apihelper.proxy = {'https':'socks5://localhost:9050'}

# @My_ugly_ugly_bot
API_TOKEN = '886216220:AAFuNgZdxzk9EeumP0uji8XFFgdWajLwHCU'
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print(message.from_user)
    name = message.from_user.first_name
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет %s, чем я могу тебе помочь?" % name)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "%s - напиши привет" % name)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
