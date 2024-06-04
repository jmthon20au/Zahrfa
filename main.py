pip install python-telegram-bot PyGithub
import os
from telegram.ext import Updater, CommandHandler
from github import Github

# استبدال 'TOKEN' بتوكن البوت الخاص بك
updater = Updater("7292751852:AAGOLGQicGpA1LnWjtzm0wBqr7BtCKOFRGQ", use_context=True)

# استبدال 'GITHUB_TOKEN' بتوكن وصول القارئ الذي يتم إنشاؤه من صفحة الإعدادات الشخصية على GitHub
github_token = os.getenv('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')
g = Github(github_token)

# وظيفة للحصول على معلومات مستودع معين
def get_repo_info(update, context):
    repo_name = context.args[0]
    repo = g.get_repo(repo_name)
    repo_info = f"اسم المستودع: {repo.name}\nوصف المستودع: {repo.description}\nعدد النجوم: {repo.stargazers_count}"
    update.message.reply_text(repo_info)

# إضافة معالج للأمر /repo
updater.dispatcher.add_handler(CommandHandler("repo", get_repo_info))

# تشغيل البوت
updater.start_polling()
updater.idle()
