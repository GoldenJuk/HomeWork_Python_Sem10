from loader import dp, bot
from aiogram.types import Message
from functions import bot_takes_sweets
import data

@dp.message_handler()
async def take_sweets(message: Message):
    if (message.text.startswith('/set') or message.text.startswith('/move')) and (len(message.text.split())) == 1:
        await bot.send_message(message.from_user.id, f'Введи команду и число конфет через пробел')

    for match in data.meet:
        if match[3]:
            if message.from_user.id == match[0]:
                if message.text.isdigit():
                    if 0 < int(message.text) <= match[1]:
                        match[2] -= int(message.text)
                        await bot.send_message(message.from_user.id, f'Осталось конфет - {match[2]}')
                        await bot_takes_sweets(message)
                    else:
                        await message.answer(f'{message.from_user.first_name}, неправильно ты взял!!! Можно брать от 1 до {match[1]}')
                else:
                    await bot.send_message(message.from_user.id, f'Всего {match[2]} конфет. Введи число!\n'
                                                                 f'Если хочешь установить новое количество конфет, набери, например: /set 500')
                    