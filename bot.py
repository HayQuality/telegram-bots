import telebot
from telebot import types

TOKEN = '7968610633:AAFt5nXWSPD-f-AktfKJJpOpR4z16_G-nsw'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("📄 Заполнить анкету", callback_data="form")
    btn2 = types.InlineKeyboardButton("🌐 Сайт", url="https://google.com")
    markup.add(btn1,btn2)
    bot.send_message(message.chat.id, "Выбери действие:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'form':
        bot.send_message(call.message.chat.id,'Как тебя зовут ?')
        bot.register_next_step_handler(call.message,ask_age)

def ask_age(message):
    name = message.text
    bot.send_message(message.chat.id,f"Приятно познакомиться, {name}! Сколько тебе лет?")
    bot.register_next_step_handler(message,finish_form,name)
def finish_form(message,name):
    age = message.text
    bot.send_message(message.chat.id, f"Спасибо, {name}! Ты записан как {age} лет.")

bot.polling()