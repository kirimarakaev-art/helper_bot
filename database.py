import aiosqlite

DB_NAME = "bot_database.db"

async def create_db():
    async with aiosqlite.connect(DB_NAME) as db:
        # Создаем таблицу пользователей, если её еще нет
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                user_name TEXT,
                age INTEGER
            )
        """)
        await db.commit()

async def add_user(user_id: int, user_name: str, age: int):
    async with aiosqlite.connect(DB_NAME) as db:
        # Добавляем или обновляем данные пользователя
        await db.execute(
            "INSERT OR REPLACE INTO users (user_id, user_name, age) VALUES (?, ?, ?)",
            (user_id, user_name, age)
        )
        await db.commit()