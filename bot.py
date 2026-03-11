import telebot

TOKEN ="8654488281:AAFeBq9-2Gang_0r3bM7P6bBJEuV-a7hPEk"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Send me a file.")

@bot.message_handler(content_types=['document','video','audio'])
def file_handler(message):
    bot.reply_to(message, "File received!")

bot.infinity_polling()
