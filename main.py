import requests
import telebot
from telebot import types
bot = telebot.TeleBot("6589521510:AAH2XlLc63zd0-z4LA9fF-PjOarqPvlU-dY")
@bot.message_handler(commands=["start"])
def startt(message):
    start = types.InlineKeyboardButton(text="جلب المواقيت",callback_data="get")
    start1 = types.InlineKeyboardButton(text="حسابي",url="https://t.me/B_xxBx")
    btn1 = types.InlineKeyboardMarkup(row_width=1)
    btn1.add(start,start1)
    bot.reply_to(message ,"اهلًا بك في بوت مواقيت الصلاة حسب مدينتك اضغط على زر ( جلب المواقيت ) للبدأ",reply_markup=btn1)
@bot.callback_query_handler(func =lambda call:True)
def comm(call):
    if call.data=="get":
        back = types.InlineKeyboardButton(text="رجوع",callback_data="back")
        btn2 = types.InlineKeyboardMarkup()
        btn2.add(back)
        v = bot.edit_message_text(chat_id=call.message.chat.id ,message_id =call.message.message_id ,text="اكتب اسم مدينتك بالعربي",reply_markup=btn2)
        bot.register_next_step_handler(v,go)
    elif call.data == "back":
        start = types.InlineKeyboardButton(text="جلب المواقيت",callback_data="get")
        start1 = types.InlineKeyboardButton(text="حسابي",url="https://t.me/B_xxBx")
        btn1 = types.InlineKeyboardMarkup(row_width=1)
        btn1.add(start,start1)
        bot.edit_message_text(chat_id =call.message.chat.id ,message_id =call.message.message_id,text="اهلًا بك في بوت مواقيت الصلاة حسب مدينتك اضغط على زر ( جلب المواقيت ) للبدأ",reply_markup=btn1)
    elif call.data == "ag":
        start = types.InlineKeyboardButton(text="جلب المواقيت",callback_data="get")
        start1 = types.InlineKeyboardButton(text="حسابي",url="https://t.me/B_xxBx")
        btn1 = types.InlineKeyboardMarkup(row_width=1)
        btn1.add(start,start1)
        bot.edit_message_text(chat_id =call.message.chat.id ,message_id =call.message.message_id,text="اهلًا بك في بوت مواقيت الصلاة حسب مدينتك اضغط على زر ( جلب المواقيت ) للبدأ",reply_markup=btn1)
def go(message):
    btn3 = types.InlineKeyboardMarkup()
    bacck = types.InlineKeyboardButton(text="ابدأ من جديد",callback_data="ag")
    btn3.add(bacck)
    cc = str(message.text)
    req = requests.get(f"https://prayer.brhymibrahim1.repl.co/ibrahim?city={cc}").json()
    date = req['main']['date']
    city = req['main']['city']
    fajr = req['main']['fajr']
    shurooq = req['main']['shurooq']
    dhuhr = req['main']['dhuhr']
    asr = req['main']['asr']
    maghrib = req['main']['maghrib']
    isha = req['main']['isha']
    all = f"-------------------------------\nالمدينة : {city}\nالتاريخ : {date}\nالفجر : {fajr}\nالشروق : {shurooq}\nالظهر : {dhuhr}\nالعصر : {asr}\nالمغرب : {maghrib}\nالعشاء : {isha}\n-------------------------------\n"
    bot.reply_to(message ,all, reply_markup=btn3)
bot.polling()
