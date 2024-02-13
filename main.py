import requests
from telebot.types import Message
from telebot import TeleBot

token = "6418845303:AAGV-jU1GiVv21Z44awdtN2f2ULwz_bkz2Q"
bot = TeleBot(token)
API = 'https://nsssar.tk/photo/photo.php'

@bot.message_handler(commands=["start"])
def start(message: Message):
    bot.reply_to(message, "Please send an image to convert to an anime.")

@bot.message_handler(content_types=["photo"])
def receiver(message: Message):
    file_id = message.photo[2].file_id
    file_url = bot.get_file_url(file_id)
    params = {"almortagel": file_url}
    response = requests.post(API, params=params).json()
    bot.send_photo(chat_id=message.chat.id, photo=response["image"])

print(bot.get_me().username)
bot.infinity_polling()
