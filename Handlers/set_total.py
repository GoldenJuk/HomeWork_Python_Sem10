from loader import dp
from aiogram.types import Message
from functions import log
import data


@dp.message_handler(commands=['set'])
async def mes_set(message: Message):
    await log(message)
    if data.game == False:
        if (len(message.text.split())) >= 2:
            if int(message.text.split()[1]) > data.one_move:
                count = message.text.split()[1]
                data.start_sweets = int(count)
                await message.answer(f'Установили новое количество конфет = {data.start_sweets}')

            else:
                await message.answer(f'Попробуй еще раз. Количество должно быть больше {data.one_move}\n\n'
                                 f'Или поменяете количество конфет,\n'
                                 f' которое можно брать за один раз.\n'
                                 f'(например, /move 10)')
        else:
            await message.answer('Не указано количество конфет. Введите /set "количество конфет". Например: /set 500')
    else:
        await message.answer('Игра уже началась.\nИзменить можно после окончания игры.')