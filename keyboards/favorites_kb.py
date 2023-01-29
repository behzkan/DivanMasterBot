from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from products_data.products_data import products_data
from text.text import TEXT_RU


def create_favorites_kb(*args: int) -> InlineKeyboardMarkup:
    favorites_kb: InlineKeyboardMarkup = InlineKeyboardMarkup()

    for button in sorted(args):
        favorites_kb.add(InlineKeyboardButton(
            f'{button} - {products_data["products"][button]["title"]}',
            callback_data=str(button)))
    favorites_kb.add(
        InlineKeyboardButton(TEXT_RU['edit_bookmarks_button'], callback_data='edit_favorites'),
        InlineKeyboardButton(TEXT_RU['cancel'], callback_data='cancel'),
    )

    return favorites_kb

def  create_edit_kb(*args: int) -> InlineKeyboardMarkup:
    bookmarks_kb: InlineKeyboardMarkup = InlineKeyboardMarkup()

    for button in sorted(args):
        bookmarks_kb.add(InlineKeyboardButton(
            f'{TEXT_RU["del"]} {button} - {products_data["products"][button]["title"]}',
            callback_data=f'{button}del'
        ))
    bookmarks_kb.add(InlineKeyboardButton(
                     TEXT_RU['cancel'], callback_data='cancle'))
    return bookmarks_kb


