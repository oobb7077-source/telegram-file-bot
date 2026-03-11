import telebot

TOKEN = "8654488281:AAG7AeXMbIUnWkLlcFjv46XErT0ki94cn0w"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Send me a file.")

@bot.message_handler(content_types=['document','video','audio'])
def file_handler(message):
    bot.reply_to(message, "File received!")

bot.infinity_polling()
