from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""¤¦ اهلا بـك يغالي 🫶❤️‍🩹 

¤¦ يمكنك استـخـراج التالـي 🫶❤️‍🩹

¤¦ تيرمڪس تليثون للحسابات 🫶❤️‍🩹

¤¦ تيرمـكـس تليثون للبوتـات 🫶❤️‍🩹

¤¦ بايـروجـرام مـيوزك للحسابات 🫶❤️‍🩹

¤¦ بايـروجـرام مـيوزك للبوتات 🫶❤️‍🩹

¤¦ مطور البوت 🫶❤️‍🩹 [ ⏤͟͞𝐀𝐋𝐏𝐎𝐏 |︎‍🦂| َِالــــبـــــوبــــ ](https://t.me/VIP_ALPOP)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="إضغط لبدا استخراج الكود", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("❣️ 𝗦𝗢𝗨𝗥𝗖𝗘 𝗔𝗟𝗣𝗢𝗣 ❣️", url="https://t.me/SOURCE_ALPOP"),
                    InlineKeyboardButton("❣️ 𝗗𝗘𝗩 𝗔𝗟𝗣𝗢𝗣 ❣️", user_id=OWNER_ID)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
