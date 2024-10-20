import telebot

import config
import user_contact


contacts = []
name = None
phone_number = None
discription = None


bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def handle_message(message):
    bot.send_message(message.chat.id, text="привет!")
    bot.send_message(message.chat.id, text="Я бот для записи контактов")   

@bot.message_handler(commands=['new_contact', 'add'])
def new_contact(message):
    user_message = bot.reply_to(message, 'Как зовут нового клиента?')
    bot.register_next_step_handler(user_message, process_name_step)

def process_name_step(user_message):
    global name 
    name = user_message.text
    user_messsage = bot.reply_to(user_message, 'Какой номер телефона у контакта?')
    bot.register_next_step_handler(user_message, process_phone_number_step)



def process_phone_number_step(user_message):
    global phone_number 
    phone_number = user_message.text
    
    user_messsage = bot.reply_to(user_message, 'Введите описание контакта(например, друг,коллега, семья).')
    bot.register_next_step_handler(user_message, process_discription_step)



def process_discription_step(user_message):
    global discription
    discription = user_message.text


    user = user_contact.UserContact(name, phone_number, discription)
    contacts.append(user)


    bot.send_message(user_message.chat.id, 'Вы ввели нового контакта')
    

@bot.message_handler(commands=['contacts'])
def list_contacts(message):
    if len(contacts) == 0:
        output_message = 'Вы не ввели ни одного сообщения'
        bot.send_message(message.chat.id, output_message)
    else:
        for contact in contacts:
            bot.send_message(message.chat.id, str(contact))





bot.infinity_polling()