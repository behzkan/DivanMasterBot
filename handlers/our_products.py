from aiogram import types, Dispatcher


# @dp.callback_query_handler(text='Гвозди декоративные')
async def dec(call: types.CallbackQuery):
    await call.message.answer('hello')
    await call.answer('downloading')
    photo = open('photo/IMG_20221128_16_12_0000012.jpg', 'rb')
    await call.message.answer_photo(photo,caption="Hello", protect_content=True)

def register_handlers(dp:Dispatcher):
    dp.register_callback_query_handler(dec,text='Гвозди декоративные')