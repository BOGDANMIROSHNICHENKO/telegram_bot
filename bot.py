import telebot
from telebot import types
from data import SQLighter as db


model = db('db.db')
token = '5500865116:AAH_kq3g1EwdNr5M7OqObk-CevGK-biPjv8'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, reply_markup=markup,
                     text='Привет,это бот - фрилансбиржа ,тут ты сможешь разместить свой заказ или заработать. Для продолжения нажми на кнопку ниже.')


markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton("Я Заказчик")
btn2 = types.KeyboardButton("Я Исполнитель")
markup.add(btn1, btn2)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Я Исполнитель"):
        btn = types.KeyboardButton("Подбор заказов")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(btn)
        bot.send_message(message.chat.id, reply_markup=markup,
                         text='Выберите заказ')

    elif(message.text == "Я Заказчик"):
        btn = types.KeyboardButton("Создать заказ")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(btn)
        bot.send_message(message.chat.id, reply_markup=markup,
                         text='Создайте заказ по макету анкеты:\n1.Название заказа\n2.Описание заказа\n3.Цена\n4.Фото(необязательно)\n5.Что нужно для проверки.')
        model.add_order(message.from_user.id, message.text)


bot.polling()
