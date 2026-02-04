import telebot

# Вставь сюда API Token, который тебе дал @BotFather
TOKEN = '8579710701:AAHVbI-Yu36CcKq3VKJ3gNjhm8gdxyAC2AA'

bot = telebot.TeleBot(TOKEN)

# Ответ на команду /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "Селям! Я твой первый бот.\n"
        "Отправь мне любую фразу, и я отвечу тебе как настоящий ногай!"
    )
    bot.reply_to(message, welcome_text)

# Обработка текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    user_text = message.text
    
    # Небольшая "ногаизация" для примера: заменяем 'и' на 'иги' или добавляем колорит
    if "привет" in user_text.lower():
        reply = "Селям, амансынъыз ба!"
    elif "как дела" in user_text.lower():
        reply = "Бек иги, сав болынъыз! Оьзинъизде не хабер?"
    else:
        # Просто повторяем текст пользователя с припиской
        reply = f"Сен дединъ: «{user_text}». Бек иги!"

    bot.send_message(message.chat.id, reply)

# Запуск бота
if __name__ == "__main__":
    print("Бот запущен...")
    bot.infinity_polling()