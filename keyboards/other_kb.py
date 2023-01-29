from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def create_kb(*args) -> ReplyKeyboardMarkup:
    kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    kb.add(*[button for button in args])

    return kb

