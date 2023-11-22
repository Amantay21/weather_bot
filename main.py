import requests
import json
import telebot
from telebot import types

bot = telebot.TeleBot("6608715523:AAF9rMJd4RPqsLgFxaVTiu9-O0L9sfGLhHE")
API = '898665fc82fc96d1ffd7b74989e3cfc5'


@bot.message_handler(commands=['start'])
def start(message):
    # bot.send_message(message.chat.id, 'Привет рад видеть тебя! Напиши название города')
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Ош')

    btn2 = types.KeyboardButton('Бишкек')
    btn3 = types.KeyboardButton('Лондон')
    markup.add(btn2, btn3)
    btn4 = types.KeyboardButton('Париж')
    btn5 = types.KeyboardButton('Хьюстон')
    btn6 = types.KeyboardButton('Токио')
    markup.add(btn1, btn4, btn5, btn6)
    bot.send_message(message.chat.id,' Привет рад видеть тебя! Напиши название города', reply_markup=markup)



@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'Сейчас погода: {temp}')

        image = ''
        if temp > 23.0:
            image = 'sunny.jpg'
        elif 23.0 >= temp > 11.0:
            image = 'chilly.jpg'
        elif temp < 11.0:
            image = 'cold.jpg'
        else:
            print('Температура не в диапазоне')
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, f'Город указан неверно')

bot.polling(none_stop=True)
