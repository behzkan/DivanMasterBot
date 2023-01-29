from aiogram import Dispatcher, types

from text.text import TEXT_RU


async def set_commands(dp: Dispatcher):
    bot_commands = [
        types.BotCommand(command='start', description='Перезапустить бота'),
        types.BotCommand(command='bookmark', description=TEXT_RU['bookmark']),
        types.BotCommand(command='help', description='Help'),
        types.BotCommand(command='next', description='next'),
]
    await dp.bot.set_my_commands(bot_commands)

