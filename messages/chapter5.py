#!/usr/bin/python3
# -*- coding: utf-8 -*-

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text, ContentTypeFilter
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import asyncio

from utils import Log, MyBot, Counter

bot, dp = MyBot().get_bot()
counter = Counter()
stickers = {"YES": ['CAACAgEAAxkBAAEFVb5i2VzAu3cVxx-EMLFxhgT785gSEAACzgADGNZ3CVzeX3MKZ7VaKQQ',
                    'CAACAgIAAxkBAAEFVcJi2V0O-fx8T5_jpS9t1BhtHI3w6QACBgADr8ZRGp7O7vhbqf36KQQ',
                    'CAACAgIAAxkBAAEFVdVi2V5DYYV7takoenHIekJaTyyvRAACLgEAAvcCyA89lj6kwiWnGikE',
                    'CAACAgIAAxkBAAEFVddi2V5T5E9VyexYQYFEqCrNDpfGHQACpAADUomRI68ST7EFwyc9KQQ',
                    'CAACAgIAAxkBAAEFVdli2V5fF8Px6D0K2IQJrMn7rLgaOAACcQAD9wLID3kKxPT9t4jLKQQ',
                    'CAACAgIAAxkBAAEFVd1i2V6BsUYkMWuia-FhuEDWFp6n0wACRAADQbVWDFpIqKL_emcUKQQ',
                    'CAACAgIAAxkBAAEFVeFi2V6WwyEhfeL9B-G6AAHaI_9fL3sAAiwAA0QNzxfI-9ztWpcNiykE',
                    'CAACAgIAAxkBAAEFVeVi2V7h6hsOsXBCTecfVjBanKbLXAAC_AEAAhZCawqBUPSpvGAKBykE',
                    'CAACAgQAAxkBAAEFVeli2V8DM7HA2rgvMfPnH8TPJQe5twACEwEAAt5A-AerHWT_QaApYykE',
                    'CAACAgIAAxkBAAEFVe1i2V8fBWTcZNubYg50Y-bHpdxtFwACgAADwZxgDDUiPX15tvOeKQQ',
                    'CAACAgIAAxkBAAEFVfFi2V8vtnHKixZd6k4xg8BtAux2qAACNg8AAh4J8UlSVZzp6JZteykE'],
            "NO":  ['CAACAgEAAxkBAAEFVcBi2VzFfvwHs7TYmDD0kCCiIQo2IwAC1AADGNZ3Ccpjz7M3NJuwKQQ',
                    'CAACAgIAAxkBAAEFVcRi2V0STUonIGG8nMEQbvyljT8QVgACAQADr8ZRGhLj3-N0EyK_KQQ',
                    'CAACAgIAAxkBAAEFVc9i2V2EAAH6Qa4wvp0XSQc2rvVLI-cAAg8MAALijjlKLRc3zE1Ct1ApBA',
                    'CAACAgIAAxkBAAEFVdFi2V2ZqKrGAAHcI_3ioe540_ge0hcAArUAA1KJkSNnCZ8AAQUB_kQpBA',
                    'CAACAgIAAxkBAAEFVdNi2V2rT3lGrbNomyNUs0fALZqKSwACfQAD9wLIDy7JuwrdyyJJKQQ',
                    'CAACAgIAAxkBAAEFVdti2V579F7Ym7viGn7I3GKTlBHqPwACRQADQbVWDB2S9JLvuNn8KQQ',
                    'CAACAgIAAxkBAAEFVd9i2V6Lb92fF-kCEYUIUdY-SBTFPQACMAADRA3PFw5rYdlOV0IAASkE',
                    'CAACAgIAAxkBAAEFVeNi2V6tIKrECilAHfaFDSE0fNu1SgACOQ8AAnayKUr6_EzRpTCdWikE',
                    'CAACAgQAAxkBAAEFVedi2V7sB-xO6Im3E0FRf__ecy67CgACKwIAAt5A-AdKsjfXGM7QMikE',
                    'CAACAgIAAxkBAAEFVeti2V8X6s_6mN6nEv6bBO1kHQadNAACcwADwZxgDAsjEJD-pZcnKQQ',
                    'CAACAgIAAxkBAAEFVe9i2V8nNU7ehSE6CwJkyBTQx1ypuAACuQ4AAmxu8Emp2F_Xn3emBikE']
            }

class Progress5(StatesGroup):

    msg_01 = State()
    msg_02 = State()
    msg_03 = State()
    msg_04 = State()
    msg_05 = State()
    msg_06 = State()
    msg_07 = State()
    msg_08 = State()
    msg_09 = State()
    msg_10 = State()

