#!/usr/bin/python3
# -*- coding: utf-8 -*-

from datetime import datetime
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
import asyncio
from utils import DB, Log, MyBot

bot, dp = MyBot().get_bot()

class Intro(StatesGroup):
    name = State()
    intro_msg_1 = State()
    intro_msg_2 = State()

def register_handlers_intro(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start")
    dp.register_message_handler(process_name, state=Intro.name)
    dp.register_message_handler(answer1, Text(equals="Не удивил"), state=Intro.intro_msg_1)
    dp.register_message_handler(answer2, Text(equals="Да супер"), state=Intro.intro_msg_1)
    dp.register_message_handler(answer3, Text(equals="Готов на все 100!"), state=Intro.intro_msg_2)
    dp.register_message_handler(answer4, Text(equals="Давай попробуем"), state=Intro.intro_msg_2)

async def cmd_start(message: types.Message):
    Log().getLogger().info("Intro")
    await Intro.name.set()
    await message.answer("Здравствуйте! Как вас зовут?", reply_markup=types.ReplyKeyboardRemove())

async def process_name(message: types.Message):
    logger = Log().getLogger()
    logger.info("Name is %s", message.text)
    postgres_insert_query = """INSERT INTO clients (NAME, REG_DATE) VALUES (%s,%s) ON CONFLICT DO NOTHING"""
    record_to_insert = (message.text, datetime.now())
    connect, cur = DB().get_connect_cursor()
    cur.execute(postgres_insert_query, record_to_insert)
    connect.commit()

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Да супер")
    keyboard.add("Не удивил")
    await message.answer('Привет, {0}! Мне приятно, что ты подключился, теперь мне не так одиноко :-)'.format(message.text))
    await asyncio.sleep(1)
    await message.answer('Меня зовут ИнноБот, я умный и весёлый, а ещё я много знаю про управление и очень хочу поделиться с тобой!'
                         'Знаешь в чём моя суперсила? В том, что я с тобой на связи 24/7 и ты можешь поболтать со мной в любое время дня и ночи,'
                         'когда будет свободная минутка! Правда здорово?',
                         reply_markup=keyboard)
    
    await Intro.intro_msg_1.set()


async def answer1(message: types.Message):
    await message.answer("А ты серьезный человек, уверен, что мы найдём общий язык:-)",
                         reply_markup=types.ReplyKeyboardRemove())
    await block_1(message)

async def answer2(message: types.Message):
    await message.answer("Я рад что ты оценил:-)", reply_markup=types.ReplyKeyboardRemove())
    await block_1(message)

async def block_1(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Готов на все 100!")
    keyboard.add("Давай попробуем")
    await asyncio.sleep(1)
    await message.answer('Планирую рассказать тебе о том что такое ситуационное управление сотрудниками. Как ты на '
                         'это смотришь, готов начать?',
                         reply_markup=keyboard)
    await Intro.intro_msg_2.set()

async def answer3(message: types.Message, state: FSMContext):
    await message.answer("Отлично, с таким настроем мы с тобой быстро во всем разберемся:-)",
                         reply_markup=types.ReplyKeyboardRemove())
    await state.finish()
    await block_2(message)

async def answer4(message: types.Message, state: FSMContext):
    await message.answer("Сделаю все возможное, чтобы тебе понравилось и было полезно! Поехали!",
                         reply_markup=types.ReplyKeyboardRemove())
    await state.finish()
    await block_2(message)

async def block_2(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("1. Управление. Причины невыполнения задач"),
    keyboard.add("2. Уровни проф развития сотрудников"),
    keyboard.add("3. Стили руководства"),
    keyboard.add("4. Особенности управления разными типами сотрудников"),
    keyboard.add("5. Общее тестирование")
    await asyncio.sleep(1)
    await message.answer('Я рекомендую тебе открывать темы последовательно в этом порядке:',
                         reply_markup=keyboard)
    