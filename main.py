import telebot
from telebot import types

TOKEN = '8579710701:AAHVbI-Yu36CcKq3VKJ3gNjhm8gdxyAC2AA'
bot = telebot.TeleBot(TOKEN)

# 1. Твоё расписание (заполни его своими предметами)
SCHEDULE = {
    'Пн': '1. Математика\n2. История\n3. Физкультура',
    'Вт': '1. Информатика\n2. Английский\n3. Физика',
    'Ср': '1. Литература\n2. География\n3. Химия',
    'Чт': '1. Биология\n2. Обществознание\n3. ОБЖ',
    'Пт': '1. Родной язык\n2. Технология\n3. Искусство',
    'Сб': 'Пар нет. Отдыхай! 😎'
}

# Функция для создания клавиатуры
def make_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Создаем кнопки (можно по 2-3 в ряд)
    btn1 = types.KeyboardButton('Пн')
    btn2 = types.KeyboardButton('Вт')
    btn3 = types.KeyboardButton('Ср')
    btn4 = types.KeyboardButton('Чт')
    btn5 = types.KeyboardButton('Пт')
    btn6 = types.KeyboardButton('Сб')
    
    markup.add(btn1, btn2, btn3)
    markup.add(btn4, btn5, btn6)
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id, 
        "Привет! Выбери день недели, чтобы узнать расписание:", 
        reply_markup=make_keyboard()
    )

@bot.message_handler(func=lambda message: message.text in SCHEDULE.keys())
def show_schedule(message):
    day = message.text
    response = f"📅 *Расписание на {day}:*\n\n{SCHEDULE[day]}"
    bot.send_message(message.chat.id, response, parse_mode="Markdown")

# На случай, если пользователь напишет что-то другое
@bot.message_handler(func=lambda message: True)
def other(message):
    bot.send_message(message.chat.id, "Пользуйся кнопками внизу! 👇", reply_markup=make_keyboard())

if __name__ == "__main__":
    bot.infinity_polling()