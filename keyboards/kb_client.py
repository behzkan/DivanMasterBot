# from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
#
# products_category = []
#
# try:
#     cursor, connection = db.get_connection()
#     cursor.execute('select * from category')
#     for i in cursor:
#         products_category.append(i)
# except db.Error as e:
#     print('error on db category', e)
#
# def ikb_products_category():
#     ibtns = []
#
#     for category in products_category:
#         ibtns.append(InlineKeyboardButton(text=f'{category[1]}', callback_data=f'{category[0]}'))
#
#     ikb = InlineKeyboardMarkup(row_width=2)
#     for ibtn in ibtns:
#         ikb.insert(ibtn)
#     return ikb
#
#
# def ikb_currency_list():
#     ikb = InlineKeyboardMarkup().add(*[
#         InlineKeyboardButton(text='KGS - KZT', callback_data="rub_kzt"),
#         InlineKeyboardButton(text='RUB - KZT', callback_data="kgs_kzt")])
#     return ikb
#
# def ikb_contacts():
#     ikb = InlineKeyboardMarkup().add(*[
#         InlineKeyboardButton(text='Whatsapp', url='http://wa.me/+77002004733'),
#         InlineKeyboardButton(text='Наш Instgram', url='http://instagram.com')
#
#     ])
#     return  ikb
#
# #
# #
# def kb_main():
#     kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#
#
#
#     kb.row(btn_products)
#     kb.add(
#         btn_shopping_cart,
#         btn_services,
#         btn_exchange,
#         btn_contacts
#     )
#     kb.add(
#         btn_info,
#
#     ).add(
#         btn_favorites,
#         btn_address
#     )
#
#     return kb
#
# def kb_to_main():
#     kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#
#     btn_to_main = KeyboardButton('🏠 Вернуться на главную')
#     kb.add(btn_to_main)
#     return kb
#
# def kb_main_back(to):
#
#     kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     btn_to_main = KeyboardButton('🏠 Вернуться на главную')
#
#     return kb
#
#
# def kb_reference_information():
#         kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#         btn_delivery = KeyboardButton('🚚 Условие доставки')
#         btn_payment = KeyboardButton('💳 Способы оплаты')
#         btn_to_main = KeyboardButton('🏠 Вернуться на главную')
#         kb.add(
#             btn_delivery,
#             btn_payment,
#             btn_to_main
#         )
#         return kb
#
# def kb_company():
#     kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#
#     btn_about = KeyboardButton('🌐 О нас')
#     btn_address = KeyboardButton('🗺 Наш адрес')
#     btn_contacts = KeyboardButton('📞 Контакты')
#     kb.add(
#         btn_about,
#         btn_address,
#         btn_contacts,
#     )
#
#     return kb