from telebot import *
from dotenv import dotenv_values

config = dotenv_values(".env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}

bot = TeleBot(config["TOKEN"])

@bot.message_handler(commands=["webapp"])
def main(message):
    bot.send_message(message.chat.id, "!!! try our webapp !!!", reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Веб приложение", web_app=types.WebAppInfo("https://m6rshm3ll0w.github.io/ASLib/"))))

bot.infinity_polling()