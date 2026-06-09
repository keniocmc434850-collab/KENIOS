from aiogram import Router, types, F
from aiogram.filters import Command
from database import add_balance

router = Router()
ADMIN_ID = 7741358304  # <--- THAY ID CỦA BẠN VÀO ĐÂY

@router.message(Command("addxu"))
async def cmd_addxu(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        return await message.answer("❌ Bạn không có quyền truy cập!")
    
    args = message.text.split()
    if len(args) < 3:
        return await message.answer("⚠️ Cú pháp: /addxu [ID] [số_xu]")
    
    user_id = int(args[1])
    amount = int(args[2])
    await add_balance(user_id, amount)
    await message.answer(f"✅ Đã cộng {amount} xu cho user {user_id}")
