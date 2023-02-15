from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU

#Create the key for answer yes or no
button_yes: KeyboardButton = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no: KeyboardButton = KeyboardButton(text=LEXICON_RU['no_button'])

#Init buidler
yes_no_kb_buidler: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

#Add the key to the builder with param "width=2"
yes_no_kb_buidler.row(button_yes, button_no, width=2)

#Create the keyboard with answer yes or no
yes_no_kb = yes_no_kb_buidler.as_markup(one_time_keyboard=True, resize_keyboard=True)


#Creating game keyboard buttons
button_rock: KeyboardButton = KeyboardButton(text=LEXICON_RU['rock'])
button_scissors: KeyboardButton = KeyboardButton(text=LEXICON_RU['scissors'])
button_paper: KeyboardButton = KeyboardButton(text=LEXICON_RU['paper'])

#Creating the gaming keyboard
game_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[
                                                            [button_rock],
                                                            [button_scissors],
                                                            [button_paper],
                                                            ],resize_keyboard=True)
