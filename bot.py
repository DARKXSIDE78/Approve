from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters, Client, errors, enums
from pyrogram.errors import UserNotParticipant
from pyrogram.errors.exceptions.flood_420 import FloodWait
from database import add_user, add_group, all_users, all_groups, users, remove_user
from configs import cfg
import random, asyncio
from flask import Flask, jsonify, request

app = Client(
    "approver",
    api_id=cfg.API_ID,
    api_hash=cfg.API_HASH,
    bot_token=cfg.BOT_TOKEN
)

gif = [
    'https://media.tenor.com/Kjtc-YmBNn0AAAPo/mad-rem.mp4'
]

# Initialize Flask app
flask_app = Flask(__name__)

# Web service example: Health check endpoint
@flask_app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok", "message": "Koyeb Health Pass is working!"})

@flask_app.route('/status', methods=['GET'])
def status():
    # Example of checking if the bot is running
    return jsonify({"status": "Bot is running", "users": len(all_users()), "groups": len(all_groups())})



#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_chat_join_request(filters.group | filters.channel & ~filters.private)
async def approve(_, m : Message):
    op = m.chat
    kk = m.from_user
    try:
        add_group(m.chat.id)
        await app.approve_chat_join_request(op.id, kk.id)
        img = random.choice(gif)
        await app.send_video(kk.id,img, "Bᴀᴋᴋᴀ!!! **{},\nWᴇʟᴄᴏᴍᴇ ᴛᴏ {}".format(m.from_user.mention, m.chat.title))
        add_user(kk.id)
    except errors.PeerIdInvalid as e:
        print("user isn't start bot(means group)")
    except Exception as err:
        print(str(err))    
 
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Start ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("start"))
async def op(_, m :Message):
    try:
        await app.get_chat_member(cfg.CHID, m.from_user.id) 
        if m.chat.type == enums.ChatType.PRIVATE:
            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Mᴀɪɴ Hᴜʙ", url="https://telegram.me/GenAnimeOfc"),
                        InlineKeyboardButton("Rᴀɴᴅᴏᴍ", url="https://t.me/+z05NzRmuqjBkYTdl")
                    ]
                ]
            )
            add_user(m.from_user.id)
            await m.reply_photo("https://i.redd.it/wa92g16cqb071.jpg", caption="Bᴀᴋᴋᴀ!!! **{}\nI ᴀᴍ Nᴀᴛsᴜᴋɪ Sᴜʙᴀʀᴜ \nYᴏᴜ ᴡᴀɴᴛ ʏᴏᴜʀ ᴏᴡɴ ᴀᴜᴛᴏ ᴀᴘᴘʀᴏᴠᴇʀ ʙᴏᴛ?\nJᴜsᴛ ᴀᴅᴅ ᴍᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ. ɢɪᴠᴇ ᴍᴇ ᴀᴅᴍɪɴ ʀɪɢʜᴛs ʟɪᴋᴇ ʟɪɴᴋ ᴀɴᴅ ᴘᴇʀᴍɪssɪᴏɴ ᴛᴏ ᴀᴄᴄᴇᴘᴛ ᴜsᴇʀ's ʀᴇǫᴜᴇsᴛ.\n\n__Cʀᴇᴀᴛᴏʀ: @DARKXSIDE78**".format(m.from_user.mention, "https://telegram.me/GenAnimeOfc"), reply_markup=keyboard)
    
        elif m.chat.type == enums.ChatType.GROUP or enums.ChatType.SUPERGROUP:
            keyboar = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Mᴀɪɴ Hᴜʙ", url="https://telegram.me/GenAnimeOfc")
                    ]
                ]
            )
            add_group(m.chat.id)
            await m.reply_text("Bᴀᴋᴋᴀ!!! **{}\nMᴇssᴀɢᴇ ᴍᴇ ᴘʀɪᴠᴀᴛᴇʟʏ**".format(m.from_user.first_name), reply_markup=keyboar)
        print(m.from_user.first_name +" ʜᴀs sᴛᴀʀᴛᴇᴅ Yᴏᴜʀ Bᴏᴛ!")

    except UserNotParticipant:
        key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("GᴇɴAɴɪᴍᴇ", url="https://telegram.me/GenAnimeOfc")
                ],[
                    InlineKeyboardButton("Rᴇᴛʀʏ!!!","chk")
                ]
            ]
        )
        await m.reply_text("**Aᴄᴄᴇss Dᴇɴɪᴇᴅ!!!\n\nYᴏᴜ ʜᴀᴠᴇ ɴᴏᴛ ᴊᴏɪɴᴇᴅ ᴏᴜʀ ɢʀᴏᴜᴘ. Jᴏɪɴ ᴀɴᴅ ʀᴇᴛʀʏ.**".format(cfg.FSUB), reply_markup=key)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ callback ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_callback_query(filters.regex("chk"))
