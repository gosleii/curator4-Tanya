import telebot
bot = telebot.TeleBot('6286788789:AAGmaubVvm5Riigrm000RXnowwmVJQ_ZfEQ')
@bot.message_handler(commands=['start'])
def main(message):
	bot.send_message(message.chat.id,'Привет! \nНапиши /fact')

@bot. message_handler (commands=['fact'])
def main(message):
	bot.send_message(message.chat.id,'Умскул лучшая школа для подготовки к ОГЭ/ЕГЭ \nМожешь еще написать /like')

@bot. message_handler (commands=['like'])
def main(message):
	bot.send_message(message.chat.id,'Это [ССЫЛКА](https://umschool.net/)')

bot. infinity_polling()
