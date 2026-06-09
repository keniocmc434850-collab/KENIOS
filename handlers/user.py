from aiogram import Router, types, F
from aiogram.filters import Command
from database import get_balance

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Chào mừng bạn đến với Bot! Dùng /menu để xem tính năng.")

@router.message(Command("ví"))
async def cmd_wallet(message: types.Message):
    balance = await get_balance(message.from_user.id)
    await message.answer(f"💰 Số dư của bạn: {balance} xu")

@router.message(F.text.regexp(r"https?://\S+"))
async def anti_link(message: types.Message):
    await message.delete()
    await message.answer("❌ Không được gửi link trong nhóm!")
