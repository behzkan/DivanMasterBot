from copy import deepcopy

from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery, InputMediaPhoto

from database.database import user_db, user_data, products_category
from keyboards.categories_kb import create_category_kb
from keyboards.main_kb import create_main_kb
from keyboards.other_kb import create_kb
from services.services import get_bookmarks
from text.text import TEXT_RU


async def cmd_start(msg: Message):
    await msg.answer(TEXT_RU[msg.text],
                     reply_markup=create_main_kb(TEXT_RU['main']))

    if msg.from_user.id not in user_db:
        user_db[msg.from_user.id] = deepcopy(user_data)


async def cmd_products(msg: Message):
    await msg.answer(TEXT_RU['downloading'], reply_markup=create_kb(TEXT_RU['return_home']))
    await msg.answer(TEXT_RU['select_category'], reply_markup=create_category_kb(products_category))


async def cmd_home(msg: Message):
    await msg.answer(TEXT_RU['home'], reply_markup=create_main_kb(TEXT_RU['main']))


async def bookmarks(msg: Message):
    await msg.answer(TEXT_RU['bookmark'])
    bookmarks_list = get_bookmarks(msg.from_user.id)
    for bookmark in bookmarks_list:
        await msg.answer(f'<pre>{bookmark}</pre>')

async def cmd_contacts(msg: Message):
    await msg.answer_contact('+77763030317', 'Bekzhan')

async def cmd_location(msg: Message):
    await msg.answer(TEXT_RU['location'])
    await msg.answer_location(43.26072, 76.927077)



def register_msg_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands='start')
    dp.register_message_handler(cmd_products, text=TEXT_RU['main']['btn_products'])
    dp.register_message_handler(cmd_home, text=TEXT_RU['return_home']),
    dp.register_message_handler(bookmarks, text=TEXT_RU['bookmark'])
    dp.register_message_handler(cmd_contacts, text=TEXT_RU['main']['btn_company_contacts'])
    dp.register_message_handler(cmd_location, text=TEXT_RU['main']['btn_location'])
