import aiosqlite

async def init_db():
    async with aiosqlite.connect("bot_data.db") as db:
        await db.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, balance INTEGER)")
        await db.commit()

async def get_balance(user_id):
    async with aiosqlite.connect("bot_data.db") as db:
        async with db.execute("SELECT balance FROM users WHERE user_id = ?", (user_id,)) as cursor:
            row = await cursor.fetchone()
            return row[0] if row else 100000

async def add_balance(user_id, amount):
    current = await get_balance(user_id)
    async with aiosqlite.connect("bot_data.db") as db:
        await db.execute("INSERT OR REPLACE INTO users (user_id, balance) VALUES (?, ?)", (user_id, current + amount))
        await db.commit()
