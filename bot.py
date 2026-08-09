
import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

users = set()

@bot.message_handler(func=lambda message: True)
def save_user(message):
    users.add(message.from_user.id)

    if message.text == "/all":
        mentions = []

        for user_id in users:
            mentions.append(f"[Kullanıcı](tg://user?id={user_id})")

        if mentions:
            bot.reply_to(
                message,
                " ".join(mentions[:50]),
                parse_mode="Markdown"
            )

print("Bot çalışıyor...")
bot.infinity_polling()
