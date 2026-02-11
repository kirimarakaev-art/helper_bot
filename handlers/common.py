from aiogram import Router, types, F
from aiogram.filters import Command
# Импортируем нашу функцию клавиатуры
from keyboards.inline import main_menu_kb 

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        f"Рад видеть тебя, {message.from_user.first_name}!\n"
        "Я готов помогать. Выбери нужный раздел ниже:",
        reply_markup=main_menu_kb() # Прикрепляем кнопки
    )

# Обработка нажатия на кнопку "Мои проекты"
@router.callback_query(F.data == "my_projects")
async def show_projects(callback: types.CallbackQuery):
    await callback.message.answer("Тут будет список твоих крутых репозиториев с GitHub!")
    # Важно: всегда отвечай на колбэк, чтобы убрать эффект загрузки
    await callback.answer()


