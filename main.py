import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import gdshortener
import requests
from user_agent import generate_user_agent
import re
import telebot , random
from telebot import types
import datetime
from hijri_converter import convert
from telebot.types import InlineKeyboardButton as b, InlineKeyboardMarkup as mk

from telebot.types import InlineKeyboardMarkup as b,InlineKeyboardMarkup as mk
import sqlite3
bot = telebot.TeleBot("6532286475:AAFIjc53deB8e03_jZRxmpEjuS2ppYGJd2Q") #حط توكن بوتك بين ""




@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message,"""
    السورس
/link
/st
/str
/today
/id""")
    
    
@bot.message_handler(func=lambda message: message.text =="السورس")
def send_source(message):
    url = 'https://t.me/my00002/136' #هنا سوي قناه عامة وانشر بيها الصوره وانسخ رابط الصوره وحطه بين الـ('')
    chat_id = message.chat.id
    bot.send_photo(chat_id=chat_id, photo=url, caption="")

    keyboard = InlineKeyboardMarkup(row_width=1)
    channel_button = InlineKeyboardButton("قناة السورس", url="http://t.me/my00002")
    developer_button = InlineKeyboardButton("مطور السورس", url="http://t.me/altaee_z")
    share_button = InlineKeyboardButton("مشاركة البوت 🤖", switch_inline_query="") #لتغير شي هنا
    keyboard.add(channel_button, developer_button, share_button)
                                                      #هنا غير الرساله بس لتشيل ال""
    bot.reply_to(message, "آلَلَهّمً صّلَِّ عٌلَى مًحًمًدٍ وٌآلَ مًحًمًدٍ 🌺", reply_markup=keyboard) 



cookies = {
    'AppSession': '6j35pliejibipiidgqr4kueuv1',
    'csrfToken': '75aa4558310672a8042cc16fcbcdffd5477b8d9c9bf46f91e401c5a532675602c645e04878c56f8ea172da3e837c27734014460b3b55dc1bbce8277162ada3c8',
    'sls': '0',
    'tmz': 'Asia/Jerusalem',
    'ref': 'admin',
    'ab': '2',
    '_ga_6QVVMFTPT3': 'GS1.1.1687605103.1.0.1687605103.0.0.0',
    '_ga': 'GA1.1.1737572540.1687605104',
}



headers = {
    'authority': 'za.gl',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://za.gl',
    'referer': 'https://za.gl/',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': generate_user_agent(),
    'x-requested-with': 'XMLHttpRequest',
}

@bot.message_handler(commands=['link'])
def Welcome(message):
 name = message.from_user.first_name
 keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)
 keyboard.add(
        telebot.types.InlineKeyboardButton(text='is.gd', callback_data='1'),
    )
    
 bot.reply_to(message,'''مرحبا {}
بوت اختصار روابط متعدد اختر ما يناسبك من الازرار .. )؛'''.format(name),reply_markup=keyboard)
 
@bot.callback_query_handler(func=lambda call:True)
def all(call):
 if call.data == '1':
  bot.send_message(call.message.chat.id,'ارسل الرابط لأقوم بأختصار بدومين is.gd')
  bot.register_next_step_handler(call.message, one)
def one(message):
 if re.search("(?P<url>https?://[^\s]+)", message.text):
 	s = gdshortener.ISGDShortener()
 	a = s.shorten(message.text)[0]
 	bot.reply_to(message,a)
 else:
 	bot.reply_to(message,'sorry ,This is not a link URL')
 
def two(message):
	global cookies
	global headers
	
	data = {
	'_method': 'POST',
	'_csrfToken': '75aa4558310672a8042cc16fcbcdffd5477b8d9c9bf46f91e401c5a532675602c645e04878c56f8ea172da3e837c27734014460b3b55dc1bbce8277162ada3c8',
	'url': message.text,
	'ad_type': '2',
	'_Token[fields]': 'fba2ac211af3a04684cf7ffe3e6afdc452d7f50f%3Aad_type',
	'_Token[unlocked]': 'adcopy_challenge%7Cadcopy_response%7Ccoinhive-captcha-token%7Cg-recaptcha-response',
	}
	response = requests.post('https://za.gl/links/shorten',cookies=cookies,headers=headers, data=data).json()['url']
	if re.search("(?P<url>https?://[^\s]+)", message.text):
	   bot.reply_to(message,response)
	else:
		bot.reply_to(message, "sorry ,This is not a link URL")

def three(message):
 if re.search("(?P<url>https?://[^\s]+)", message.text):
 	url = f'https://v.ht/api.php?url='+message.text
 	req = requests.get(url).text
 	bot.reply_to(message,req)
 else:
 	bot.reply_to(message,'sorry ,This is not a link URL')
 	

