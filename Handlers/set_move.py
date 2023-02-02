from loader import dp
from aiogram.types import Message
from functions import log
import data


@dp.message_handler(commands=['move'])
async def mes_set_move(message: Message):
    await log(message)
    if data.game == False:
       if len (message.text.split()) >= 2:
           if int(message.text.split()[1]) >= 1:
               count = message.text.split()[1]
               data.one_move = int(count)
               await message.answer(f'Установили новое количество конфет,\nкоторое можно брать за один раз = {data.one_move}')

           else:
               await message.answer(f'Попробуй еще раз. Количество должно быть больше или равно 1 штук.')
       else:
            await message.answer('Не указано количество конфет. Введите /move "количество конфет". Например: /move 10 ')

    else:
        await message.answer('Игра уже началась.\nИзменить можно после окончания игры.')