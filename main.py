import telebot
from fastapi import FastAPI, Request

TOKEN = '8792672663:AAHv4ORGXc_wlSAPg6XqStqRUNsDvMYPmZI'
WEBHOOK_URL = "https://optimusprime-48zy.onrender.com/webhook"

bot = telebot.TeleBot(TOKEN)
app = FastAPI()


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Hi from webhook 👋")


@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    update = telebot.types.Update.de_json(data)
    bot.process_new_updates([update])
    return {"ok": True}


@app.on_event("startup")
async def on_startup():
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL)
