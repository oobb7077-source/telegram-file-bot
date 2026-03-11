from pyrogram import Client, filters, idle
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

API_ID = 32100091
API_HASH = "612fe5aa877cfc69abc5a6d92019627b"
BOT_TOKEN ="8654488281:AAHK3jdV6x3KqroxmMQbt1JX5LmBw8y5fAU"

OWNER_ID = 6495482801
OWNER_TAG = "@Suzuka_17"

CHANNELS = [
    ("📢 Channel 1", "@Otaku_Paradise_Jp", "https://t.me/Otaku_Paradise_Jp"),
    ("📢 Channel 2", "@NexPlayHQ", "https://t.me/NexPlayHQ"),
    ("📢 Channel 3", "@CraftMM", "https://t.me/CraftMM"),
    ("📢 Channel 4", "@Gyro_Gaming_Market", "https://t.me/Gyro_Gaming_Market")
]

app = Client("KT_FILE_BOT", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


# JOIN BUTTONS
def join_buttons():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("📢 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 𝟭", url=CHANNELS[0][2]),
            InlineKeyboardButton("📢 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 𝟮", url=CHANNELS[1][2])
        ],
        [
            InlineKeyboardButton("📢 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 𝟯", url=CHANNELS[2][2]),
            InlineKeyboardButton("📢 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 𝟰", url=CHANNELS[3][2])
        ],
        [
            InlineKeyboardButton("♻️ 𝗧𝗥𝗬 𝗔𝗚𝗔𝗜𝗡", callback_data="check_join")
        ]
    ])


# CHECK JOIN
async def check_join(client, user_id):

    for name, username, link in CHANNELS:

        try:
            member = await client.get_chat_member(username, user_id)

            if member.status in ["left", "kicked"]:
                return False

        except:
            return False

    return True


# START
@app.on_message(filters.command("start"))
async def start(client, message):

    text = f"""
╭━━━〔 🚀 𝗞𝗧 𝗙𝗜𝗟𝗘 𝗕𝗢𝗧 〕━━━╮
┃
┃ 📂 𝗙𝗶𝗹𝗲 𝗦𝘁𝗼𝗿𝗮𝗴𝗲 𝗕𝗼𝘁
┃ 🔒 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 𝗝𝗼𝗶𝗻 𝗥𝗲𝗾𝘂𝗶𝗿𝗲𝗱
┃
┃ 📥 𝗧𝘆𝗽𝗲 /get
┃ 𝗧𝗼 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗙𝗶𝗹𝗲
┃
┣━━━━━━━━━━━━━━━
┃ 👑 𝗢𝘄𝗻𝗲𝗱 𝗕𝘆 : {OWNER_TAG}
╰━━━━━━━━━━━━━━━╯
"""

    await message.reply_text(text)


# USER FILE REQUEST
@app.on_message(filters.command("get"))
async def get_file(client, message):

    joined = await check_join(client, message.from_user.id)

    if not joined:

        text = f"""
╭━━━〔 📢 𝗝𝗢𝗜𝗡 𝗙𝗜𝗥𝗦𝗧 〕━━━╮
┃
┃ ⚠️ 𝗣𝗹𝗲𝗮𝘀𝗲 𝗝𝗼𝗶𝗻
┃ 𝗔𝗹𝗹 𝗢𝘂𝗿 𝗖𝗵𝗮𝗻𝗻𝗲𝗹𝘀
┃
┃ 📥 𝗔𝗳𝘁𝗲𝗿 𝗝𝗼𝗶𝗻
┃ ♻️ 𝗖𝗹𝗶𝗰𝗸 𝗧𝗿𝘆 𝗔𝗴𝗮𝗶𝗻
┃
┣━━━━━━━━━━━━━━━
┃ 👑 𝗢𝘄𝗻𝗲𝗱 𝗕𝘆 : {OWNER_TAG}
╰━━━━━━━━━━━━━━━╯
"""

        await message.reply_text(text, reply_markup=join_buttons())
        return

    if not os.path.exists("file.zip"):
        await message.reply_text("❌ 𝗙𝗶𝗹𝗲 𝗡𝗼𝘁 𝗙𝗼𝘂𝗻𝗱")
        return

    await message.reply_document(
        "file.zip",
        caption=f"""
╭━━━〔 📦 𝗗𝗢𝗪𝗡𝗟𝗢𝗔𝗗 𝗥𝗘𝗔𝗗𝗬 〕━━━╮
┃
┃ ✅ 𝗝𝗼𝗶𝗻 𝗩𝗲𝗿𝗶𝗳𝗶𝗲𝗱
┃ ⬇️ 𝗙𝗶𝗹𝗲 𝗦𝗲𝗻𝘁
┃
┣━━━━━━━━━━━━━━━
┃ 👑 𝗢𝘄𝗻𝗲𝗱 𝗕𝘆 : {OWNER_TAG}
╰━━━━━━━━━━━━━━━╯
"""
    )


# TRY AGAIN
@app.on_callback_query(filters.regex("check_join"))
async def check_again(client, query):

    joined = await check_join(client, query.from_user.id)

    if not joined:

        await query.answer("❌ 𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹𝘀 𝗙𝗶𝗿𝘀𝘁", show_alert=True)

    else:

        await query.message.edit_text(
"""
╭━━━〔 ✅ 𝗩𝗘𝗥𝗜𝗙𝗜𝗘𝗗 〕━━━╮
┃
┃ 🎉 𝗝𝗼𝗶𝗻 𝗖𝗼𝗺𝗽𝗹𝗲𝘁𝗲
┃
┃ 📥 𝗡𝗼𝘄 𝗧𝘆𝗽𝗲 /get
┃
╰━━━━━━━━━━━━━━━╯
"""
        )


# OWNER FILE UPLOAD
@app.on_message(filters.document)
async def upload(client, message):

    if message.from_user.id != OWNER_ID:

        await message.reply_text(
"""
╭━━━〔 ❌ 𝗔𝗖𝗖𝗘𝗦𝗦 𝗗𝗘𝗡𝗜𝗘𝗗 〕━━━╮
┃
┃ 🚫 𝗢𝗻𝗹𝘆 𝗕𝗼𝘁 𝗢𝘄𝗻𝗲𝗿
┃ 𝗖𝗮𝗻 𝗨𝗽𝗹𝗼𝗮𝗱
┃
╰━━━━━━━━━━━━━━━╯
"""
        )
        return

    await message.reply_text(
"""
╭━━━〔 📦 𝗙𝗜𝗟𝗘 𝗦𝗔𝗩𝗘𝗗 〕━━━╮
┃
┃ ✅ 𝗙𝗶𝗹𝗲 𝗦𝘁𝗼𝗿𝗲𝗱
┃ 👑 𝗢𝘄𝗻𝗲𝗿 𝗨𝗽𝗹𝗼𝗮𝗱
┃
╰━━━━━━━━━━━━━━━╯
"""
    )


print("🚀 KT FILE BOT STARTED")
app.start()
idle()
