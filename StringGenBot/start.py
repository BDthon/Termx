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
        text=f"""📟¦اهلا بـك عزيـزي 📬 {msg.from_user.mention},
⚡¦يـمكنك استـخـراج الـتـالـي
♻️¦تيرمـكـس تليثون للحسـابـات🏂
♻️¦تيرمـكـس تليثون للبوتــات🤖
🎧¦بايـروجـرام مـيوزك للحسابات🙋🏼‍♂️
🗽¦بايـروجـرام مـيوزك احدث اصدار🎊
🎧¦بايـروجـرام مـيوزك للبوتات🤖
- يعمـل هـذا البـوت لمساعدتـك بطريقـة سهلـه للحصـول على كـود تيرمكـس لتشغيل تلـيثون والبايروجرام لتشغيل السورسات تم انشـاء هـذا البـوت بواسطـة

بواسطـة : [𝑆𝑂𝑈𝑅𝐸𝐶 𝐵𝐷𝑇𝐻𝑂𝑁](http://t.me/BDthon) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="🌐 ⍆ اضغط لبدا استخراج كود ⍅🌐", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("⚙ الــســــوࢪسـ ⚙️", url="https://t.me/Bdthon"),
                    InlineKeyboardButton("𝑇𝑂𝐹𝐸𝑈 𝐼𝑅𝐴𝑄", user_id=6799580948)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
