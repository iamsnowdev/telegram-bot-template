from aiogram import Router
from aiogram.types import Message, CallbackQuery


router = Router(name=__name__)


@router.message()
async def any_message(message: Message):
    ...


@router.callback_query()
async def any_callback(callback: CallbackQuery):
    ...