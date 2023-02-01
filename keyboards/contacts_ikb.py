from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from text.text import TEXT_RU


def create_contacts_ikb(contacts: dict) -> InlineKeyboardMarkup:
    contacts_ikb: InlineKeyboardMarkup = InlineKeyboardMarkup(row_width=2)

    contacts_ikb.add(*[InlineKeyboardButton(name, f'{TEXT_RU["link_wa"]}{number}') for name, number in contacts.items()])
    return contacts_ikb
