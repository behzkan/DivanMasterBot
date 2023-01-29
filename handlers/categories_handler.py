from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery, InputMediaPhoto, ReplyKeyboardRemove

from database.database import user_db
from keyboards.other_kb import create_kb
from keyboards.pagination import create_pagination_kb
from services.services import get_products_by_category, generate_product_info
from text.text import TEXT_RU


async def category_handler(callback: CallbackQuery):
    get_products_by_category(callback.data, callback.from_user.id)
    products = user_db[callback.from_user.id]["watching"]
    user_db[callback.from_user.id]["watching"]["current_item"] = 0
    current_item = user_db[callback.from_user.id]["watching"]["current_item"]

    try:
        photo = open(
            f'{products["products"][current_item]["img"]}/{(products["products"][current_item]["item"]).replace("/", "_")}_main.jpg', 'rb')
        call = await callback.message.answer_photo(photo)
        await call.edit_caption(generate_product_info(products["products"][current_item]),
                          reply_markup=create_pagination_kb(
                              'backward',
                              f'{current_item + 1}/{products["products_count"]}⭐',
                              'forward'
                          ))
    except Exception as e:
        photo = open('img/no.jpg', 'rb')
        call = await callback.message.answer_photo(photo)
        await call.edit_caption(generate_product_info(products["products"][products["current_item"]]),
                                            reply_markup=create_pagination_kb(
                                                'backward',
                                                f'{products["current_item"] + 1}/{products["products_count"]}⭐',
                                                'forward'
                                            ))
    await callback.answer('Загружается...')


async def cmd_press_backward(callback: CallbackQuery):
    products = user_db[callback.from_user.id]["watching"]
    if products["current_item"] > 0:
        user_db[callback.from_user.id]["watching"]["current_item"] -= 1
        current_item = user_db[callback.from_user.id]["watching"]["current_item"]
        try:
            photo = open(
                f'{products["products"][current_item]["img"]}/{(products["products"][current_item]["item"]).replace("/", "_")}_main.jpg',
                'rb')
            call = await callback.message.edit_media(InputMediaPhoto(photo))
            await call.edit_caption(generate_product_info(products["products"][current_item]),
                                    reply_markup=create_pagination_kb(
                                        'backward',
                                        f'{products["current_item"] + 1}/{products["products_count"]}⭐',
                                        'forward'
                                    ))
        except Exception as e:
            photo = open('img/no.jpg', 'rb')
            await callback.message.edit_media(InputMediaPhoto(photo))
            await callback.message.edit_caption(generate_product_info(products["products"][products["current_item"]]),
                                                reply_markup=create_pagination_kb(
                                                    'backward',
                                                    f'{products["current_item"] + 1}/{products["products_count"]}⭐',
                                                    'forward'
                                                ))
        await callback.answer('Загружается...')
    await callback.answer()

async def cmd_press_forward(callback: CallbackQuery):
    products = user_db[callback.from_user.id]["watching"]
    if products["current_item"] < products["products_count"] - 1:
        user_db[callback.from_user.id]["watching"]["current_item"] += 1
        current_item = user_db[callback.from_user.id]["watching"]["current_item"]
        try:
            photo = open(
                f'{products["products"][current_item]["img"]}/{(products["products"][current_item]["item"]).replace("/", "_")}_main.jpg',
                'rb')
            call = await callback.message.edit_media(InputMediaPhoto(photo))
            await call.edit_caption(generate_product_info(products["products"][products["current_item"]]),
                                                reply_markup=create_pagination_kb(
                                                    'backward',
                                                    f'{products["current_item"] + 1}/{products["products_count"]}⭐',
                                                    'forward'
                                                ))
        except Exception as e:
            photo = open('img/no.jpg', 'rb')
            await callback.message.edit_media(InputMediaPhoto(photo))
            await callback.message.edit_caption(generate_product_info(products["products"][products["current_item"]]),
                                          reply_markup=create_pagination_kb(
                                              'backward',
                                              f'{products["current_item"] + 1}/{products["products_count"]}⭐',
                                              'forward'
                                          ))
        await callback.answer('Загружается...')
    await callback.answer()

async def process_page_press(callback: CallbackQuery):
    current_item = user_db[callback.from_user.id]["watching"]["current_item"]
    user_db[callback.from_user.id]["bookmarks"].add(
        user_db[callback.from_user.id]["watching"]["products"][current_item]["item"]
    )
    await callback.answer('Товар добавлена в избранное!')


def register_msg_handler(dp: Dispatcher):
    dp.register_callback_query_handler(cmd_press_backward, text='backward')
    dp.register_callback_query_handler(cmd_press_forward, text='forward')
    dp.register_callback_query_handler(category_handler, Text(contains='category'))
    dp.register_callback_query_handler(process_page_press)