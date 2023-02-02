import data
from loader import dp
from aiogram.types import Message
from functions import log

@dp.message_handler(commands=['help'])
async def mes_help(message: Message):
    data.game = False
    await log(message)
    await message.answer(f'Мои команды:\n\n /start\n /new_game - Новая игра\n /set               - Всего конфет\n '
                         f'/move          - Забираем конфет за один ход\n /help            - Помощь')