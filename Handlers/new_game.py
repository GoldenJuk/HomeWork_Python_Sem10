from loader import dp, bot
from aiogram.types import Message
from random import choice
from functions import log
import data
from functions import bot_takes_sweets, player_takes_sweets


@dp.message_handler(commands=['new_game'])
async def mes_new(message: Message):
    data.game = True
    player = message.from_user.id

    for match in data.meet:
        if player == match[0]:
            await message.answer('Ты уже начал игру, продолжай!')
            break
    else:
        # await dp.bot.send_message(5194485882, f'Игру начал, {message.from_user.full_name}!!!')
        my_game = [message.from_user.id, data.one_move, data.start_sweets, data.game]
        data.meet.append(my_game)
        await log(message)
        for match in data.meet:
            if player == match[0]:
                total = match[2]
                one_move = match[1]
                await bot.send_message(message.from_user.id, f'Началась новая игра.\nНа столе {total} конфет. '
                                                             f'За один ход можно взять не более {one_move}.\n\n  Выбираю очередность!\n'
                                                             f'----------------------------------------\n')
                first = message.from_user.full_name
                second = 'Bot'
                first_move = choice([first, second])
                await bot.send_message(message.from_user.id, f'Первым ходит {first_move}')
                if first_move == second:
                   if match[2] > match[1]:
                       await bot_takes_sweets(message)
                   else:
                        await player_takes_sweets(message)