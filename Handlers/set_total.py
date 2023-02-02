from loader import dp
from aiogram.types import Message
from functions import log
import data


@dp.message_handler(commands=['set'])
async def mes_set(message: Message):
    await log(message)
    for match in data.meet:
        if message.from_user.id == match[0]:
            if len (message.text.split()) > 1:
                if int(message.text.split()[1]) > match[1]:
                    count = message.text.split()[1]
                    match[2] = int(count)
                    await message.answer(f'Установили новое количество конфет = {match[2]}')
                else:
                    await message.answer(f'Попробуй еще раз. Количество должно быть больше {data.one_move}\n\n'
                                         f'Или поменяете количество конфет,\n'
                                         f' которое можно брать за один раз.\n'
                                         f'(например, /move 10)')
            else:
                await message.answer('Не указано количество конфет. Введите /set "количество конфет". Например: /set 500')