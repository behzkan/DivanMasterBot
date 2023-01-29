from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def create_category_kb(categories: dict) -> InlineKeyboardMarkup:
    categories_kb = InlineKeyboardMarkup(row_width=2)

    categories_kb.add(
        *[InlineKeyboardButton(value, callback_data=f'{key}_category') for key, value in categories.items()]
        )

    return categories_kb

