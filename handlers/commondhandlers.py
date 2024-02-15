from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from keyboards.all_keyboards import kb_start

commond_router = Router()

@commond_router.message(CommandStart())
async def start_handler(message:Message):
    await message.answer(
        text='Assalomu alaykum.\nXush kelibsiz!',
        reply_markup=kb_start
    )

@commond_router.message(Command('help'))
async def help_handler(message:Message):
    await message.answer(text='Do you need help?')