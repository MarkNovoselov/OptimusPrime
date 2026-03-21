import telebot
from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
from telebot import types

TOKEN = '8792672663:AAHv4ORGXc_wlSAPg6XqStqRUNsDvMYPmZI'
WEBHOOK_URL = "https://optimusprime-48zy.onrender.com/webhook"


bot = telebot.TeleBot(TOKEN)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL)
    print("Webhook set")

    yield

    # shutdown (если нужно)
    bot.remove_webhook()


app = FastAPI(lifespan=lifespan)


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton("Словарь Матов", callback_data="btn1")

    markup.add(btn1)
    
    bot.send_message(message.chat.id, "Привет я Матный гномик, чем займемся?", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "btn1":
        bot.send_message(call.message.chat.id, '''Словарь матов по корням:
        -ху- (хуй)
        -хер-
        -хрен-
        -фиг-
        -еб-
        -пизд-
        -жоп-
        -говн-
        -ёпт-
        -бля-
        -перд-
        -ср- (срать)
        -муд-
        другие''')


@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    update = telebot.types.Update.de_json(data)
    bot.process_new_updates([update])
    return {"ok": True}
