import asyncio
import logging

from aiogram import Dispatcher, Bot

from config_data.config import Config, load_config
from handlers.categories_handler import register_msg_handler
from handlers.user_handlers import register_msg_handlers
from keyboards.bot_commands import set_commands
from products_data.products_data import load_products

logger = logging.getLogger(__name__)








def register_all_handlers(dp: Dispatcher) -> None:
    register_msg_handler(dp)
    register_msg_handlers(dp)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s '
               u'[%(asctime)s] - %(name)s - %(message)s')

    logger.info('Starting bot')

    config: Config = load_config(None)

    bot: Bot = Bot(config.tgBot.token, parse_mode='HTML', disable_web_page_preview=True)
    dp: Dispatcher = Dispatcher(bot)

    await set_commands(dp)

    register_all_handlers(dp)
    load_products('products_data/products.json')
    try:
        await dp.start_polling()
    finally:
        await bot.close()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except(KeyboardInterrupt, SystemExit):
        logger.error('Bot stopped')










# Мы занимаемся поставкой нестандартной фурнитуры для изготовителей мебели в РК и по СНГ
#    Ножки бывают разной высоты, моделей и цветов - чтобы вы могли найти свой индивидуальный стиль!
#  Мы поможем подобрать комплектующие
# для мебели под ваши задачи

# После оформления заказа с вами свяжется наш менеджер для уточнения деталей.