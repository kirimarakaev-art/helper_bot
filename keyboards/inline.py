from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def main_menu_kb(): # Проверь это имя!
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="💎 Мои проекты", callback_data="my_projects"),
        InlineKeyboardButton(text="📝 Написать мне", callback_data="contact_me")
    )
    return builder.as_markup()