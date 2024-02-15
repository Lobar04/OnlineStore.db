import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import BotCommand

from config import bot_token
from handlers.commondhandlers import commond_router
from handlers.message_handlers import message_router


async def main():
    bot = Bot(token=bot_token, parse_mode=ParseMode.HTML, disable_web_page_preview=True)
    await bot.set_my_commands(commands=[
        BotCommand(command='start', description='Start/restart bot'),
        BotCommand(command='help', description='Manuel for using bot'),
    ])
    dp = Dispatcher()
    dp.include_routers(commond_router,message_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot stopped')


