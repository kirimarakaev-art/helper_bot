from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram import Router, types, F
from aiogram.filters import Command
from database import add_user



router = Router()



# 1. Определяем состояния
class Survey(StatesGroup):
    name = State()    # Будем ждать имя
    age = State()     # Будем ждать возраст





# 2. Хендлер для начала опроса (например, по кнопке "Написать мне")
@router.callback_query(F.data == "contact_me")
async def start_survey(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Давай познакомимся! Как тебя зовут?")
    # Переводим пользователя в состояние "ожидания имени"
    await state.set_state(Survey.name)
    await callback.answer()




# 3. Ловим имя и спрашиваем возраст
@router.message(Survey.name)
async def process_name(message: types.Message, state: FSMContext):
    # Сохраняем имя в память
    await state.update_data(chosen_name=message.text)
    await message.answer(f"Приятно познакомиться, {message.text}! А сколько тебе лет?")
    # Переходим к следующему состоянию
    await state.set_state(Survey.age)





# 4. Ловим возраст и финализируем
@router.message(Survey.age)
async def process_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Введи возраст цифрами!")
        return

    user_data = await state.get_data()
    name = user_data.get("chosen_name")
    age = int(message.text)

    # СОХРАНЯЕМ В БАЗУ ДАННЫХ
    await add_user(message.from_user.id, name, age)

    await message.answer(f"Данные сохранены! Теперь я тебя помню, {name}.")
    await state.clear()

    age_num = int(message.text)
    if age_num < 5 or age_num > 100:
        await message.answer("Что-то не верится... Введи реальный возраст:")
        return

    # Если всё ок, идем дальше
    user_data = await state.get_data()
    await message.answer(
        f"Регистрация завершена!\n"
        f"Имя: {user_data.get('chosen_name')}\n"
        f"Возраст: {age_num}"
    )
    await state.clear()