def register_handlers_chapter5(dp: Dispatcher):
    dp.register_message_handler(fifth_chapter_welcome, commands="chapter5", state='*')
    dp.register_message_handler(fifth_chapter_welcome, Text(equals="5. Общее тестирование"), state='*')
    dp.register_message_handler(fifth_chapter_answer_01, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress5.msg_01)
    dp.register_message_handler(fifth_chapter_answer_02, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress5.msg_02)
    dp.register_message_handler(fifth_chapter_answer_03, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress5.msg_03)
    dp.register_message_handler(fifth_chapter_answer_04, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress5.msg_04)
    dp.register_message_handler(fifth_chapter_answer_05, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress5.msg_05)
    dp.register_message_handler(fifth_chapter_answer_06, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress5.msg_06)
    dp.register_message_handler(fifth_chapter_answer_07, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress5.msg_07)
    dp.register_message_handler(fifth_chapter_answer_08, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress5.msg_08)
    dp.register_message_handler(fifth_chapter_answer_09, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress5.msg_09)
    dp.register_message_handler(fifth_chapter_answer_10, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress5.msg_10)    
    
async def fifth_chapter_welcome(message: types.Message, state: FSMContext):
    """ Welcome """

    await state.finish()
    Log().getLogger().info("Chapter 5")
    counter.set_counter(0)
    await asyncio.sleep(1)
    await message.answer("""Рад видеть тебя в финальном разделе!
Молодец, что решил пройти все до конца!
Итак, ответь на несколько вопросов!""", reply_markup=types.ReplyKeyboardRemove())
    await fifth_chapter_question_01(message)

# 1
async def fifth_chapter_question_01(message: types.Message):
    
    await asyncio.sleep(1)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Знания и опыт в конкретной задаче")
    keyboard.add("Красный диплом и энциклопедические знания")
    keyboard.add("Богатый внутренний мир и готовность учиться")
    await message.answer("""*1.Компетентность в работе – это…*""", parse_mode=types.ParseMode.MARKDOWN, reply_markup=keyboard)
    await Progress5.msg_01.set()

async def fifth_chapter_answer_01(message: types.Message):
    
    await asyncio.sleep(1)

    if(message.text == "Знания и опыт в конкретной задаче"):
        counter.increase_counter()
        await bot.send_sticker(chat_id = message.chat.id, sticker = stickers["YES"][1], reply_markup=types.ReplyKeyboardRemove())
    else:
        await bot.send_sticker(chat_id = message.chat.id, sticker = stickers["NO"][1], reply_markup=types.ReplyKeyboardRemove())
    
    await fifth_chapter_question_02(message)

# 2
async def fifth_chapter_question_02(message: types.Message):
    
    await asyncio.sleep(1)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Р2")
    keyboard.add("Р3")
    keyboard.add("Р4")
    await message.answer("""*2.К какому типу отнести сотрудника?*

У Лены огромный опыт и богатые знания, но она вечно всем не довольна, 
просит премии и требует особого внимания.""", parse_mode=types.ParseMode.MARKDOWN, reply_markup=keyboard)
    await Progress5.msg_02.set()

async def fifth_chapter_answer_02(message: types.Message):
    
    await asyncio.sleep(1)

    if(message.text == "Р3"):
        counter.increase_counter()
        await bot.send_sticker(chat_id = message.chat.id, sticker = stickers["YES"][2], reply_markup=types.ReplyKeyboardRemove())
    else:
        await bot.send_sticker(chat_id = message.chat.id, sticker = stickers["NO"][2], reply_markup=types.ReplyKeyboardRemove())
    
    await fifth_chapter_question_03(message)

# 3
async def fifth_chapter_question_03(message: types.Message):
    
    await asyncio.sleep(1)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Образование + вера в себя")
    keyboard.add("Мотивация  + опыт работы")
    keyboard.add("Компетентность + мотивация")
    await message.answer("""*3. УПР – это…*""", parse_mode=types.ParseMode.MARKDOWN, reply_markup=keyboard)
    await Progress5.msg_03.set()

async def fifth_chapter_answer_03(message: types.Message):
    
    await asyncio.sleep(1)

    if(message.text == "Компетентность + мотивация"):
        counter.increase_counter()
        await bot.send_sticker(chat_id = message.chat.id, sticker = stickers["YES"][3], reply_markup=types.ReplyKeyboardRemove())
    else:
        await bot.send_sticker(chat_id = message.chat.id, sticker = stickers["NO"][3], reply_markup=types.ReplyKeyboardRemove())
    
    await fifth_chapter_question_04(message)

