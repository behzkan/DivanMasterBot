from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def create_main_kb(buttons: dict) -> ReplyKeyboardMarkup:
    main_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True )
    main_kb.add(*[KeyboardButton(button) for key, button in buttons.items()])
    return main_kb


