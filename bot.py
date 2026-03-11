import telebot

TOKEN ="8654488281:AAFeBq9-2Gang_0r3bM7P6bBJEuV-a7hPEk"
OWNER_ID = 6495482801
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "🚀 Welcome to Turbo File Bot\nSend me a file!")

@bot.message_handler(content_types=['document'])
def file_handler(message):

    if message.from_user.id != OWNER_ID:
        bot.send_message(message.chat.id,"❌ You are not allowed to upload files.")
        return

    bot.send_message(message.chat.id,"✅ File received!")

bot.infinity_polling()
