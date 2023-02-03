import data
from loader import dp
from aiogram.types import Message
from functions import log

@dp.message_handler(commands=['help'])
async def mes_help(message: Message):
    data.game = False
    await log(message)
    await message.answer(f'Мои команды:\n\n/start\n{"/new_game":15} - Новая игра\n{"/set":24} - Всего конфет\n{" ":30}(например: /set 200)\n'
                         f'{"/move":21} - Забираем конфет за один ход\n{" ":30}(например: /move 10)\n{"/help":22} - Помощь')