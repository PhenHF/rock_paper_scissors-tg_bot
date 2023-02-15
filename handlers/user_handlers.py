from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import Message
from keyboards.keyboards import game_kb, yes_no_kb
from lexicon.lexicon_ru import LEXICON_RU
from services.services import get_bot_choice, get_winner


router: Router = Router()

#Handler for /start
@router.message(CommandStart())
async def procces_command_start(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=yes_no_kb)


#Handler for /help
@router.message(Command(commands=['help']))
async def procces_command_help(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=yes_no_kb)

#Handler if user consent play
@router.message(Text(text=LEXICON_RU['yes_button']))
async def procces_yes_answer(message: Message):
    await message.answer(text=LEXICON_RU['yes'], reply_markup=game_kb)


#Handler if user dissent play
@router.message(Text(text=LEXICON_RU['no_button']))
async def procces_no_answer(message: Message):
    await message.answer(text=LEXICON_RU['no'])

#Handler for gaming keyboard
@router.message(Text(text=[LEXICON_RU['rock'], LEXICON_RU['paper'], LEXICON_RU['scissors']]))
async def gaming_procces(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(text=f'{LEXICON_RU["bot_choice"]} '
                              f'- {LEXICON_RU[bot_choice]}')
    winner = get_winner(message.text, bot_choice)
    await message.answer(text=LEXICON_RU[winner], reply_markup=yes_no_kb)