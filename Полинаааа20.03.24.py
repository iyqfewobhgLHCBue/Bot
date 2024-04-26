import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command, CommandObject
from aiogram import F
import sqlite3
from aiogram.types import FSInputFile

con = sqlite3.connect('telegramm_bot_Polina_dostoprimechatelnosti.db')
cursor = con.cursor()
cursor.execute('SELECT * FROM dostoprimechatelnosti')
data = cursor.fetchall()
print(data)

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="6833268368:AAEUkfps_AMX_HuL4PW1eQV3UdeN6e5Sa4s")
# Диспетчер
dp = Dispatcher()

def keyboard_for_kazan():
    kb = []
    for i in data:
        if i[4] == 0:
            kb.append([types.KeyboardButton(text=i[1])])
    print(kb)
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True,
                                         )
    return keyboard
def keyboard_for_StPetersburg():
    kb = []
    for i in data:
        if i[4] == 1:
            kb.append([types.KeyboardButton(text=i[1])])
    print(kb)
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True,
                                         )
    return keyboard
@dp.message(Command("help"))
async def cmd_start(message: types.Message):
    await message.answer("city-список городов \n find-выберите город")


@dp.message(Command("city"))
async def cmd_city(message: types.Message):
    kb = [
        [types.KeyboardButton(text='Казань')],
        [types.KeyboardButton(text='Санкт-Петербург')]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True,
                                         )
    await message.answer("Нажмите на кнопку с городом", reply_markup=keyboard)


@dp.message(F.text)
async def cmd_start(message: types.Message):
    logging.info(message.text)
    if message.text == "Казань":
        await message.answer('Вот', reply_markup=keyboard_for_kazan())
        return
    elif message.text == "Санкт-Петербург":
        await message.answer("Вот-вот", reply_markup=keyboard_for_StPetersburg())
        return

@dp.message(F.text.lower() == "кто тебя создал?")
async def cmd_start(message: types.Message):
    await message.answer("меня создал cucumber228")


@dp.message(F.text.lower() == "на каком языке ты написан?")
async def cmd_start(message: types.Message):
    await message.answer("любопытной варваре на базаре нос оторвали")


@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text='Привет')],
        [types.KeyboardButton(text='/help')]
    ]
    Keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True,
                                         )
    await message.answer('привет', reply_markup=Keyboard)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())