#!/usr/bin/python3
# -*- coding: utf-8 -*-

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text, ContentTypeFilter
import asyncio

from utils import Log, MyBot, Counter

bot, dp = MyBot().get_bot()
counter = Counter()

class Progress4(StatesGroup):
    msg_1 = State()
    msg_2 = State()
    msg_3 = State()
    msg_4 = State()

def register_handlers_chapter4(dp: Dispatcher):
    dp.register_message_handler(fourth_chapter_welcome, commands="chapter4", state='*')
    dp.register_message_handler(fourth_chapter_welcome, Text(equals="4. Особенности управления разными типами сотрудников"))
    dp.register_message_handler(fourth_chapter_answer_1, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress4.msg_1)
    dp.register_message_handler(fourth_chapter_answer_2, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress4.msg_2)
    dp.register_message_handler(fourth_chapter_answer_3, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress4.msg_3)
    dp.register_message_handler(fourth_chapter_answer_4, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress4.msg_4)

async def fourth_chapter_welcome(message: types.Message, state: FSMContext):
    await state.finish()
    Log().getLogger().info("Chapter 4")
    await asyncio.sleep(2)
    
    await message.answer("Привет! Мы с тобой оказались в последнем (по счету, а не по значению!) разделе, поздравляю, "
                         "что ты стремительно двигаешься к завершению курса и прокачиваешь себя. ")


    await asyncio.sleep(2)

    await message.answer("Давай поговорим о том, как управлять разными типами сотрудников, то есть обсудим, какая есть "
                         "специфика в постановке целей и задач, мотивации и контроле сотрудников с разным УПР.")

    await asyncio.sleep(2)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Да, не терпится!")
    keyboard.add("Куда ж я денусь...")

    await message.answer("Готов начать?", 
                         reply_markup=keyboard)

    await Progress4.msg_1.set()

    async def fourth_chapter_answer_1(message: types.Message):
        await asyncio.sleep(1)
        if(message.text == "Да, не терпится!"):
            await message.answer("Уже начинаем", reply_markup=types.ReplyKeyboardRemove())
        else:
            await message.answer("Похоже ты сегодня не в духе. Лови виртуальную поддержку (какой-то добрый"
                                 "смайл добавить). А я постараюсь всё объяснить максимально просто. ", 
                                 reply_markup=types.ReplyKeyboardRemove())

        await fourth_chapter_block_1(message)

    async def fourth_chapter_block_1(message: types.Message):
        await asyncio.sleep(1)
        await message.answer("Начнем с постановки целей разным типам сотрудников. "
                             "Самое главное правило: ставя цели, учитывай УПР (уровень профессионального развития) сотрудников. А теперь ближе к делу.  "
                             "а где мотивирующие действия. ", reply_markup=types.ReplyKeyboardRemove())

        await asyncio.sleep(2)


        await message.answer("Если перед тобой Р1 (сотрудник с высокой мотивацией и низкой компетентностью по отношению к задаче),"
                             "давай максимально подробные, четкие и ясные инструкции. Новичок в задаче обычно мотивирован на ее выполнение сам по себе, а ясное"
                             "понимание, что делать, поможет ему не наломать дров и станет дополнительным стимулом. ", reply_markup=types.ReplyKeyboardRemove())

        await asyncio.sleep(2)

        await message.answer("КАРТИНКА "
"Постановка целей для Р1 "
"1. Расскажи сотруднику, что нужно сделать: результат и какие сроки."
"2. Опиши, как это сделать и перечисли первые шаги."
"3. Покажи и дай попробовать."
"4. Исправь ошибки.  ", reply_markup=types.ReplyKeyboardRemove())

        await asyncio.sleep(2)

        await message.answer("Для Р2 стоит уменьшить детализацию инструкций, но довольно подробно обсудить, что нужно делать. "
                             "Обязательно мотивировать:  всели уверенность («Ты справишься»), пообещай поддержку в сложных ситуациях («Будут сложности, обращайся!»).",
                             reply_markup=types.ReplyKeyboardRemove())

        await asyncio.sleep(2)

        await message.answer("КАРТИНКА "
"Постановка целей для Р2"
"1. Расскажи сотруднику, что нужно сделать: результат и сроки."
"2. Спроси, как собирается делать?"
"3. Утони, почем так?"
"4. Покажи логику выполнения задачи."
"5. Договоритесь о ближайшей точке контроля", reply_markup=types.ReplyKeyboardRemove())

        await asyncio.sleep(2)


        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard.add("Да, предельно")
        keyboard.add("В целом, вникаю")

        await message.answer("Тебе все понятно?", reply_markup=keyboard)

        await Progress4.msg_2.set()


    async def fourth_chapter_answer_2(message: types.Message):
        asyncio.sleep(1)

        if(message.text == "Да, предельно"):
            await message.answer("Так держать! *Смайл большой палец вверх", reply_markup=types.ReplyKeyboardRemove())
        else:
            await message.answer("Хорошо, идем дальше!", reply_markup=types.ReplyKeyboardRemove())

        await fourth_chapter_block_2(message)

    async def fourth_chapter_block_2(message: types.Message):
        await asyncio.sleep(2)

        await message.answer("У Р3 – сотрудника  с переменной мотивацией и высокой компетентностью -  стоит спросить, как бы он выполнил эту задачу, "
                             "выслушать и скорректировать  план действий. Важно, чтобы сотрудник с твоей помощью сам нашел мотивацию на выполнение задачи, "
                             "увидел свой интерес: зачем мне выполнять эту задачу?", reply_markup=types.ReplyKeyboardRemove())

        await asyncio.sleep(2)
        
        await message.answer("КАРТИНКА "
"Постановка целей для Р3"
"1. Расскажи сотруднику, что нужно сделать: результат и сроки."
"2. Поработай с мотивацией сотрудника: почему именно он, почему важно."
"3. Спроси, справится ли сотрудник? Какие есть вопросы?"
"4. Поставь точки контроля.", reply_markup=types.ReplyKeyboardRemove())

        await asyncio.sleep(2)

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard.add("Не надо ни мотивации, ни инструкций")
        keyboard.add("Сам расскажи")

        await message.answer("Про Р4 попробуешь сам?", reply_markup=keyboard)

        await Progress4.msg_3.set()


    async def fourth_chapter_answer_3(message: types.Message):
        await asyncio.sleep(1)

        await message.answer("Р4 с энтузиазмом примется за сложную, интересную задачу, если ему предоставить свободу действий. "
                             "Ему не нужны подробные инструкции и стимулы. Однако согласуй с ним выполнение задачи."
                             , reply_markup=types.ReplyKeyboardRemove())
        
        await asyncio.sleep(2)


        await message.answer("КАРТИНКА "
"Постановка целей для Р4"
"1. Расскажи сотруднику, что нужно сделать: результат и сроки."
"2. Спроси, есть ли вопросы?"
"3. Договоритесь о точке контроля.", reply_markup=types.ReplyKeyboardRemove())

        await asyncio.sleep(2)

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard.add("Конечно!")
        keyboard.add("Нет, расскажи")

        await message.answer("Для полноты картины давай обсудим с тобой, как применять систему постановки целей по SMART для разных типов сотрудников. "
                             "Помнишь ли ты, что такое система SMART? ", reply_markup=keyboard)

        await Progress4.msg_4.set()

    async def fourth_chapter_answer_4(message: types.Message):
        await asyncio.sleep(1)

        if(message.text == "Конечно!"):
            await message.answer("Замечательно", reply_markup=types.ReplyKeyboardRemove())
        else:
            await message.answer("Конечно!", reply_markup=types.ReplyKeyboardRemove())
    
        await  fourth_chapter_block_3(message)

    async def fourth_chapter_block_3(messages: types.Message):
        await asyncio.sleep(1)

        await message.answer("SMART – это метод описания цели, включающий в себя: конкретность, измеримость, достижимость, важность и определённость по срокам. "
                             , reply_markup=types.ReplyKeyboardRemove())

