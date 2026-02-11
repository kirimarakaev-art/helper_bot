from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def main_menu_kb():
    builder = InlineKeyboardBuilder()
    # Добавляем две кнопки в один ряд
    builder.row(
        InlineKeyboardButton(text="💎 Мои проекты", callback_data="my_projects"),
        InlineKeyboardButton(text="📝 Написать мне", callback_data="contact_me")
    )
    # Добавляем кнопку во второй ряд
    builder.row(
        InlineKeyboardButton(text="⚙️ Настройки", callback_data="settings")
    )
    return builder.as_markup()