# 4
async def fifth_chapter_question_04(message: types.Message):
    
    await asyncio.sleep(1)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Хочу, но не умею")
    keyboard.add("Могу и хочу!")
    keyboard.add("Не могу и не хочу")
    await message.answer("""*4. Сотрудника с УПР Р2 можно охарактеризовать так:*""", parse_mode=types.ParseMode.MARKDOWN, reply_markup=keyboard)
    await Progress5.msg_04.set()

async def fifth_chapter_answer_04(message: types.Message):
    
    await asyncio.sleep(1)

    if(message.text == "Не могу и не хочу"):
        counter.increase_counter()
        await bot.send_sticker(chat_id = message.chat.id, sticker = stickers["YES"][4], reply_markup=types.ReplyKeyboardRemove())
    else:
        await bot.send_sticker(chat_id = message.chat.id, sticker = stickers["NO"][4], reply_markup=types.ReplyKeyboardRemove())
    
    await fifth_chapter_question_05(message)

# 5
async def fifth_chapter_question_05(message: types.Message):
    
    await asyncio.sleep(1)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Р4")
    keyboard.add("Р1")
    keyboard.add("Р3")
    await message.answer("""*5. Определите уровень профессионального развития сотрудника.*

Опытный сотрудник Сергей получил новое задание, оно значительно отличается от того, что он делал раньше. 
Он очень старается, но у него пока не очень получается. 
Несмотря на неудачу, он не падает духом, ищет информацию, советуется, двигается вперед.""", parse_mode=types.ParseMode.MARKDOWN, reply_markup=keyboard)
    await Progress5.msg_05.set()

async def fifth_chapter_answer_05(message: types.Message):
    
    await asyncio.sleep(1)

    if(message.text == "Р1"):
        counter.increase_counter()
        await bot.send_sticker(chat_id = message.chat.id, sticker = stickers["YES"][5], reply_markup=types.ReplyKeyboardRemove())
    else:
        await bot.send_sticker(chat_id = message.chat.id, sticker = stickers["NO"][5], reply_markup=types.ReplyKeyboardRemove())
    
    await fifth_chapter_question_06(message)

# 6
async def fifth_chapter_question_06(message: types.Message):
    
    await asyncio.sleep(1)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("четкие инструкции с большим количеством деталей")
    keyboard.add("дам свободу действий")
    keyboard.add("спрошу о планах, внесу корректировки")
    await message.answer("""*6. Егор работает в компании давно, хороший специалист.*
Вчера он был назначен руководителем абсолютно нового для компании проекта. 
Насколько подробные ты бы давал инструкции этому человеку?""", parse_mode=types.ParseMode.MARKDOWN, reply_markup=keyboard)
    await Progress5.msg_06.set()

async def fifth_chapter_answer_06(message: types.Message):
    
    await asyncio.sleep(1)

    if(message.text == "четкие инструкции с большим количеством деталей"):
        counter.increase_counter()
        await bot.send_sticker(chat_id = message.chat.id, sticker = stickers["YES"][6], reply_markup=types.ReplyKeyboardRemove())
    else:
        await bot.send_sticker(chat_id = message.chat.id, sticker = stickers["NO"][6], reply_markup=types.ReplyKeyboardRemove())
    
    await fifth_chapter_question_07(message)

# 7
async def fifth_chapter_question_07(message: types.Message):
    
    await asyncio.sleep(1)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Р1")
    keyboard.add("Р4")
    keyboard.add("Р3")
    await message.answer("""*7. Для какого типа сотрудника (Р1, Р2, Р3, Р4) наилучшим вариантом будут такие мотиваторы:* 
поощрение инициативы, 
сложные и интересные задачи, 
свобода, 
делегирование ответственности, 
совместные обсуждения?""", parse_mode=types.ParseMode.MARKDOWN, reply_markup=keyboard)
    await Progress5.msg_07.set()

async def fifth_chapter_answer_07(message: types.Message):
    
    await asyncio.sleep(1)

    if(message.text == "Р4"):
        counter.increase_counter()
        await bot.send_sticker(chat_id = message.chat.id, sticker = stickers["YES"][7], reply_markup=types.ReplyKeyboardRemove())
    else:
        await bot.send_sticker(chat_id = message.chat.id, sticker = stickers["NO"][7], reply_markup=types.ReplyKeyboardRemove())
    
    await fifth_chapter_question_08(message)

