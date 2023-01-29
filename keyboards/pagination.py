from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from text.text import TEXT_RU


def create_pagination_kb(*buttons: str) -> InlineKeyboardMarkup:
    pagination_kb: InlineKeyboardMarkup = InlineKeyboardMarkup()

    pagination_kb.row(*[InlineKeyboardButton(
        TEXT_RU[button]
        if button in TEXT_RU else button, callback_data=button)
        for button in buttons])
    return pagination_kb


