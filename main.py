import telebot

bot = telebot.TeleBot('8792672663:AAHv4ORGXc_wlSAPg6XqStqRUNsDvMYPmZI')

@bot.message_handler(commands=['start'])
def start_messsage(message):
    bot.send_message(message.chat.id, 'пашел нахуй')

bot.infinity_polling(none_stop=True,interval=0)