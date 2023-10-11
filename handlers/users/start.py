from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.startkyboards import start_btn
from keyboards.inline.chanel import chanel_list
from keyboards.inline.support import support_list
from keyboards.inline.goldpass import goldpass_list
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    photo = "https://play-lh.googleusercontent.com/0mJuxwS-XI21njoPFuBk2MIkhQF0dFH2sKQcSPOxJJMB72Je9hNnyhGgHhDcouRoihI"
    await message.answer_photo(
        photo=photo, caption= "🔆 Для продолжения выбери нужную команду на клавиатуре❓ Если есть дополнительные вопросы по поводу бота, нажмите на кнопку «🛠 Поддержка»", reply_markup= start_btn)


@dp.message_handler(lambda message: message.text == '💬Канал')
async def courses(message: types.Message):
    await message.answer("Подпишитесь на наш канал!📊", reply_markup=chanel_list)


@dp.message_handler(lambda message: message.text == '📉 Курс')
async def courses(message: types.Message):
    await message.answer("""
📉От 1G до 2999G - 1G=120UZS 
                         
📉От 3000G до 5999G - 1G=117UZS
                         
📉От 6000G и выше - 1G=111UZS
"""
    )


@dp.message_handler(lambda message: message.text == '🛠 Поддержка')
async def courses(message: types.Message):
    await message.answer("Если у вас возникли какие-либо вопросы или проблемы, не стесняйтесь обращаться к нашему администратору!😊", reply_markup=support_list) 


@dp.message_handler(text='🎢Голд пасс')
async def bot_start(message: types.Message):
    photo = "https://image.winudf.com/v2/image1/Y29tLnB1bmtlc3RhLmNsaWNrZXJfc2NyZWVuX3J1LVJVXzFfMTY5NDI0OTEwNV8wMTQ/screen-1.webp?fakeurl=1&type=.webp"
    await message.answer_photo(
        photo=photo, caption= """🌟 Biz sizga GoldPass-ni foydali xarid qilish imkonini beradigan yangi yangilanishlar va o'yinlarni e'lon qilishdan faxrlanamiz! 🎮💰

<b> 🏆 Золотой пропуск 1: 130000 сум 💎
🏆 Золотой пропуск +20 уровней: 298000 сум 💰

Обновите свой опыт игры и получите удивительные привилегии:

🚀 Уровень 1: всего 14000 сум 🎉
🔥 Уровень 10: всего 114000 сум 🎁
🌟 Уровень 25: всего 227000 сум 🏅
🎖 Уровень 75: всего 590000 сум 🚀

Не упустите возможность улучшить свой опыт игры с Золотым пропуском! ✨🎁🎮 </b>.""", reply_markup= goldpass_list)
    

