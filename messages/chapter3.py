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

class Progress3(StatesGroup):
    msg_1 = State()
    msg_2 = State()
    msg_3 = State()
    msg_4 = State()
    msg_5 = State()
    msg_6 = State()
    msg_7 = State()
    msg_8 = State()
    msg_9 = State()
    msg_10 = State()
    msg_11 = State()
    msg_12 = State()
    msg_13 = State()
    msg_14 = State()
    msg_15 = State()
    msg_16 = State()
    msg_17 = State()
    msg_18 = State()
    msg_19 = State()

def register_handlers_chapter3(dp: Dispatcher):
    dp.register_message_handler(third_chapter_answer_1, commands="chapter3", state='*')
    dp.register_message_handler(third_chapter_answer_1, Text(equals="3. Стили руководства"))
    dp.register_message_handler(third_chapter_answer_2, Text(equals=["Хуже некуда", "Oтлично!", "Сойдет"]), state=Progress3.msg_1)
    dp.register_message_handler(to_third_chapter_block_1, Text(equals=["Готов!"]), state=Progress3.msg_2)
    dp.register_message_handler(third_chapter_answer_3, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress3.msg_3)
    dp.register_message_handler(third_chapter_answer_4, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress3.msg_4)
    dp.register_message_handler(third_chapter_answer_5, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress3.msg_5)
    dp.register_message_handler(third_chapter_answer_6, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress3.msg_6)
    dp.register_message_handler(third_chapter_answer_7, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress3.msg_7)
    dp.register_message_handler(third_chapter_answer_8, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress3.msg_8)
    dp.register_message_handler(third_chapter_answer_9, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress3.msg_9)
    dp.register_message_handler(third_chapter_answer_10, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress3.msg_10)
    dp.register_message_handler(third_chapter_answer_11, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress3.msg_11)
    dp.register_message_handler(third_chapter_answer_12, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress3.msg_12)
    dp.register_message_handler(third_chapter_answer_13, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress3.msg_13)
    dp.register_message_handler(third_chapter_answer_14, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress3.msg_14)
    dp.register_message_handler(third_chapter_answer_15, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress3.msg_15)
    dp.register_message_handler(third_chapter_answer_16, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress3.msg_16)
    dp.register_message_handler(third_chapter_answer_17, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress3.msg_17)
    dp.register_message_handler(third_chapter_answer_18, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress3.msg_18)
    dp.register_message_handler(third_chapter_answer_19, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress3.msg_19)


async def third_chapter_answer_1(message: types.Message):
    Log().getLogger().info("Chapter 3")
    await asyncio.sleep(2)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Oтлично!")
    keyboard.add("Сойдет")
    keyboard.add("Хуже некуда")

    await message.answer("Вот мы и снова вместе! " 
                         "Приветствую тебя в 3 разделе. Тут мы поговорим о стилях руководства (управления). Как настроение?", 
                         reply_markup=keyboard)
    await Progress3.msg_1.set()

