from aiogram import Router, F
from aiogram.types import Message

from config import db_name
from keyboards.all_keyboards import get_categories, kb_start
from utils.database import Database

db = Database(db_name)
message_router = Router()

@message_router.message(F.text == 'Categories')
async def category_handler(message: Message):
    await message.answer(
        text='Select category, please...',
        reply_markup=get_categories())

@message_router.message(F.text.in_({'Smartphones', 'Notebooks','IPads','Kindle'}))
async def product_handler(message: Message):
    cats = db.get_categories()
    for cat in cats:
        if message.text == cat[1]:
            products = db.get_products(cat[0])
            break
    await message.answer_photo(
        photo=products[0][4],
        caption=f'<b>{products[0][1]}:</b>\n\n{products[0][3]}'
    )


