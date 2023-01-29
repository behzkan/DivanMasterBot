from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from text.text import TEXT_RU


def create_start_kb(*buttons) -> InlineKeyboardMarkup:
    start_kb: InlineKeyboardMarkup = InlineKeyboardMarkup()
    start_kb.row(*[InlineKeyboardButton(text=TEXT_RU[button], callback_data=button) for button in buttons])

    return start_kb
