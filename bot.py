import telebot
from telebot import apihelper

#main variables
TOKEN = "624798015:AAFvK2W7CkjEMj56ZVB6c7bYcPLWaDff12o"
bot = telebot.TeleBot(TOKEN)


#handlers
@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет, я бот безумного Гарика, молочу в фарш любое информационное мясо')

@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    if text == "привет":
        bot.send_message(chat_id, 'Привет')
    else:
        bot.send_message(chat_id, 'Простите, я вас не понял :(')
bot.polling()