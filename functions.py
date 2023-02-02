from aiogram.types import Message
from random import randint
import data


async def log(message: Message):
    with open ('log.csv', 'a') as file:
        file.write(f'{message.date}, {message.from_user.first_name}, {message.from_user.id}, {message.text}\n')


async def bot_takes_sweets(message: Message):
    for match in data.meet:
        if message.from_user.id == match[0]:
           match[3] = True
           if match[2] > match[1]:
               sweets = match[2] % (match[1] + 1)
               if sweets == 0: sweets = randint(1, match[1])
               match[2] -= sweets
               await message.answer(f'Я взял {sweets} конфет. На столе осталось: {match[2]} конфет.')
               await player_takes_sweets(message)
           else:
               await message.answer(f'Осталось {match[2]} конфет, я их забираю. Я выйграл!!!')
               data.meet.remove(match)
               match[3] = False


async def player_takes_sweets(message: Message):
    for match in data.meet:
        if message.from_user.id == match[0]:
            match[3] = True
            if match[2] > match[1]:
                await message.answer(f'{message.from_user.first_name}, ходи! Сколько берешь конфет?')
            else:
                await message.answer(f'Выйграл, {message.from_user.first_name}!!!')
                data.meet.remove(match)
                match[3] = False
