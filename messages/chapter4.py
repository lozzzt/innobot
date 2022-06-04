#!/usr/bin/python3
# -*- coding: utf-8 -*-

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
import asyncio

from utils import Log, MyBot, Counter

bot, dp = MyBot().get_bot()
counter = Counter()

class Progress4(StatesGroup):
    msg_1 = State()
    msg_2 = State()
    msg_3 = State()

def register_handlers_chapter4(dp: Dispatcher):
    dp.register_message_handler(fourth_chapter_welcome, commands="chapter4", state='*')
    dp.register_message_handler(fourth_chapter_welcome, Text(equals="4. Стили руководства"))

async def fourth_chapter_welcome(message: types.Message, state: FSMContext):
    await state.finish()
    Log().getLogger().info("Chapter 4")
    await asyncio.sleep(2)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Oтлично!")
    keyboard.add("Хорошо")
    await message.answer("Приветствую тебя в 4 разделе", 
                         reply_markup=keyboard)