async def chk(_, cb : CallbackQuery):
    try:
        await app.get_chat_member(cfg.CHID, cb.from_user.id)
        if cb.message.chat.type == enums.ChatType.PRIVATE:
            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Mᴀɪɴ Hᴜʙ", url="https://telegram.me/GenAnimeOfc"),
                        InlineKeyboardButton("Rᴀɴᴅᴏᴍ", url="https://t.me/+z05NzRmuqjBkYTdl")
                    ]
                ]
            )
            add_user(cb.from_user.id)
            await cb.message.edit("Bᴀᴋᴋᴀ!!! **{}\nI ᴀᴍ Nᴀᴛsᴜᴋɪ Sᴜʙᴀʀᴜ\n__Cʀᴇᴀᴛᴏʀ: @DARKXSIDE78**".format(cb.from_user.mention, "https://telegram.me/GenAnimeOfc"), reply_markup=keyboard, disable_web_page_preview=True)
        print(cb.from_user.first_name +" ʜᴀs sᴛᴀʀᴛᴇᴅ Yᴏᴜʀ Bᴏᴛ!")
    except UserNotParticipant:
        await cb.answer("Yᴏᴜ ʜᴀᴠᴇ ɴᴏᴛ ᴊᴏɪɴᴇᴅ ᴏᴜʀ ɢʀᴏᴜᴘ. Jᴏɪɴ ᴀɴᴅ ʀᴇᴛʀʏ.")

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Info ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("users") & filters.user(cfg.SUDO))
async def dbtool(_, m : Message):
    xx = all_users()
    x = all_groups()
    tot = int(xx + x)
    await m.reply_text(text=f"""
Mʏ Aʟʟ Sᴛᴀᴛs

Tᴏᴛᴀʟ Usᴇʀs: `{xx}`
Tᴏᴛᴀʟ Gʀᴏᴜᴘs: `{x}`
Tᴏᴛᴀʟ Usᴇʀ+Gʀᴏᴜᴘ: `{tot}` """)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Broadcast ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("bcast") & filters.user(cfg.SUDO))
async def bcast(_, m : Message):
    allusers = users
    lel = await m.reply_text("`⚡️ Pʀᴏᴄᴇssɪɴɢ...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            #print(int(userid))
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
        except errors.InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await lel.edit(f"Sᴜᴄᴄᴇssғᴜʟ: `{success}`\nFᴀɪʟᴇᴅ: `{failed}`\nBʟᴏᴄᴋᴇᴅ: `{blocked}`\nDᴇᴀᴄᴛɪᴠᴀᴛᴇᴅ: `{deactivated}`")

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Broadcast Forward ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("fcast") & filters.user(cfg.SUDO))
async def fcast(_, m : Message):
    allusers = users
    lel = await m.reply_text("`⚡️ Pʀᴏᴄᴇssɪɴɢ...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            #print(int(userid))
            if m.command[0] == "fcast":
                await m.reply_to_message.forward(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "fcast":
                await m.reply_to_message.forward(int(userid))
        except errors.InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await lel.edit(f"Sᴜᴄᴄᴇssғᴜʟ: `{success}`\nFᴀɪʟᴇᴅ: `{failed}`\nBʟᴏᴄᴋᴇᴅ: `{blocked}`\nDᴇᴀᴄᴛɪᴠᴀᴛᴇᴅ: `{deactivated}`")

if __name__ == '__main__':
    from threading import Thread
    # Start the Flask server in a separate thread to avoid blocking the Pyrogram client
    def start_flask():
        flask_app.run(host="0.0.0.0", port=8000)

    # Start Flask server
    thread = Thread(target=start_flask)
    thread.start()

print("Nᴀᴛsᴜᴋɪ Sᴜʙᴀʀᴜ ɪs ʙᴀᴄᴋ!!!")
app.run()
