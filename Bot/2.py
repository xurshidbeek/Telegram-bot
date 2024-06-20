# app.py module
# -*- coding: utf-8 -*-
import logging
from aiogram import Bot, Dispatcher, types
from db import Database
from button import menu_keyboard, menu_detail, mahsulot_button
from inline_button import keyboard
from aiogram.types import InputFile
from aiogram.utils import executor
from gtts import gTTS
import os

@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)


