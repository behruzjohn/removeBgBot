import telebot, requests, io

TOKEN = "7569794171:AAHc-P4ilg7tujauHjkSoJo5O02rI-rEZ88"
API_KEY = "S8Wdntg9HbQP2bs8oKf3uaP6"
ADMIN_ID = 1799220737

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id,
    "👤 *Behruzjon haqida ma’lumotlar:*\n\n"
    "🔹 Telegram: [@Behruzjon6789](https://t.me/Behruzjon6789)\n"
    "📱 Telefon: +998 99 484 67 89\n"
    "📷 Instagram: [@behruzjon_010_](https://instagram.com/behruzjon_010_)\n\n"
    "⚠️ Ushbu ma’lumotlar maxsus kod orqali ko‘rinadi.",
    parse_mode="Markdown"
)



@bot.message_handler(func=lambda message: message.text and message.text.lower() == "6789")
def check_code(message):
   bot.send_message(message.chat.id,
    "👤 *Behruzjon haqida ma’lumotlar:*\n\n"
    "🔹 Telegram: [@Behruzjon6789](https://t.me/Behruzjon6789)\n"
    "📱 Telefon: +998 99 484 67 89\n"
    "📷 Instagram: [@behruzjon_010_](https://instagram.com/behruzjon_010_)\n\n"
    "⚠️ Ushbu ma’lumotlar maxsus kod orqali ko‘rinadi.",
    parse_mode="Markdown"
)



@bot.message_handler(func=lambda message: message.text and message.text.strip().startswith("@"))
def forward_username_to_admin(message):
    username = message.text.strip()

    bot.send_message(ADMIN_ID,
        f"📩 Yangi username yuborildi:\n"
        f"🔸 Username: {username}\n"
        f"👤 Foydalanuvchi: {message.from_user.first_name}\n"
        f"🆔 Telegram ID: {message.from_user.id}"
    )
    bot.send_message(message.chat.id, "✅ Username qabul qilindi. Rahmat!")

@bot.message_handler(content_types=['photo'])
def remove_bg(message):
    try:
        file_info = bot.get_file(message.photo[-1].file_id)
        file = bot.download_file(file_info.file_path)

        response = requests.post(
            "https://api.remove.bg/v1.0/removebg",
            files={"image_file": io.BytesIO(file)},
            data={"size": "auto"},
            headers={"X-Api-Key": API_KEY},
        )

        if response.status_code == 200:
            output = io.BytesIO(response.content)
            output.name = "output.png"
            bot.send_document(message.chat.id, output)
        else:
            bot.send_message(message.chat.id, f"❌ Xatolik yuz berdi:\n{response.status_code} - {response.text}")

    except Exception as e:
        bot.send_message(message.chat.id, f"⚠️ Botda xatolik: {e}")

bot.polling()
