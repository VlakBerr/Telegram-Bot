import datetime

import telebot

import config

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def handle_message(message):
    bot.send_message(message.chat.id, text="привет!")


@bot.message_handler(commands=['current_time', 'time'])
def current_time(message):
    now = datetime.datetime.now()
    output_message = f'{now.year} год, {now.month} месяц, {now.day} число'
    bot.send_message(message.chat.id, text=output_message)



bot.infinity_polling()