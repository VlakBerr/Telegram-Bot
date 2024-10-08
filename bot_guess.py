from random import randint

from telebot import TeleBot, types

from config import token


bot = TeleBot(token=token)
low=1
high=100
bot_number = None



@bot.message_handler(commands=['start'])
def start(message):
    keyboard_markup = types.InlineKeyboardMarkup()
    button_start = types.InlineKeyboardButton(text='Начать', callback_data='start')
    keyboard_markup.add(button_start)
    bot.send_message(message.chat.id, 'Привет! Я бот для игры "Угадай число", нажми "Начать" чтобы играть',
                     reply_markup=keyboard_markup)
    
@bot.message_handler(func=lambda message: True)
def any_other_message(message):
    bot.send_message(message.chat.id, 'Выйди из бота')



@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'start':
        global bot_number
        bot_number = randint(low, high)

        output_message = f'Я загадал число от {low} до {high}'


        message = call.message
        #bot.delete_message(chat_id=message.chat.id, message_id = message.id, text = 'Начнем')
        #bot.edit_message_text(chat_id=message.chat.id, message_id = message.id, text = 'Начнем')

        bot.edit_message_text(chat_id=message.chat.id, message_id=message.id, text=output_message)
        bot.register_next_step_handler(message, process_guess_number_step)


def process_guess_number_step(message):
    str_number = message.text
    if not str_number.isdigit():
        bot.send_message(message.chat.id, 'Вы ввели не число! Введите число')
        bot.register_next_step_handler(message, process_guess_number_step)
        return
    number = int(str_number)

    if number == bot_number:
        output_message = 'Вы угадали!'
    elif number < bot_number:
        output_message = 'Я загадал чило больше'
    else:
        output_message = 'Я загадал чило меньше'
    bot.send_message(message.chat.id, output_message)

    if output_message != 'Вы угадали!':
        bot.register_next_step_handler(message, process_guess_number_step)

bot.infinity_polling()
