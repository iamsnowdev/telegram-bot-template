from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.enums import ButtonStyle

from bot.assets.texts import all_texts


def get_start(lang: str) -> InlineKeyboardMarkup:
    texts = all_texts.get(lang=lang).keyboards.start
    keyboard = [
        [
            InlineKeyboardButton(text=texts.btn1, callback_data="btn1"),
            InlineKeyboardButton(text=texts.btn2, callback_data="btn2")
        ]
    ]

    return InlineKeyboardMarkup(inline_keyboard=keyboard)