@bot.message_handler(commands=['st'])
def welcome(message):
    name = message.from_user.first_name
    global count
    count = 0
    markup = types.InlineKeyboardMarkup()
    
    markup.add(types.InlineKeyboardButton("تسبيح", callback_data="tasbeeh"))
    bot.send_message(message.chat.id,"مرحبا بك {} في بوت التسبيح اضغط اسفل على زر *تسبيح* للبدأ".format(name),parse_mode="markdown", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def all(call):
    global count

    if call.data == "tasbeeh":
        count += 1
 
    elif call.data == "reset":
        count = 0

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("• {} •".format(count), callback_data="tasbeeh"))
    markup.add(types.InlineKeyboardButton("تسبيح", callback_data="tasbeeh"))
    markup.add(types.InlineKeyboardButton("تصفير التسبيح", callback_data="reset"))
    
    tz = random.choice(names)
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"*هو الله الذي لا اله الا هو \n( {tz} )*",parse_mode='markdown', reply_markup=markup)


admin = 6454550864 #ايديك
@bot.message_handler(regexp='str')
def start_msg(message):
	bot.reply_to(message,"ارسل كلمة تقييم ")

	
@bot.message_handler(regexp='تقييم')
def tqem(message):
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        telebot.types.InlineKeyboardButton(text='⭐', callback_data='Tqm#1'),
        telebot.types.InlineKeyboardButton(text='⭐⭐', callback_data='Tqm#2'),
        telebot.types.InlineKeyboardButton(text='⭐⭐⭐', callback_data='Tqm#3'),
        telebot.types.InlineKeyboardButton(text='⭐⭐⭐⭐', callback_data='Tqm#4'),
        telebot.types.InlineKeyboardButton(text='⭐⭐⭐⭐⭐', callback_data='Tqm#5')
    )
    bot.send_message(message.chat.id, "قيم البوت", reply_to_message_id=message.message_id, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def all(call):
    name = call.from_user.first_name
    tqm = call.data.split("#")[1]
    bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text=f"مشكوراً على تقييمك للبوت. تقييمك: {tqm}")
    bot.send_message(admin, text=f"عزيزي المطور، قام [{name}](tg://settings) بتقييم البوت. تقييمه: {tqm}",parse_mode="markdown")



@bot.message_handler(commands=['today'])
def send_date(message):
    today = datetime.date.today()
    hijri_date = convert.Gregorian(today.year, today.month, today.day).to_hijri()
    response = f"التاريخ الهجري: {hijri_date}\nالتاريخ الميلادي: {today}"
    bot.reply_to(message, response)
    
    
    
   
headers = {
    'Host': 'restore-access.indream.app',
    'Connection': 'keep-alive',
    'x-api-key': 'e758fb28-79be-4d1c-af6b-066633ded128',
    'Accept': '*/*',
    'Accept-Language': 'ar',
    'Content-Length': '25',
    'User-Agent': 'Nicegram/101 CFNetwork/1404.0.5 Darwin/22.3.0',
    'Content-Type': 'application/x-www-form-urlencoded',
}

@bot.message_handler(commands=['id'])
def start(message):
    keyboard = types.InlineKeyboardMarkup()
    isrs = types.InlineKeyboardButton(text=" ~ ايديي", callback_data="get_id")
    keyboard.add(isrs)
    bot.send_message(message.chat.id, text="مرحبا بك \n الان فقط قم بارسال ايدي الحساب لمعرفه تاريخ الانشاء ✅", reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def t7(message):
    data = '{"telegramId":' + str(message.text) + '}'
    response = requests.post('https://restore-access.indream.app/regdate', headers=headers, data=data).json()
    date = response['data']['date']
    if date:
        mej = f"~ الايدي {message.text}\n ~ تاريخ انشاء الحساب {date}"
        bot.reply_to(message, mej)

@bot.callback_query_handler(func=lambda call: call.data == "get_id")
def get_id(call):
    id_message = f"~ ايديك : {call.message.chat.id}"
    bot.send_message(call.message.chat.id, text=id_message)
    data_Pyro = '{"telegramId":' + str(idd) + '}'
    PyroRobots = requests.post('https://restore-access.indream.app/regdate', headers=headers, data=data_Pyro)

    Pyro = json.loads(PyroRobots.text)
    date = Pyro['data']['date']

    if date:
        bot.reply_to(msg, f'• تاريخ انشاء حسابك علي تليجرام هو {date}')
    else:
        bot.reply_to(msg, 'حدث خطا ، تاكد من ارسال الايدي الخاص بك بشكل صحيح')


########


print('run')
bot.infinity_polling()
