import telebot
from telebot import apihelper

#main variables
TOKEN = "624798015:AAFvK2W7CkjEMj56ZVB6c7bYcPLWaDff12o"
bot = telebot.TeleBot(TOKEN)


#handlers
@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    chat_id = message.chat.id
    text = message.text
    msg = bot.send_message(chat_id, 'Сколько вам лет?')
    bot.register_next_step_handler(msg, askAge)

def askAge(message):
    chat_id = message.chat.id
    text = message.text
    if not text.isdigit():
        msg = bot.send_message(chat_id, 'Возраст должен быть числом, введите еще раз')
        bot.register_next_step_handler(msg, askAge) #askSource
        return
    msg = bot.send_message(chat_id, 'Спасибо, я запомнил что вам' + text + 'лет')

'''
@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    if text == "привет":
        bot.send_message(chat_id, 'Привет Garik')
    else:
        bot.send_message(chat_id, 'Простите, я вас не понял :(')
bot.polling()
'''