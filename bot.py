import telebot
from telebot import types
token='5645976423:AAHjVCXh-bsIP9RGPFkdanQ-FFx0Fe2UDaw'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id,'👋Привет,это бот - фрилансбиржа ,тут ты сможешь разместить свой заказ или заработать.Для продолжения нажми на кнопку ниже.')


bot.infinity_polling()