import asyncio
import os
from aiogram import Bot, Dispatcher
from database import init_db
from handlers import admin, user

async def main():
    bot = Bot(token=os.getenv("TOKEN")) # Đọc token từ biến môi trường của Railway
    dp = Dispatcher()
    
    # Khởi tạo Database
    await init_db()
    
    # Đăng ký các Router
    dp.include_router(admin.router)
    dp.include_router(user.router)
    
    print("Bot đang chạy...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
