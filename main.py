import telebot
from telebot import types
from datetime import datetime, timedelta

TOKEN = '8487799319:AAEnohFOagYKOR03bmuf-PDg37R87Lm4HFk'
bot = telebot.TeleBot(TOKEN)

# Расписание на основе твоих файлов (для группы И-1-25)
# 'even' - числитель, 'odd' - знаменатель
SCHEDULE = {
    'even': {  # ЧИСЛИТЕЛЬ
        'Пн': '1. АВС (лек)\n2.Окно\n3. Окно\n4. Окно',
        'Вт': '1. ИСиТ(лек)\n2. I  Окно   |   II ИСиТ(пр)\n3. Англ Яз\n4. История России(пр)\n5. Физкультура(Каратэ)',
        'Ср': '1. АиП(лек)\n2. Выш. Мат. (лек)\n3. Дискретная математика (лек)\n4. Окно \n5. Физкультура(Регби)',
        'Чт': '1. I ВССТ (пр)   |   II Окно\n2. I АиП (пр)   | II Кр. Тат.\n3. I Кр. Тат.   | II АиП.\n4. Выш. Мат.\n5. Окно',
        'Пт': '1. История России (лек)\n2. История России (лек)\n3.I АВС (пр)   | II ВССТ (пр)\n4. Физкультура(Регби)'
    },
    'odd': {  # ЗНАМЕНАТЕЛЬ
        'Пн': '1. Ист. религий России (лек)\n2. Ист. религий России (лек)\n3.Ист. религий России (сем)\n4. I ИСиТ (пр)   | II Окно',
        'Вт': '1. I ИСиТ (пр)   | II Окно\n2. I  Окно   |   II ИСиТ(пр)\n3. Англ. Яз.\n4. ВССТ (лек)\n5. Физкультура(Каратэ)',
        'Ср': '1. Эконом. теория (лек)\n2. Выш. Мат. (лек)\n3. Окно\n4. Дискретная математика (пр)\n5. Физкультура(Регби)',
        'Чт': '1. I ВССТ (пр)   |   II Окно\n2. I АиП (пр)   | II Окно\n3. I Окно   | II АиП.\n4. Выш. Мат.\n',
        'Пт': '1. Окно\n2. Эконом. теория (пр)\n3. I АВС (пр)   | II ВССТ (пр)\n4. Физкультура(Регби)'
    }
}

DAYS_MAP = {0: 'Пн', 1: 'Вт', 2: 'Ср', 3: 'Чт', 4: 'Пт', 5: 'Сб', 6: 'Вс'}

def get_week_type(target_date=None):
    if target_date is None:
        target_date = datetime.now()
    week_num = target_date.isocalendar()[1]
    # По твоему календарю: числитель (even) - четные недели, знаменатель (odd) - нечетные
    return 'even' if week_num % 2 == 0 else 'odd'

def make_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(types.KeyboardButton('📅 Сегодня'), types.KeyboardButton('➡️ Завтра'))
    days = [types.KeyboardButton(d) for d in ['Пн', 'Вт', 'Ср', 'Чт', 'Пт']]
    markup.add(*days)
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    w_type = "ЧИСЛИТЕЛЬ (четная)" if get_week_type() == 'even' else "ЗНАМЕНАТЕЛЬ (нечетная)"
    bot.send_message(message.chat.id, f"Бот готов! Сейчас неделя: {w_type}", reply_markup=make_keyboard())

@bot.message_handler(func=lambda m: True)
def handle_msg(message):
    now = datetime.now()
    if message.text == '📅 Сегодня':
        day = DAYS_MAP[now.weekday()]
        show_day(message, day, get_week_type(), "сегодня")
    elif message.text == '➡️ Завтра':
        tomorrow = now + timedelta(days=1)
        day = DAYS_MAP[tomorrow.weekday()]
        show_day(message, day, get_week_type(tomorrow), "завтра")
    elif message.text in DAYS_MAP.values():
        show_day(message, message.text, get_week_type(), message.text)

def show_day(message, day_name, week_type, label):
    if day_name in ['Сб', 'Вс']:
        bot.send_message(message.chat.id, f"На {label} расписания нет!")
        return
    
    sched_text = SCHEDULE[week_type].get(day_name, "Пар нет")
    header = "📈 ЧИСЛИТЕЛЬ" if week_type == 'even' else "📉 ЗНАМЕНАТЕЛЬ"
    bot.send_message(message.chat.id, f"📅 *{label.upper()}* ({header}):\n\n{sched_text}", parse_mode="Markdown")

if __name__ == "__main__":
    bot.infinity_polling()