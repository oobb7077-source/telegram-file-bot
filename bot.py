from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_ID = 32100091
API_HASH = "612fe5aa877cfc69abc5a6d92019627b"
BOT_TOKEN ="8654488281:AAEwzgvD7aOtVafkvw8VhS8bPPghjzNXvEI"

OWNER_ID = 6495482801

CHANNELS = [
    ("Join Channel 1", "@channel1"),
    ("Join Channel 2", "@channel2"),
    ("Join Channel 3", "@channel3"),
    ("Join Channel 4", "@channel4")
]

app = Client("KT_TURBO_BOT", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


def join_buttons():
    buttons = [
        [
            InlineKeyboardButton("📢 Join Channel 1", url="https://t.me/channel1"),
            InlineKeyboardButton("📢 Join Channel 2", url="https://t.me/channel2")
        ],
        [
            InlineKeyboardButton("📢 Join Channel 3", url="https://t.me/channel3"),
            InlineKeyboardButton("📢 Join Channel 4", url="https://t.me/channel4")
        ],
        [
            InlineKeyboardButton("♻️ Try Again", callback_data="check_join")
        ]
    ]
    return InlineKeyboardMarkup(buttons)


async def check_join(client, user_id):
    for ch_name, ch in CHANNELS:
        try:
            member = await client.get_chat_member(ch, user_id)
            if member.status in ["left", "kicked"]:
                return False
        except:
            return False
    return True


@app.on_message(filters.command("start"))
async def start(client, message):

    joined = await check_join(client, message.from_user.id)

    if not joined:

        text = """
╭━━━〔 📢 𝐉𝐎𝐈𝐍 𝐑𝐄𝐐𝐔𝐈𝐑𝐄𝐃 〕━━━╮
┃
┃ ⚠️ 𝐁𝐨𝐭 𝐮𝐬𝐞 𝐥𝐮𝐩𝐚
┃ 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐚𝐫 𝐤𝐨𝐮𝐧𝐠 𝐣𝐨𝐢𝐧 𝐩𝐚
┃
┃ 📥 𝐉𝐨𝐢𝐧 𝐩𝐲𝐢𝐲 𝐭𝐚𝐡
┃ ♻️ 𝐓𝐫𝐲 𝐀𝐠𝐚𝐢𝐧 𝐧𝐡𝐢𝐩 𝐩𝐚
┃
╰━━━━━━━━━━━━━━━━━━━━━━╯
"""
        await message.reply_text(text, reply_markup=join_buttons())
        return

    text = """
╭━━━〔 🚀 𝐊𝐓 𝐓𝐔𝐑𝐁𝐎 𝐁𝐎𝐓 〕━━━╮
┃
┃ ⚡ 𝐅𝐢𝐥𝐞 𝐒𝐭𝐨𝐫𝐚𝐠𝐞 𝐁𝐨𝐭
┃ 🔒 𝐎𝐰𝐧𝐞𝐫 𝐎𝐧𝐥𝐲 𝐔𝐩𝐥𝐨𝐚𝐝
┃
┃ 📤 𝐒𝐞𝐧𝐝 𝐚 𝐅𝐢𝐥𝐞
┃ 𝐓𝐨 𝐒𝐭𝐨𝐫𝐞
┃
╰━━━━━━━━━━━━━━━━━━━━━━╯
"""
    await message.reply_text(text)


@app.on_callback_query(filters.regex("check_join"))
async def check_join_callback(client, query):

    joined = await check_join(client, query.from_user.id)

    if not joined:
        await query.answer("❌ Join channels first!", show_alert=True)
    else:
        await query.message.edit_text(
"""
╭━━━〔 ✅ 𝐕𝐄𝐑𝐈𝐅𝐈𝐄𝐃 〕━━━╮
┃
┃ 🎉 𝐘𝐨𝐮 𝐜𝐚𝐧 𝐧𝐨𝐰
┃ 𝐮𝐬𝐞 𝐭𝐡𝐞 𝐛𝐨𝐭
┃
╰━━━━━━━━━━━━━━━━━━━━━━╯
"""
        )


@app.on_message(filters.document)
async def file_handler(client, message):

    if message.from_user.id != OWNER_ID:
        await message.reply_text(
"""
╭━━━〔 ❌ 𝐀𝐂𝐂𝐄𝐒𝐒 𝐃𝐄𝐍𝐈𝐄𝐃 〕━━━╮
┃
┃ 🚫 𝐎𝐧𝐥𝐲 𝐁𝐨𝐭 𝐎𝐰𝐧𝐞𝐫
┃ 𝐂𝐚𝐧 𝐔𝐩𝐥𝐨𝐚𝐝
┃
╰━━━━━━━━━━━━━━━━━━━━━━╯
"""
        )
        return

    file_name = message.document.file_name
    size = round(message.document.file_size / (1024*1024),2)

    text = f"""
╭━━━〔 📦 𝐅𝐈𝐋𝐄 𝐒𝐓𝐎𝐑𝐄𝐃 〕━━━╮
┃
┃ 📄 𝐍𝐚𝐦𝐞 : {file_name}
┃ 💾 𝐒𝐢𝐳𝐞 : {size} MB
┃
┃ ✅ 𝐔𝐩𝐥𝐨𝐚𝐝 𝐒𝐮𝐜𝐜𝐞𝐬𝐬
┃ 👑 𝐁𝐲 : 𝐎𝐰𝐧𝐞𝐫 ➝ @Suzuka_17
┃
╰━━━━━━━━━━━━━━━━━━━━━━╯
"""
    await message.reply_text(text)


app.run()
