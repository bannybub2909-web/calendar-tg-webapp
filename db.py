import aiosqlite

DB_NAME = "calendar.db"

async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            date TEXT,
            text TEXT
        )
        """)
        await db.commit()

async def add_note(user_id: int, date: str, text: str):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "INSERT INTO notes (user_id, date, text) VALUES (?, ?, ?)",
            (user_id, date, text)
        )
        await db.commit()

async def get_notes(user_id: int, date: str):
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute(
            "SELECT text FROM notes WHERE user_id=? AND date=?",
            (user_id, date)
        )
        return await cursor.fetchall()