async def third_chapter_answer_2(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    await asyncio.sleep(1)
    if (message.text == "Хуже некуда"):
        keyboard.add("Готов!")
        await message.answer("Договорились, я на связи и жду, когда ты вернешься.", reply_markup=keyboard)
        await Progress3.msg_2.set()
    elif (message.text == "Oтлично!"):
        await message.answer("Вот и хорошо, тогда приступим.", reply_markup=keyboard)
        await third_chapter_block_1(message)
    else :
        await message.answer("Надеюсь, что в процессе настроение улучшится.", reply_markup=keyboard)
        await third_chapter_block_1(message)

async def to_third_chapter_block_1(message: types.Message):
    await third_chapter_block_1(message)

async def third_chapter_block_1(message: types.Message):
    await message.answer("Ты уже знаешь, что есть 4 типа сотрудников по отношению к задаче и научился их диагностировать."
                         "С каждым таким сотрудником важно взаимодействовать по-разному."
                         , reply_markup=types.ReplyKeyboardRemove())
    await asyncio.sleep(3)
    await message.answer("Стили складываются из комплекса действий руководителя. "
                         "Каких именно? Инструктирующих и мотивирующих (или вовлекающих). ")
    await asyncio.sleep(3)
    await bot.send_photo(chat_id = message.chat.id,
                         photo = open('media/instructional-actions.png', 'rb'))
    await asyncio.sleep(2)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Однозначно!")
    keyboard.add("Хотелось бы пример.")
    await message.answer("Все ли тебе понятно?", reply_markup=keyboard)
    await Progress3.msg_3.set()

async def third_chapter_answer_3(message: types.Message):
    await asyncio.sleep(1)
    if (message.text == "Однозначно!"):   
        await message.answer("Замечательно, тогда продолжим!", reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer("К примеру, это инструктаж, четкая постановка целей и задач, планирование. ", 
                            reply_markup=types.ReplyKeyboardRemove())

    await third_chapter_block_2(message)

async def third_chapter_block_2(message: types.Message):
    await message.answer("В чем суть и смысл этих действий? Сделать так, чтобы сотрудник предельно ясно понимал, что и как ему "
                         "нужно сделать, у него не возникало никаких вопросов насчет предстоящей деятельности. "
                         "Для новых сотрудников это особенно важно. Но и для опытных в некоторых случаях будет далеко не лишним."
                         , reply_markup=types.ReplyKeyboardRemove())
    
    await asyncio.sleep(3)
    await bot.send_photo(chat_id = message.chat.id,
                         photo = open('media/motivating-actions.png', 'rb'))

    await asyncio.sleep(3)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Нет, все ясно!")
    keyboard.add("Кoнечно!")
    await message.answer("Привести пример?", reply_markup=keyboard)
    await Progress3.msg_4.set()

async def third_chapter_answer_4(message: types.Message):
    await asyncio.sleep(1)
    if(message.text == "Нет, все ясно!"):
        await message.answer("Хорошо! Их главная функция – повысить уверенность в себе и побудить работать “с огоньком”. ", 
                            reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer("Например, помощь, оценка вклада сотрудника, благодарность, акцент на его сильных сторонах, "
                         "выслушивание его сложностей и активная помощь и так далее.  ", 
                            reply_markup=types.ReplyKeyboardRemove())

    await third_chapter_block_3(message)


async def third_chapter_block_3(message: types.Message):
    counter.set_counter(0)
    await asyncio.sleep(1)
    await message.answer("Давай я задам тебе несколько вопросов, чтобы ты закрепил понимание, где инструктирующие, "
                         "а где мотивирующие действия. "
                         , reply_markup=types.ReplyKeyboardRemove())
    
    await asyncio.sleep(2)

    await message.answer("Итак, задание очень простое. Прочитай описание действия руководителя и определи, "
                         "это инструктирование или  мотивирование?")
    await asyncio.sleep(2)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Мотивирующее")
    keyboard.add("Инстрyктирующее")

    await message.answer("1. Руководитель похвалил сотрудника за качественно выполненную работу." 
                        "Это мотивирующее или инcтруктирующее действие? ", reply_markup=keyboard)
    await Progress3.msg_5.set()

async def third_chapter_answer_5(message: types.Message):
    await asyncio.sleep(1)
    if (message.text == "Мотивирующее"):
        counter.increase_counter()
        await message.answer("Верно!", reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer("Мимо:( Это про мотивирование", reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(2)
    await third_chapter_block_4(message)


async def third_chapter_block_4(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Мoтивирующее")
    keyboard.add("Инструктирующeе")
    await message.answer("2. Руководитель подробно рассказал, почему эта задача интересная и перспективная для сотрудника.",
                        reply_markup=keyboard)
    await Progress3.msg_6.set()

async def third_chapter_answer_6(message: types.Message):
    await asyncio.sleep(1)
    if(message.text == "Мoтивирующее"):
        counter.increase_counter()
        await message.answer("В точку!", reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer("Увы, нет, это мотивирование", reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(2)
    await third_chapter_block_5(message)

async def third_chapter_block_5(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Mотивирующее")
    keyboard.add("Инструктирующеe")
    await message.answer("3. Руководитель прислал подробное описание того, что нужно сделать. ",
                        reply_markup=keyboard)
    await Progress3.msg_7.set()

async def third_chapter_answer_7(message: types.Message):
    await asyncio.sleep(1)
    if(message.text == "Mотивирующее"):
        await message.answer("Увы, нет", reply_markup=types.ReplyKeyboardRemove())
    else:
        counter.increase_counter()
        await message.answer("Да, согласен!", reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(2)
    await third_chapter_block_6(message)

async def third_chapter_block_6(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Мотивирующeе")
    keyboard.add("Инструктирyющее")
    await message.answer("4. Руководитель поинтересовался мнением сотрудника, какую технологию лучше выбрать для выполнения этой задачи. ",
                        reply_markup=keyboard)
    await Progress3.msg_8.set()

async def third_chapter_answer_8(message: types.Message):
    await asyncio.sleep(1)
    if(message.text == "Мотивирующeе"):
        counter.increase_counter()
        await message.answer("Однозначно!", reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer("Нет, это мотивационное действие", reply_markup=types.ReplyKeyboardRemove())
    
    await asyncio.sleep(2)
    await third_chapter_block_7(message)


async def third_chapter_block_7(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Мотивирующеe")
    keyboard.add("Инструктирующee")
    await message.answer("5. Руководитель на личном примере показал, как выполнить задачу. ",
                        reply_markup=keyboard)
    await Progress3.msg_9.set()

async def third_chapter_answer_9(message: types.Message):
    await asyncio.sleep(1)
    if(message.text == "Мотивирующеe"):
        await message.answer("Увы, нет.", reply_markup=types.ReplyKeyboardRemove())
    else:
        counter.increase_counter()
        await message.answer("Точно!", reply_markup=types.ReplyKeyboardRemove())
    await asyncio.sleep(2)
    await third_chapter_block_8(message)


async def third_chapter_block_8(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Мотивирующee")
    keyboard.add("Инструктирующее")
    await message.answer("6. Руководитель обозначил критерии достижения результата ",
                        reply_markup=keyboard)
    await Progress3.msg_10.set()

async def third_chapter_answer_10(message: types.Message):
    await asyncio.sleep(1)
    if(message.text == "Мотивирующee"):
        await message.answer("Нет, это инструктирующее действие", reply_markup=types.ReplyKeyboardRemove())
    else:
        counter.increase_counter()
        await message.answer("Ты абсолютно прав!", reply_markup=types.ReplyKeyboardRemove())
    await asyncio.sleep(1)
    await third_chapter_block_9(message)

async def third_chapter_block_9(message: types.Message):
    correct_answers = counter.get_counter()
    if correct_answers in [0, 5, 6]:
        word = 'правильных ответов'
    elif correct_answers == 1:
        word = 'правильный ответ'
    else:
        word = 'правильных ответа'
    Log().getLogger().info("{0} {1} из 6".format(correct_answers, word))
    await asyncio.sleep(1)
    await message.answer("Отлично! Ты выполнил все 6 заданий и у тебя {0} {1} из 6. ".format(correct_answers, word)
                         , reply_markup=types.ReplyKeyboardRemove())
    
    await asyncio.sleep(2)

    await message.answer("Хочу подарить тебе шпаргалку с описанием мотивирующих и инструктирующих действий. " 
                         "Ты можешь сохранить картинки в галерею телефона и по необходимости обращаться к ним. ")
    await asyncio.sleep(2)

    await bot.send_photo(chat_id = message.chat.id,
                         photo = open('media/main-instructional-actions.png', 'rb'),
                         caption = 'Основные инструктирующие действия')

    await asyncio.sleep(6)
    await bot.send_photo(chat_id = message.chat.id,
                             photo = open('media/main-motivating-actions.png', 'rb'),
                             caption = 'Основные мотивирующие действия')

    await asyncio.sleep(6)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Конечно, легко")
    keyboard.add("Пока не очень")

    await message.answer("Теперь я уверен, что ты знаешь и умеешь различать мотивирующие и инструктирующие действия. "
                         "Да?", reply_markup=keyboard)
    await Progress3.msg_11.set()

async def third_chapter_answer_11(message: types.Message):
    await asyncio.sleep(1)
    if(message.text == "Конечно, легко"):
        await message.answer("Супер! Полетели дальше", reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer("Ты всегда можешь вернуться в начало раздела и перечитать теорию, чтобы лучше понять. Я дождусь. ",
                         reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(2)
    await third_chapter_block_10(message)


async def third_chapter_block_10(message: types.Message):
    await message.answer("А теперь давай соберем воедино схему разного сочетания инструктирующих и мотивирующих действий. "
                         "Во втором разделе мы с тобой изучали уровни профессионального развития (УПР), ты наверняка помнишь, что их 4. " 
                         "И определяются они соотношением уровня компетентность и мотивации сотрудника. "
                         , reply_markup=types.ReplyKeyboardRemove())
    
    await asyncio.sleep(4)

    await message.answer("Как я уже говорил выше, похожая история со стилями управления, которые складываются из инструктирующих "
                         "и мотивирующих действий. Сочетание инструктирующих и вовлекающих действий дают нам 4 стиля руководства: "
                         "инструктирующий, наставнический, вовлекающий, делегирующий. ")
    await asyncio.sleep(4)

    await bot.send_photo(chat_id = message.chat.id,
                         photo = open('media/management-styles-c1-c2.png', 'rb'))

    await asyncio.sleep(4)

    await bot.send_photo(chat_id = message.chat.id,
                         photo = open('media/management-styles-c3-c4.png', 'rb'))

    await asyncio.sleep(6)

    await bot.send_photo(chat_id = message.chat.id,
                         photo = open('media/management-styles-c1-c2-c3-c4.png', 'rb'))

    await asyncio.sleep(3)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Инстрyктирующий")
    keyboard.add("Нaставнический")
    keyboard.add("Вoвлекающий")
    keyboard.add("Дeлегирующий")
    keyboard.add("Всe понемногу")

    await message.answer("Что ж, теперь ты знаешь про 4 стиля управления. Как думаешь, а какой применять лучше всего? ", 
                        reply_markup=keyboard)
    await Progress3.msg_12.set()

async def third_chapter_answer_12(message: types.Message):
    await asyncio.sleep(1)
    if(message.text == "Всe понемногу"):
        await message.answer("Ты наиболее близок к истине! Важно быть гибким.", reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer("Не всегда и не со всеми сотрудниками", reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(2)
    await third_chapter_block_11(message)


async def third_chapter_block_11(message: types.Message):
    await asyncio.sleep(1)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("От настроения")
    keyboard.add("От характера руководителя")
    keyboard.add("От уровня профессионального развития сотрудника")

    await message.answer("Руководителю очень важно применять все эти стили. Как думаешь, от чего это зависит? "
                         , reply_markup=keyboard)
    await Progress3.msg_13.set()

async def third_chapter_answer_13(message: types.Message):
    await asyncio.sleep(1)
    if(message.text == "От настроения"):
        await message.answer("Бывает и такое, но нет. Применение стиля зависит от УПР сотрудника.", reply_markup=types.ReplyKeyboardRemove())
    elif (message.text == "От характера руководителя"):
        await message.answer("Да, безусловно, но это не решающий фактор. Применение стиля зависит от УПР сотрудника. ", reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer("В точку!", reply_markup=types.ReplyKeyboardRemove())
  
    await asyncio.sleep(2)
    await third_chapter_block_12(message)


async def third_chapter_block_12(message: types.Message):
    await asyncio.sleep(1)

    await message.answer("Выбор стиля должен зависеть от уровня профессионального развития сотрудника по отношению к задаче. "
                         "С одними сотрудниками достаточно просто описать задачу и быть спокойным, что она будет выполнена, "
                         "для других важны четкие инструкции, постоянный контроль.  "
                         , reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(3)

    await message.answer("Давай рассмотрим этот момент подробнее. ")

    await asyncio.sleep(1)

    await message.answer("К сотруднику Р1 нужно применять стиль С1. "
                         "Сотрудник, который является новичком в задаче, как правило, имеет высокую мотивацию, но недостаточную компетентность. "
                         "Поэтому для Р1 идеально подходит инструктирующий стиль (С1). В нём много инструкций и мало мотивирования. ")

    await asyncio.sleep(3)

    await message.answer("К сотруднику Р2 нужно применять стиль С2. "
                         "Р2 по-прежнему имеет низкую (или среднюю) компетентность, но, поняв, что с задачей все не так просто, как ему "
                         "казалось на начальном этапе, теряет мотивацию и уверенность в себе. Поэтому от руководителя требуется не только давать "
                         "ему четкие инструкции, но и поддерживать сотрудника, возвращая ему веру в себя. Управляя Р2, руководителю следует "
                         "использовать наставнический стиль (С2).")
    
    await asyncio.sleep(1)
    #отправить гифку - хз какую
    await asyncio.sleep(3)

    await message.answer("К сотруднику Р3 нужно применять стиль С3. "
                         "Организационный подросток, сотрудник типа Р3 имеет достаточно высокую компетентность и очень нестабильную мотивацию. "
                         "Поэтому самым адекватным для Р3 будет вовлекающий стиль руководства (С3). В нём много вовлекающих действий и мало инструкций.")

    await asyncio.sleep(1)
    #отправить гифку - хз какую
    await asyncio.sleep(3)

    await message.answer("К сотруднику Р4 нужно применять стиль С4. "
                         "Сотрудник-профи, у которого высокая компетентность, может работать почти самостоятельно, при этом мотивировать его не нужно,"
                         " у него высокая внутренняя вовлеченность. Такому сотруднику важно не мешать, предоставив ему свободу в действиях и принятии решений."
                         " Оптимальный стиль для управления Р4 - делегирующий (С4).")
    
    await asyncio.sleep(1)
    #отправить гифку - хз какую
    await asyncio.sleep(3)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Дa!")
    keyboard.add("Не совсем")

    await message.answer("Сложилась ли картинка, все ли тебе понятно? ", reply_markup=keyboard)
    await Progress3.msg_14.set()

async def third_chapter_answer_14(message: types.Message):
    await asyncio.sleep(1)
    if(message.text == "Дa!"):
        await message.answer("Отлично!", reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer("Задача руководителя - быть гибким и адекватно применять разные стили. "
                             "Это помогает тебе максимально раскрыть потенциал каждого сотрудника и помочь им максимально раскрыться. ",
                             reply_markup=types.ReplyKeyboardRemove())
  
    await asyncio.sleep(2)
    await third_chapter_block_13(message)


async def third_chapter_block_13(message: types.Message):
    await asyncio.sleep(1)

    await message.answer("Итак, руководитель должен быть гибким в применении стилей управления и умело использовать "
                         "каждый в зависимости от того, какой сотрудник перед ним."
                         , reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(2)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Кoнечно")
    keyboard.add("Не сейчас")

    await message.answer("Давай закрепим понимание стилей на видеопримерах. "
                         "Твоя задача будет посмотреть фрагмент  и определить, какой стиль управления применяет руководитель. "
                         "Ты готов?  ", reply_markup=keyboard)
    await Progress3.msg_15.set()

async def third_chapter_answer_15(message: types.Message):
    await asyncio.sleep(1)
    if(message.text == "Кoнечно"):
        await message.answer("Тогда поехали!", reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer("Хорошо, можешь идти дальше, а потом пересмотреть видео. ",
                             reply_markup=types.ReplyKeyboardRemove())
  
    await asyncio.sleep(2)
    await third_chapter_block_14(message)

async def third_chapter_block_14(message: types.Message):
    await asyncio.sleep(1)

    #отправка видео
    await bot.send_message(chat_id = message.chat.id, text="<a href='https://ok.ru/video/200996426023'>Итак, первое видео. </a>",parse_mode= types.ParseMode.HTML)
    
    

    await asyncio.sleep(2)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Инструктирyющий")
    keyboard.add("Настaвнический")
    keyboard.add("Вовлeкающий")
    keyboard.add("Делегирyющий")

    await message.answer("Какой это стиль? ", reply_markup=keyboard)
    await Progress3.msg_16.set()

async def third_chapter_answer_16(message: types.Message):
    await asyncio.sleep(1)
    if (message.text == "Инструктирyющий"):
        await message.answer("Верно! Тут много инструкций и мало мотивирования.", reply_markup=types.ReplyKeyboardRemove())
    elif (message.text == "Настaвнический"):
        await message.answer("Инструкций довольно много, в этом смысле согласен. Но мотивировать в данном случае не особенно нужно. "
                             "Тут более адекватен инструктирующий стиль. ", reply_markup=types.ReplyKeyboardRemove())
    elif (message.text == "Вовлeкающий"):
        await message.answer("Неверно! Это инструктирующий стиль. ", reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer("Неверно! Это инструктирующий стиль.  ", reply_markup=types.ReplyKeyboardRemove())
  
    await asyncio.sleep(2)
    await third_chapter_block_15(message)

async def third_chapter_block_15(message: types.Message):
    await asyncio.sleep(1)

    #отправка видео
    # Видео 2
    # Отряд самоубийц
    # https://ok.ru/video/833415549197

    await bot.send_message(chat_id = message.chat.id, text="<a href='https://ok.ru/video/833415549197'>Видео 2 </a>",parse_mode= types.ParseMode.HTML)
    
    await asyncio.sleep(2)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Инcтруктирующий")
    keyboard.add("Наcтавнический")
    keyboard.add("Вoвлeкающий")
    keyboard.add("Дeлeгирующий")

    await message.answer("Какой это стиль? ", reply_markup=keyboard)
    await Progress3.msg_17.set()

async def third_chapter_answer_17(message: types.Message):
    await asyncio.sleep(1)

    if (message.text == "Инcтруктирующий"):
        await message.answer("Нет) Инструкций тут явно немного в стиле пойди туда, не знаю куда, а мотивирования много, только негативного, со знаком минус.", 
        reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer("Хорошо, можешь идти дальше, а потом пересмотреть видео. ", reply_markup=types.ReplyKeyboardRemove())
  
    await asyncio.sleep(2)
    await third_chapter_block_16(message)

async def third_chapter_block_16(message: types.Message):
    await asyncio.sleep(1)

    #отправка видео
    # Видео 3
    # Отрывок из метода Хитча

    await asyncio.sleep(2)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Инструктирующий")
    keyboard.add("Наставнический")
    keyboard.add("Вовлекающий")
    keyboard.add("Делегирующий")

    await message.answer("Какой это стиль? ", reply_markup=keyboard)
    await Progress3.msg_18.set()

async def third_chapter_answer_18(message: types.Message):
    await asyncio.sleep(1)

    if (message.text == "Инструктирующий"):
        await message.answer("Да, тут есть инструкции, но и мотивация, поддержка. Это наставнический стиль.",reply_markup=types.ReplyKeyboardRemove())
    elif (message.text == "Наставнический"):
        await message.answer("Да, тут очень много инструкций и есть мотивация, поддержка.", reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer("Это наставнический стиль.", reply_markup=types.ReplyKeyboardRemove())
  
    await asyncio.sleep(2)
    await third_chapter_block_17(message)

async def third_chapter_block_17(message: types.Message):
    await asyncio.sleep(1)

    await message.answer("Спасибо, что потренировался! Конечно, примеры из кино не отображают всю реальность, "
                         "поэтому тебе самому нужно будет пробовать и применять эти стили. ", reply_markup=types.ReplyKeyboardRemove())
    
    await asyncio.sleep(2)

    await message.answer("Давай сделаем выводы. Основная задача руководителя – как можно быстрее провести сотрудника от Р1 к Р4. "
                         "Это позволяет ему перейти от наиболее затратных по времени и силам Инструктирующего (С1) и Наставнического (С2) "
                         "стилей к более экономным - Вовлекающему (С3) и Делегирующему (С4).")

    await asyncio.sleep(3)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Все отлично!")
    keyboard.add("Я запутался.")

    await message.answer("Какой это стиль? ", reply_markup=keyboard)
    await Progress3.msg_19.set()

async def third_chapter_answer_19(message: types.Message, state: FSMContext):
    await asyncio.sleep(1)
    await state.finish()
    await message.answer("Спасибо за обратную связь! Если осталось желание потренироваться и закрепить изученное, то "
                         "ты всегда можешь вернуться и перечитать теорию, потренироваться на кейсах. ", reply_markup=types.ReplyKeyboardRemove())
    # from messages.chapter4 import fourth_chapter_welcome
    # await fourth_chapter_welcome(message)