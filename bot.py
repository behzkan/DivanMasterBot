from aiogram import Bot, types
from aiogram import Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils import executor


TOKEN = '5694324132:AAHbPms9rMlqXjt66rHCHlaTH2nd_z3c_28'

bot = Bot(TOKEN)
dp = Dispatcher(bot)

# client
@dp.message_handler(commands=['start'])
async def start_cmd(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'Добрый день!', reply_markup=main_kb)

@dp.message_handler()
async def s(msg: types.Message):

    if 'контакты' in msg.text.lower():
        await bot.send_message(msg.from_user.id, '[Наш сайт](https://divanmaster.kz/)', parse_mode='Markdown')
        await bot.send_message(msg.from_user.id, "[Наш инстаграм](https://www.instagram.com/divanmaster.kz/)", parse_mode='Markdown')
        await bot.send_message(msg.from_user.id, "[Связаться с менеджером](wa.me/+77763030317)", parse_mode='Markdown')
    elif 'нас' in msg.text.lower():
        await  bot.send_message(msg.from_user.id, '*Мы молодая успешно развивающаяся компания, занимаемся поставкой\
        нестандартной фурнитуры для изготовителей мебели в РК и по СНГ*', parse_mode='Markdown')

    elif 'адрес' in msg.text.lower():
        await bot.send_message(msg.from_user.id, 'ул.Масанчи 23г/1, Алматы, Казахстан')
        await bot.send_message(msg.from_user.id, 'График работы: \n \
                                *ПН - ПТ 09:00 - 17:30* \n \
                                         *СБ 10:00 - 13:00*', parse_mode='Markdown')
        await bot.send_message(msg.from_user.id, '{:>30}'.format('hello'))
 # keyboards

kb_search = KeyboardButton('🔍 Поиск товаров')
kb_checkout = KeyboardButton('📋 Оформить заказ')
kb_shopping_cart = KeyboardButton('🛒 Корзина')
kb_contacts = KeyboardButton('🧑🏻‍💻 Контакты')
kb_about = KeyboardButton('🌐 О нас')
kb_address = KeyboardButton('🗺 Адрес')
kb_back = KeyboardButton('🏠  Вернуться в меню')



main_kb = ReplyKeyboardMarkup(resize_keyboard=True)

main_kb.row(kb_shopping_cart, kb_contacts)
main_kb.add(kb_search)
main_kb.row(kb_address, kb_about)

executor.start_polling(dp, skip_updates=True)

