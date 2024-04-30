from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import F
from aiogram.utils.keyboard import InlineKeyboardBuilder
import asyncio
import logging

logging.basicConfig(level=logging.INFO)
bot = Bot(token="6833268368:AAEUkfps_AMX_HuL4PW1eQV3UdeN6e5Sa4s")
dp = Dispatcher()

HELP_COMMAND = """
/help-помощь,
/start- начало работы с ботом,
/city-список городов"""

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(text="Привет! Давай знакомиться!\nЯ-бот помощник. Я расскажу тебе о достопримечательностях разных городов России. Введи команду /city и выбери нужный тебе город!")
    await message.delete()

@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.reply(text=HELP_COMMAND)

@dp.message(Command("city"))
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="/Казань"),
            types.KeyboardButton(text="/Санкт-Питербург"),
            types.KeyboardButton(text="/Уфа")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Выберите нужный вам город"
    )
    await message.answer("Выберите нужный вам город", reply_markup=keyboard)

@dp.message(Command("Казань"))
async def cmd_Kazan(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Кремлёвская набережная"),
            types.KeyboardButton(text="Дворец земледельцев"),
            types.KeyboardButton(text="Казанский кремль")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        input_field_placeholder="Выберите достопримечаельность Казани"
    )
    await message.answer("Выберите достопримечаельность", reply_markup=keyboard)

@dp.message(Command("Санкт-Питербург"))
async def cmd_StPetersburg(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Альпинистам блокадного Ленинграда"),
            types.KeyboardButton(text="Памятник Петру I"),
            types.KeyboardButton(text="Здание Главного штаба")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        input_field_placeholder="Выберите достопримечаельность Санкт-Питербурга"
    )
    await message.answer("Выберите достопримечаельность", reply_markup=keyboard)

    @dp.message(Command("Уфа"))
    async def cmd_Ufa(message: types.Message):
        kb = [
            [
                types.KeyboardButton(text="Памятник Ленину (сквер Ленина)"),
                types.KeyboardButton(text="Собор Рождества Богородицы"),
                types.KeyboardButton(text="Монумент Дружбы")
            ],
        ]
        keyboard = types.ReplyKeyboardMarkup(
            keyboard=kb,
            input_field_placeholder="Выберите достопримечаельность Уфы"
        )
        await message.answer("Выберите достопримечаельность", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())