# 8
async def fifth_chapter_question_08(message: types.Message):
    
    await asyncio.sleep(1)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Инструктирующий (С1)")
    keyboard.add("Вовлекающий (С3)")
    keyboard.add("Делегирующий (С4)")
    await message.answer("""<b>8. Посмотри ролик, определи, какой стиль управления использует руководитель</b>
<a href='https://www.youtube.com/watch?v=wpviTF7XGyc'>https://www.youtube.com/watch?v=wpviTF7XGyc</a>""", parse_mode=types.ParseMode.HTML, reply_markup=keyboard)
    await Progress5.msg_08.set()

async def fifth_chapter_answer_08(message: types.Message):
    
    await asyncio.sleep(1)

    if(message.text == "Инструктирующий (С1)"):
        counter.increase_counter()
        await bot.send_sticker(chat_id = message.chat.id, sticker = stickers["YES"][8], reply_markup=types.ReplyKeyboardRemove())
    else:
        await bot.send_sticker(chat_id = message.chat.id, sticker = stickers["NO"][8], reply_markup=types.ReplyKeyboardRemove())
    
    await fifth_chapter_question_09(message)

# 9
async def fifth_chapter_question_09(message: types.Message):
    
    await asyncio.sleep(1)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Р1")
    keyboard.add("Р2")
    keyboard.add("Р4")
    await message.answer("""*9. Для какого типа сотрудника подойдёт такой контроль:* 
промежуточный контроль по критериям и обсуждение конечных результатов работы""", parse_mode=types.ParseMode.MARKDOWN, reply_markup=keyboard)
    await Progress5.msg_09.set()

async def fifth_chapter_answer_09(message: types.Message):
    
    await asyncio.sleep(1)

    if(message.text == "Р4"):
        counter.increase_counter()
        await bot.send_sticker(chat_id = message.chat.id, sticker = stickers["YES"][9], reply_markup=types.ReplyKeyboardRemove())
    else:
        await bot.send_sticker(chat_id = message.chat.id, sticker = stickers["NO"][9], reply_markup=types.ReplyKeyboardRemove())
    
    await fifth_chapter_question_10(message)

# 10
async def fifth_chapter_question_10(message: types.Message):
    
    await asyncio.sleep(1)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("не знает, как")
    keyboard.add("не знает, что")
    keyboard.add("не хочет")
    keyboard.add("не может")
    await message.answer("""*10. Прочитай кейс. Выбери из списка причину, по которой сотрудник не выполнил задачу.* 

Ева давно работает в компании. Уже полгода она выполняет задачи без энтузиазма. 
Недавно она обсуждала с руководством прибавку к зарплате, а когда ее не получила, то стала выполнять задачи ещё хуже.""", parse_mode=types.ParseMode.MARKDOWN, reply_markup=keyboard)
    await Progress5.msg_10.set()

async def fifth_chapter_answer_10(message: types.Message, state: FSMContext):
    
    await asyncio.sleep(1)

    if(message.text == "не хочет"):
        counter.increase_counter()
        await bot.send_sticker(chat_id = message.chat.id, sticker = stickers["YES"][10], reply_markup=types.ReplyKeyboardRemove())
    else:
        await bot.send_sticker(chat_id = message.chat.id, sticker = stickers["NO"][10], reply_markup=types.ReplyKeyboardRemove())
    
    await fifth_chapter_final(message, state)

# Final
async def fifth_chapter_final(message: types.Message, state: FSMContext):
    
    await state.finish()
    await asyncio.sleep(1)

    correct_answers = counter.get_counter()
    if correct_answers in [2, 3, 4]:
        word = 'правильных ответа'
    elif correct_answers == 1:
        word = 'правильный ответ'
    else:
        word = 'правильных ответов'

    await message.answer("Вот теперь точно все! Поздравляю с полным завершением курса!\n"
                         "И у тебя {0} {1} из 10.".format(correct_answers, word), reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(1)
    await bot.send_sticker(chat_id = message.chat.id, 
                           sticker = 'CAACAgIAAxkBAAEFVg5i2W-tPxDmVkRzujgezKbeL30wfgACAgADr8ZRGrfoDI5wEsHhKQQ', 
                           reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(1)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.row(
                KeyboardButton('1️⃣'), KeyboardButton('2️⃣'), KeyboardButton('3️⃣')).row(
                KeyboardButton('4️⃣'), KeyboardButton('5️⃣'), KeyboardButton('6️⃣')).row(
                KeyboardButton('7️⃣'), KeyboardButton('8️⃣'), KeyboardButton('9️⃣')).row(
                KeyboardButton('🔟'))
    await message.answer('Оцени, пожалуйста, насколько ты готов порекомендовать этот курс своим коллегам?', reply_markup=keyboard)
