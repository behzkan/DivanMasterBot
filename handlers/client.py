# from aiogram import Dispatcher, types
# from aiogram.types import ReplyKeyboardRemove
# from aiogram.dispatcher.filters import Text
# from keyboards.kb_client import *
# from construct_bot import bot
# import db
#
#
#
#
#
# async def products_category(msg: types.Message):
#
#     await msg.answer('<i>👀 Что вас интересует?</i>',
#                      parse_mode=types.ParseMode.HTML, reply_markup=ReplyKeyboardRemove())
#     await msg.answer('<i>✨ Выберите категорию или воспользуйтесь поиском</i>, <b>/search</b>', reply_markup=ikb_products_category(),
#                      parse_mode=types.ParseMode.HTML)
#
# async def call_get_product(call: types.CallbackQuery):
#     category_id = call.products_data
#     cursor, connection = db.get_connection()
#
#     cursor.execute('select * from ')
#     await call.answer()
#
# async def reference_information(msg: types.Message):
#     await msg.answer("""
#     <pre>Вы можете выбрать товары и оформить заказ онлайн или позвонить в отдел продаж: \n менеджеры
# проконсультируют вас, примут заказ и оформят доставку удобным для вас способом.</pre>
# """, reply_markup=kb_reference_information(), parse_mode=types.ParseMode.HTML)
#
#
#
# async def back_to_main(msg: types.Message):
#     await msg.answer('Вы находитесь в главном меню', reply_markup=kb_main())
#
# async def delivery_condition(msg: types.Message):
#     await msg.answer("""
#     Мы осуществляем доставку по всему <b>Казахстану</b>, а также по <b>СНГ</b>.
#
#         <b>Cроки доставки по Казахстану 🇰🇿:</b>
#
#                 <u>Астана, Караганда, Темиртау</u> - <b>1-3 дня</b>
#                 <u>Актобе, Актау, Атырау, Уральск</u> — <b>6-10 дней</b>
#                Костанай, Кокшетау, Павлодар, Петропавловск, Семей, Усть-Каменогорск, Шымкент, Тараз, Жезказган, Сатпаев, Кызылорда - <b>2-5 дней</b>
#
#     """, parse_mode=types.ParseMode.HTML, disable_web_page_preview=True, reply_markup=kb_main_back('ℹ Справочная информация'))
#
#     await msg.answer("""
#          <b><i>Условие доставки по СНГ и  другим странам:
#                 🇦🇿 🇦🇲 🇧🇾 🇰🇬 🇲🇩 🇷🇺 🇹🇯 🇺🇿 :</i></b>
#
#                 Доставка осуществляется транспортными компаниями -  Энергия, Gtdel. Сроки доставки в среднем <pre>5-12 дней</pre>.
#
#         """, parse_mode=types.ParseMode.HTML, disable_web_page_preview=True)
#     await msg.answer("""
#         <i>Если сумма заказа меньше <u>20000₸</u> тогда  доставляются только через курьерские службы или самовывоз.</i>
#         🚶 Самовывоз со склада <a href="https://go.2gis.com/y8i6uc">Алматы, Масанчи 23г/1</a>
#         """, parse_mode=types.ParseMode.HTML, disable_web_page_preview=True)
#
# async def favorites(msg: types.Message):
#     await msg.answer('У вас пока нет избранных товаров.')
#     await msg.answer('Нажимайте на ♡ возле товаров, чтобы не потерять их')
#
# async def payment_method(msg: types.Message):
#     await msg.answer(msg.text)
#     await msg.answer("""<b>
#                     💰 Наличными
# 💳 Платежной картой <pre>(POS-терминал, Visa или MasterCard)</pre>
# 🟥 А также с помощью Kaspi QR</b>""", parse_mode=types.ParseMode.HTML, reply_markup=kb_to_main())
#
#
# async def currency(msg: types.Message):
#     await msg.answer('Выберите курс:', reply_markup=ikb_currency_list())
#
# async def address(msg: types.Message):
#     await msg.answer("""
#
#
#
#     """, parse_mode=types.ParseMode.HTML)
#
#     await bot.send_location(msg.from_user.id, 43.26072, 76.927077)
#
# async def contacts(msg: types.Message):
#     await bot.send_contact(msg.from_user.id, '+7 (705) 525-96-90', 'Berik')
#     await bot.send_contact(msg.from_user.id, '+7 (700) 200-47-33', 'Bek', reply_markup=ikb_contacts())
#
# async def call_get_product(call: types.CallbackQuery):
#     await call.message.answer('He')
#     await call.answer()
#
#
# def register_handlers_client(dp: Dispatcher):
#     dp.register_message_handler(cmd_start, commands='start')
#     dp.register_message_handler(products_category, Text(equals='📦 Наши товары'))
#     dp.register_message_handler(back_to_main, Text(equals='🏠 Вернуться на главную'))
#     dp.register_message_handler(delivery_condition, Text(equals='🚚 Условие доставки'))
#     dp.register_message_handler(payment_method, Text(equals='💳 Способы оплаты'))
#     dp.register_message_handler(reference_information, Text(equals='ℹ Справочная информация'))
#     dp.register_message_handler(favorites, Text(equals='♡ Избранное'))
#     dp.register_message_handler(currency, Text(equals='💱 Курсы валют'))
#     dp.register_message_handler(contacts, Text(equals='📞 Контакты'))
#     dp.register_message_handler(address, Text(equals='🗺 Мы на карте'))
#     dp.register_callback_query_handler(call_get_product)
#
#
#
