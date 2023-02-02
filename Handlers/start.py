from aiogram.types import Message
from loader import dp
from functions import log
import data


@dp.message_handler(commands=['start'])
async def mes_start(message: Message):
    data.game = False
    await log(message)
    await message.answer(f'Привет, {message.from_user.first_name}!!!\n\n'
                         f'Мои команды:\n\n /start\n /new_game\n /set\n /move\n /help')
    await dp.bot.send_message(5194485882, f'К чату присоединился, {message.from_user.full_name}!!!')
