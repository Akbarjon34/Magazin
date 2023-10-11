from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types

from loader import dp



class GoldAmountState(StatesGroup):
    amount = State()  # Создайте состояние amount внутри GoldAmountState

@dp.message_handler(lambda message: message.text == '🍯Купить голду')
async def buy_gold_start(message: types.Message):
    await message.answer("⬇️Введите количество голды:")
    await GoldAmountState.amount.set()

@dp.message_handler(state=GoldAmountState.amount)
async def buy_gold_amount(message: Message, state: FSMContext):
    try:
        amount = int(message.text)
        gold_price_per_unit = 120  # Цена за 1 голду
        total_price = amount * gold_price_per_unit

        # Рассчитайте цену для выставления скина с учетом 20% наценки
        skin_price = round(total_price * 1.20, 2)  # Округляем до двух знаков после запятой

        await message.answer(f"{amount} GOLD🍯 - {total_price} cум.")
        await message.answer(f"❗️Чтобы купить голду - выставьте на продажу TEC-9 'Tie Dye' за {skin_price} UZS, и отправьте скриншот сюда -> @jamshid_5878 с комкой")

        await state.finish()  # Завершить состояние
    except ValueError:
        await message.answer("Пожалуйста, введите корректное количество голды (целое число).")