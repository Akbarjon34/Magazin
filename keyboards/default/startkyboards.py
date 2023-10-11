from aiogram.types  import ReplyKeyboardMarkup, KeyboardButton

start_btn = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='🍯Купить голду'),
            KeyboardButton(text='🎢Голд пасс')
        ],
        [
            KeyboardButton(text='💬Канал'),
            KeyboardButton(text='🛠 Поддержка')
        ],
        [
              KeyboardButton(text='📉 Курс')
        ]
    ], resize_keyboard=True
)