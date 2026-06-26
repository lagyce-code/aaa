import json
import asyncio
from pyrogram import Client, idle
from pyromod import listen
from pyrogram.types import ChatPrivileges, ChatPermissions

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

bot = Client(
    "m4o",
    api_id=31681257,
    api_hash="ac78c30e1f8498af7fc782630348dcaa",
    bot_token="8845386071:AAH8-_XjezIDvzj4U2foWIhdzGqy6qMd3mE",
    plugins=dict(root="MZombie")
)

# تعديل المسار ليقرأ من الفولدر الحالي مباشرة لتفادي خطأ الصلاحيات
with open('config.json', 'r', encoding='utf-8') as file:
    config = json.load(file)

sourse_dev = config['sourse_dev']

DEVS = []
DEVS.append(7807482327)
owner_id = sourse_dev
bot_id = bot.bot_token.split(":")[0]

async def start_zombiebot():
    print("[INFO]: جاري محاولة تشغيل البوت...")
    
    try:
        # المحاولة الأولى للتشغيل العادي
        await bot.start()
        print("[SUCCESS]: تم تشغيل البوت بنجاح من المحاولة الأولى!")
        
    except Exception as e:
        error_msg = str(e)
        # التحقق من خطأ توقيت السيرفر [16]
        if "msg_id is too low" in error_msg or "[16]" in error_msg:
            print("[!] اكتشاف خطأ في توقيت السيرفر.. جاري تطبيق المزامنة البرمجية تلقائياً...")
            try:
                # تصفير وقت بداية الجلسة لإجبار بايروجرام على احتساب الـ offset وتخطي فرق الساعة
                if hasattr(bot, "session") and bot.session:
                    bot.session.start_time = 0
                
                await asyncio.sleep(1)
                
                # إعادة المحاولة بعد تطبيق الخدعة
                await bot.start()
                print("[SUCCESS]: تم تخطي خطأ الساعة وتشغيل البوت بنجاح!")
            except Exception as retry_error:
                print(f"[ERROR]: فشل تشغيل البوت حتى بعد المزامنة الداعمة: {retry_error}")
                return
        else:
            print(f"[ERROR]: فشل التشغيل لسبب آخر تماماً: {e}")
            return

    # إرسال رسالة التنبيه للمطورين بعد إتمام التشغيل بنجاح وتخطي الأخطاء
    for hh in DEVS:
        try:
            await bot.send_message(hh, f"**◍ تم تشغيل الصانع بنجاح 🚦\n√**")
        except:
            pass
            
    await idle()

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
