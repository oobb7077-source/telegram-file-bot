import telebot

TOKEN ="8654488281:AAFeBq9-2Gang_0r3bM7P6bBJEuV-a7hPEk"
OWNER_ID = 6495482801
bot = telebot.TeleBot(TOKEN)

files = {}

@bot.message_handler(commands=['start'])
def start(message):

    args = message.text.split()

    if len(args) > 1:
        key = args[1]

        if key in files:
            bot.send_document(message.chat.id, files[key])
            return

    text = """
╭━━━〔 🚀 𝙏𝙐𝙍𝘽𝙊 𝙁𝙄𝙇𝙀 𝘽𝙊𝙏 〕━━━╮

📤 𝙎𝙚𝙣𝙙 𝙢𝙚 𝙖 𝙛𝙞𝙡𝙚  
🔗 𝙄 𝙬𝙞𝙡𝙡 𝙘𝙧𝙚𝙖𝙩𝙚 𝙖 𝙙𝙤𝙬𝙣𝙡𝙤𝙖𝙙 𝙡𝙞𝙣𝙠  

⚡ 𝙁𝙖𝙨𝙩 | 𝙎𝙚𝙘𝙪𝙧𝙚 | 𝙀𝙖𝙨𝙮

╰━━━━━━━━━━━━━━━━╯
"""
    bot.send_message(message.chat.id, text)


@bot.message_handler(content_types=['document'])
def file_handler(message):

    file_id = message.document.file_id
    unique = message.document.file_unique_id

    files[unique] = file_id

    link = f"https://t.me/YOUR_BOT_USERNAME?start={unique}"

    text = f"""
╭━━━〔 ✅ 𝙁𝙄𝙇𝙀 𝙐𝙋𝙇𝙊𝘼𝘿𝙀𝘿 〕━━━╮

📂 𝙁𝙞𝙡𝙚: {message.document.file_name}

🔗 𝘿𝙤𝙬𝙣𝙡𝙤𝙖𝙙 𝙇𝙞𝙣𝙠
{link}

╰━━━━━━━━━━━━━━━━╯
"""

    bot.send_message(message.chat.id, text)


bot.infinity_polling()
