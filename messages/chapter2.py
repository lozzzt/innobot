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

class Progress2(StatesGroup):
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
    msg_20 = State()
    msg_21 = State()
    msg_22 = State()
    msg_23 = State()
    msg_24 = State()

def register_handlers_chapter2(dp: Dispatcher):
    dp.register_message_handler(to_chapter2, commands="chapter2", state='*')
    dp.register_message_handler(to_chapter2, Text(equals="2. Уровни проф развития сотрудников"))
    dp.register_message_handler(answer1, Text(equals="Нет конечно!"), state=Progress2.msg_1)
    dp.register_message_handler(answer2, Text(equals="Да, если он старательный"), state=Progress2.msg_1)
    dp.register_message_handler(answer3, Text(equals="Конечно!"), state=Progress2.msg_2)
    dp.register_message_handler(answer4, Text(equals="Нет, я идеален!"), state=Progress2.msg_2)
    dp.register_message_handler(answer5, Text(equals=["Какие группы?", "Понятно"]), state=Progress2.msg_3)
    dp.register_message_handler(answer6, Text(equals="Полезная картинка"), state=Progress2.msg_4)
    dp.register_message_handler(answer7, Text(equals="Ок, принято!"), state=Progress2.msg_4)
    dp.register_message_handler(answer8, Text(equals=["Знакомо", "Понятно, дальше!"]), state=Progress2.msg_5)
    dp.register_message_handler(answer9, Text(equals=["Да, много таких", "Меня такие люди не радуют"]), state=Progress2.msg_6)
    dp.register_message_handler(answer10, Text(equals="Не то слово!"), state=Progress2.msg_7)
    dp.register_message_handler(answer11, Text(equals="Побольше бы таких!"), state=Progress2.msg_7)
    dp.register_message_handler(answer12, Text(equals="Да!"), state=Progress2.msg_8)
    dp.register_message_handler(answer13, Text(equals="Приведи пример"), state=Progress2.msg_8)
    dp.register_message_handler(answer14, Text(equals=["Р2", "Р3"]), state=Progress2.msg_9)
    dp.register_message_handler(answer15, Text(equals="➡️ Да"), state=Progress2.msg_10)
    dp.register_message_handler(answer16, Text(equals="➡️ Позже пройду"), state=Progress2.msg_10)
    dp.register_message_handler(answer17, Text(equals="➡️ Продолжить"), state=Progress2.msg_11)
    dp.register_message_handler(answer18, Text(equals=["➡️ Р1", "➡️ Р2", "➡️ Р3"]), state=Progress2.msg_12)
    dp.register_message_handler(answer19, Text(equals="➡️ Р4"), state=Progress2.msg_12)
    dp.register_message_handler(answer20, Text(equals=["2️⃣ Р2", "3️⃣ Р3", "4️⃣ Р4"]), state=Progress2.msg_13)
    dp.register_message_handler(answer21, Text(equals="1️⃣ Р1"), state=Progress2.msg_13)
    dp.register_message_handler(answer22, Text(equals=["▶️ Р1", "▶️ Р2", "▶️ Р4"]), state=Progress2.msg_14)
    dp.register_message_handler(answer23, Text(equals="▶️ Р3"), state=Progress2.msg_14)
    dp.register_message_handler(answer24, Text(equals=["⏺ Р1", "⏺ Р3", "⏺️ Р4"]), state=Progress2.msg_15)
    dp.register_message_handler(answer25, Text(equals="⏺ Р2"), state=Progress2.msg_15)
    dp.register_message_handler(answer26, Text(equals=["⏹ Р1", "⏹ Р3", "⏹ Р4"]), state=Progress2.msg_16)
    dp.register_message_handler(answer27, Text(equals="⏹️ Р2"), state=Progress2.msg_16)
    dp.register_message_handler(answer28, Text(equals="➡️ Да!"), state=Progress2.msg_17)
    dp.register_message_handler(answer29, Text(equals="➡️ Не хочется, в другой раз"), state=Progress2.msg_17)
    dp.register_message_handler(answer29_2, Text(equals="Готов продолжить!"), state=Progress2.msg_18)
    dp.register_message_handler(answer30, Text(equals=["🅿️1️⃣", "🅿️3️⃣", "🅿️4️⃣"]), state=Progress2.msg_19)
    dp.register_message_handler(answer31, Text(equals="🅿️2️⃣"), state=Progress2.msg_19)
    dp.register_message_handler(answer32, Text(equals=["🅿2", "🅿3", "🅿4"]), state=Progress2.msg_20)
    dp.register_message_handler(answer33, Text(equals="🅿1"), state=Progress2.msg_20)
    dp.register_message_handler(answer34, Text(equals=["🅿2️⃣", "🅿3️⃣", "🅿4️⃣"]), state=Progress2.msg_21)
    dp.register_message_handler(answer35, Text(equals="🅿1️⃣"), state=Progress2.msg_21)
    dp.register_message_handler(answer36, Text(equals=["1", "2", "3", "4", "5"]), state=Progress2.msg_22)
    dp.register_message_handler(answer37, Text(equals="Да, продолжу!"), state=Progress2.msg_23)
    dp.register_message_handler(answer38, Text(equals="Чуть позже"), state=Progress2.msg_23)
    dp.register_message_handler(answer39, Text(equals="Готов!"), state=Progress2.msg_24)


async def to_chapter2(message: types.Message):
    await block_8(message)

async def block_8(message: types.Message):
    Log().getLogger().info("Chapter 2")
    await message.answer('И снова привет! В этом разделе тебя ждет информация об уровнях профессионального развития и '
                         'о том, чем отличаются сотрудники с разным уровнем. Также мы поговорим о том, '
                         'как диагностировать этот самый уровень. Начнем!', reply_markup=types.ReplyKeyboardRemove())
    await asyncio.sleep(4)
    await bot.send_photo(chat_id = message.chat.id,
                                 photo = open('media/upr.png', 'rb'),
                                 caption = 'Уровень профессионального развития (УПР) – умение и желание сотрудника выполнить '
                                                                     'поставленную перед ним задачу.')
    await asyncio.sleep(3)
    await message.answer('УПР зависит от сочетания 2-х факторов: компетентности и мотивации.')
    await asyncio.sleep(2)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Нет конечно!")
    keyboard.add("Да, если он старательный")
    await message.answer('Компетентность – знания и навыки,  которые нужны для выполнения конкретной задачи. Как '
                         'думаешь, сотрудник будет одинаково компетентен в решении всех задач?', reply_markup=keyboard)
    await Progress2.msg_1.set()

async def answer1(message: types.Message):
    await message.answer("Согласен с тобой!👍", reply_markup=types.ReplyKeyboardRemove())
    await block_9(message)

async def answer2(message: types.Message):
    await message.answer("Я подумаю об этом. Но похоже это что-то из области фантастики!",
                         reply_markup=types.ReplyKeyboardRemove())
    await block_9(message)

async def block_9(message: types.Message):
    await asyncio.sleep(2)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Конечно!")
    keyboard.add("Нет, я идеален!")
    await message.answer('Уровень компетентности всегда привязан к КОНКРЕТНОЙ задаче. То есть сотрудник может быть '
                         'профессионалом  в одной задаче и полным дилетантом в другой. Если ты сейчас обратишься к '
                         'своему опыту, то наверняка найдешь и те задачи,  в которых ты суперпрофи, и те, '
                         'в которых тебе есть, куда расти. Есть такое?', reply_markup=keyboard)
    await Progress2.msg_2.set()

async def answer3(message: types.Message):
    await bot.send_animation(chat_id = message.chat.id, 
                            reply_markup = types.ReplyKeyboardRemove(), 
                             animation = open('media/like.gif', 'rb'))
    await block_10(message)

async def answer4(message: types.Message):
    await bot.send_sticker(chat_id = message.chat.id, sticker = 'CAACAgIAAxkBAAIENmKYVBgMvSB0g1S7kAHbfTPC-4nAAAJNFgACcnfASKosAjUQ9JsZJAQ')
    await message.answer("Мне нравится твоя самооценка! Круто! И всё же даже когда все задачи ты выполняешь на "
                         "высоком уровне, есть те, которые даются сложнее.", reply_markup=types.ReplyKeyboardRemove())
    await block_10(message)

async def block_10(message: types.Message):
    await asyncio.sleep(3)
    await message.answer("С компетентностью разобрались. Перейдем ко второму фактору.")
    await asyncio.sleep(2)
    await message.answer("Мотивация – то, что побуждает человека к действиям, желание выполнить работу хорошо, "
                         "уверенности в своих возможностях и силах.")
    await asyncio.sleep(3)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Какие группы?")
    keyboard.add("Понятно")
    await message.answer('Сочетание компетентности и мотивации в разных пропорциях и составляют 4 уровня '
                         'профессионального развития. По каждой типовой задаче и по двум этим параметрам (уровень '
                         'мотивации и компетентности) всех сотрудников можно разбить на 4 неравные группы.',
                         reply_markup=keyboard)
    await Progress2.msg_3.set()

async def answer5(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Полезная картинка")
    keyboard.add("Ок, принято!")
    await message.answer(
        'В зависимости от уровня развития (Р – развитие) по отношению к конкретной задаче выделяют следующие типы сотрудников:\n'
        'Р1 (новичок) – высокая мотивация, низкая компетентность;\n'
        'Р2 (разуверившийся ученик) – низкая мотивация, низкая (или умеренная) компетентность;\n'
        'Р3 (специалист) – переменная мотивация, высокая компетентность;\n'
        'Р4 (профессионал) – высокая мотивация, высокая компетентность.')
    await asyncio.sleep(1)
    await bot.send_photo(chat_id = message.chat.id,
                         photo = open('media/4-pro-types-p1-p4.png', 'rb'),
                         caption = '4 типа сотрудников', 
                         reply_markup=keyboard)
    await Progress2.msg_4.set()

async def answer6(message: types.Message):
    await message.answer("Спасибо, что оценил мои старания!", reply_markup=types.ReplyKeyboardRemove())
    await asyncio.sleep(1)
    await block_11(message)

async def answer7(message: types.Message):
    await block_11(message)

async def block_11(message: types.Message):
    await message.answer("Если ты немного понаблюдаешь  за своими подчинёнными в различных ситуациях, то диагностика "
                         "начнет происходить почти автоматически. Давай поговорим, как определить тип сотрудника?",
                         reply_markup=types.ReplyKeyboardRemove())
    await asyncio.sleep(4)
    await message.answer("«Р1» - энтузиасты-новички: умений и опыта крайне мало или совсем нет, а вот желания "
                         "работать им не занимать! Они всегда в первых рядах: готовы браться за все, но результат "
                         "часто вызывает уныние. Он очень хочет и готов выполнять задачи, но пока не всё умеет.")
    await asyncio.sleep(5)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Знакомо")
    keyboard.add("Понятно, дальше!")
    await message.answer("Если ты спросишь у сотрудников, кто готов выполнить конкретную задачу, то он (Р1) скорее "
                         "всего откликнется в первых рядах (и не очень важно, есть ли у него опыт и умения), скажет, "
                         "что ему надо очень мало времени, он быстро справится! А если ты уточнишь, как он будет "
                         "выполнять задачу, то ответит что-то типа “по ходу разберусь”.",
                         reply_markup=keyboard)
    await Progress2.msg_5.set()

async def answer8(message: types.Message):
    await bot.send_sticker(chat_id = message.chat.id, sticker = 'CAACAgIAAxkBAAID2GKNG_WfiWu4YQ_9eZ5reBZ60yyKAALPGQACJQHASHk80OtmxE9JJAQ')
    await asyncio.sleep(1)
    await message.answer("«Р2» – это «разуверившиеся ученики», которые при первых сложностях потеряли веру в себя, "
                         "хоть и приобрели по пути немного навыков, опыта, знаний. Они вызывают или тоску (если ты "
                         "человек по жизни спокойный), или раздражение (если ты эмоциональный). Они крайне мало умеют "
                         "и не верят в себя.", reply_markup=types.ReplyKeyboardRemove())
    await asyncio.sleep(5)
    await message.answer("Р2, как правило, отказываются от задач из-за неуверенности в своих силах. А если и берутся, "
                         "то просят непомерно много времени. И чаще всего не могут описать технологию выполнения "
                         "задачи.")
    await asyncio.sleep(3)
    #отправка стикера дурачка в пижаме
    await bot.send_sticker(chat_id = message.chat.id, sticker = 'CAACAgIAAxkBAAID1WKNGsU5BpyX5qj4LUZh4AM86ob_AAKAGAACj2rISNRGejv7n_wfJAQ')
    await asyncio.sleep(1)
    await message.answer("«Р3» полны неожиданностей: то хотят, то не хотят, то готовы взяться за задачу, то начинают "
                         "капризничать. У них масса претензий по разным поводам, поэтому их поведение часто "
                         "раздражает начальника. Мотивация у них сильно хромает. Человек может, но не всегда хочет.")
    await asyncio.sleep(5)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Да, много таких")
    keyboard.add("Меня такие люди не радуют")
    await message.answer("Если его попросить “взять” задачу, он нередко начинает торговаться в стиле “А что мне за "
                         "это будет?”, немного растягивать сроки (не так сильно, как Р2), но при этом сможет хорошо и "
                         "в деталях описать технологию выполнения задачи. Деталей будет много. А знаешь почему? "
                         "Потому что надо создать видимость, как много человеку нужно сделать.", reply_markup=keyboard)
    await Progress2.msg_6.set()

async def answer9(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Не то слово!")
    keyboard.add("Побольше бы таких!")
    await message.answer("Профессионалы «Р4»  способны длительное время самостоятельно выполнять сложные задания. Как "
                         "правило, руководитель ощущает рядом с Р4 спокойную уверенность. Человек умеет и хочет. "
                         "Здорово, правда?", reply_markup=keyboard)
    await Progress2.msg_7.set()

async def answer10(message: types.Message):
    await message.answer("Вот и я так считаю", reply_markup=types.ReplyKeyboardRemove())
    await block_12(message)

async def answer11(message: types.Message):
    await message.answer("Да-а-а, мечта! Желаю тебе таких сотрудников!", reply_markup=types.ReplyKeyboardRemove())
    await block_12(message)

async def block_12(message: types.Message):
    await asyncio.sleep(2)
    await message.answer("Как его определить? На выполнение задачи берет оптимальные сроки, технологию выполнения, "
                         "если спросишь, описывает крупноблочно, при этом ты сразу поймешь, что он знает, "
                         "о чем говорит.")
    await asyncio.sleep(4)
    await bot.send_photo(chat_id = message.chat.id,
                                 photo = open('media/diagnostics-p1-p4.png', 'rb'),
                                 caption = 'Диагностика разных типов сотрудников')
    await asyncio.sleep(6)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Да!")
    keyboard.add("Приведи пример")
    await message.answer("Все ли теперь по полочкам, все ли понятно?", reply_markup=keyboard)
    await Progress2.msg_8.set()

async def answer12(message: types.Message):
    await message.answer("Я рад!", reply_markup=types.ReplyKeyboardRemove())
    await block_13(message)

async def answer13(message: types.Message):
    await message.answer("С удовольствием!", reply_markup=types.ReplyKeyboardRemove())
    await block_13(message)

async def block_13(message: types.Message):
    await asyncio.sleep(1)
    await message.answer("Андрей очень хочет стать тимлидом, но при этом еще никогда не управлял людьми, проектами, "
                         "не читал ни одной книги по управлению. К какому типу его отнести? Это Р1, так как у него "
                         "много мотивации, но мало (нет) опыта.")
    await asyncio.sleep(5)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Р2")
    keyboard.add("Р3")
    await message.answer("Сергей по настоянию руководителя прошел пару тренингов, прочитал книгу “Мама, я тимлид”, "
                         "она ему не особенно зашла. Он как не хотел никем и ничем управлять, так и не хочет. Как "
                         "думаешь, какой тип?", reply_markup=keyboard)
    await Progress2.msg_9.set()

async def answer14(message: types.Message):
    await message.answer("Сергей - типичный Р2: нет мотивации + мало умений.", reply_markup=types.ReplyKeyboardRemove())
    await asyncio.sleep(2)
    await message.answer("Оля, опытный разработчик: стала постоянно избегать привычных задач, часто говорит, "
                         "что ей мало денег и что-то нет желания работать. Тут мы видим невысокую мотивацию, "
                         "при этом есть опыт. Это Р3.")
    await asyncio.sleep(3)
    await message.answer("После окончания проекта Леонид с большим удовольствием взялся за новый с более большой "
                         "командой. Опыт и способности есть, мотивация высокая. Это Р4.")
    await asyncio.sleep(3)
    await message.answer("Я рассказал тебе все, что знал, о типах сотрудников! Теперь ты подкован и во всеоружии.")
    await asyncio.sleep(2)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("➡️ Да")
    keyboard.add("➡️ Позже пройду")
    await message.answer("Но знать не равно уметь!  Давай потренируемся определять типы сотрудников. У меня есть "
                         "короткий и нескучный тренажер на диагностику УПР,  надеюсь, что тебе понравится :) . "
                         "Готов?", reply_markup=keyboard)
    await Progress2.msg_10.set()

async def answer15(message: types.Message):
    await message.answer("Отлично!", reply_markup=types.ReplyKeyboardRemove())
    await block_14(message)

async def answer16(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("➡️ Продолжить")
    await message.answer("Ок, как будешь готов, возвращайся, я на связи!", reply_markup=keyboard)
    await Progress2.msg_11.set()

async def answer17(message: types.Message):
    await block_14(message)

async def block_14(message: types.Message):
    counter.set_counter(0)
    await bot.send_photo(chat_id = message.chat.id,
                         photo = open('media/inno-sherlock.png', 'rb'),
                         caption = 'ЗАДАНИЕ 1.')
    await asyncio.sleep(1)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("➡️ Р1")
    keyboard.add("➡️ Р2")
    keyboard.add("➡️ Р3")
    keyboard.add("➡️ Р4")
    await message.answer("Шерлок Холмс по отношению к дедуктивному методу решения задач. Какой тип?",
                         reply_markup=keyboard)
    await Progress2.msg_12.set()

async def answer18(message: types.Message):
    await message.answer("Увы, нет. Холмс по отношению к этой задаче типичный Р4: умеет, может и хочет",
                         reply_markup=types.ReplyKeyboardRemove())
    await block_15(message)

async def answer19(message: types.Message):
    counter.increase_counter()
    await message.answer("Верно! Он и прекрасно умеет, и хочет решать задачи с помощью этого метода.",
                         reply_markup=types.ReplyKeyboardRemove())
    await block_15(message)

async def block_15(message: types.Message):
    await bot.send_photo(chat_id = message.chat.id, photo = open('media/inno-potter.png', 'rb'), caption= 'ЗАДАНИЕ 2.')
    await asyncio.sleep(1)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("1️⃣ Р1")
    keyboard.add("2️⃣ Р2")
    keyboard.add("3️⃣ Р3")
    keyboard.add("4️⃣ Р4")
    await message.answer("Гарри Поттер по отношению к борьбе с темными силами в 1 книге (фильме)",
                         reply_markup=keyboard)
    await Progress2.msg_13.set()

async def answer20(message: types.Message):
    await message.answer(
        "Не соглашусь! Должной компетенцией Гарри еще точно не обладал, но при этом хотел бороться с темными силами. Он Р1.",
        reply_markup=types.ReplyKeyboardRemove())
    await block_16(message)

async def answer21(message: types.Message):
    counter.increase_counter()
    await message.answer(
        "Я тоже так считаю. Должной компетенцией Гарри еще точно не обладал, но при этом хотел бороться с темными силами.",
        reply_markup=types.ReplyKeyboardRemove())
    await block_16(message)

async def block_16(message: types.Message):
    await bot.send_photo(chat_id = message.chat.id, 
                         photo = open('media/inno-house-md.png', 'rb'),
                         caption = 'ЗАДАНИЕ 3.')
    await asyncio.sleep(1)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("▶️ Р1")
    keyboard.add("▶️ Р2")
    keyboard.add("▶️ Р3")
    keyboard.add("▶️ Р4")
    await message.answer("Доктор Хаус по отношению к общению с пациентами по сбору анамнеза",
                         reply_markup=keyboard)
    await Progress2.msg_14.set()

async def answer22(message: types.Message):
    await message.answer(
        "Неверно, потому что умения у него явно есть и при этом никакого желания.",
        reply_markup=types.ReplyKeyboardRemove())
    await block_17(message)

async def answer23(message: types.Message):
    counter.increase_counter()
    await message.answer(
        "Да, он точно это умеет, но совершенно не горит желанием и всячески избегает.",
        reply_markup=types.ReplyKeyboardRemove())
    await block_17(message)

async def block_17(message: types.Message):
    await bot.send_photo(chat_id = message.chat.id, 
                         photo = open('media/inno-aria.png', 'rb'),
                         caption = 'ЗАДАНИЕ 4.')
    await asyncio.sleep(1)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("⏺ Р1")
    keyboard.add("⏺ Р2")
    keyboard.add("⏺ Р3")
    keyboard.add("⏺️ Р4")
    await message.answer("Арья по отношению к соблюдению правил этикета",
                         reply_markup=keyboard)
    await Progress2.msg_15.set()

async def answer24(message: types.Message):
    await message.answer(
        "Не соглашусь! Она типичный Р2: совершенно не испытывала радости от необходимости соблюдать правила этикета и не особенно стремилась их освоить",
        reply_markup=types.ReplyKeyboardRemove())
    await block_18(message)

async def answer25(message: types.Message):
    counter.increase_counter()
    await message.answer(
        "Да, согласен! Она совершенно не испытывала радости от необходимости соблюдать правила этикета и не особенно стремилась их освоить.",
        reply_markup=types.ReplyKeyboardRemove())
    await block_18(message)

async def block_18(message: types.Message):
    await bot.send_photo(chat_id = message.chat.id, 
                         photo = open('media/inno-neznaika.png', 'rb'),
                         caption = 'ЗАДАНИЕ 5.')
    await asyncio.sleep(1)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("⏹ Р1")
    keyboard.add("⏹️ Р2")
    keyboard.add("⏹ Р3")
    keyboard.add("⏹ Р4")
    await message.answer("К какому типу относится Незнайка, который писал стихи?",
                         reply_markup=keyboard)
    await Progress2.msg_16.set()

async def answer26(message: types.Message):
    await message.answer(
        "Не думаю! Скорее он Р2:  у него и не получалось, и он не горел желанием это делать.",
        reply_markup=types.ReplyKeyboardRemove())
    await block_19(message)

async def answer27(message: types.Message):
    counter.increase_counter()
    await message.answer(
        "В точку! У него и не получалось, и он не горел желанием это делать.",
        reply_markup=types.ReplyKeyboardRemove())
    await block_19(message)

async def block_19(message: types.Message):
    correct_answers = counter.get_counter()
    if correct_answers in [0, 5]:
        word = 'правильных ответов'
    elif correct_answers == 1:
        word = 'правильный ответ'
    else:
        word = 'правильных ответа'
    Log().getLogger().info("{0} {1} из 5".format(correct_answers, word))

    await asyncio.sleep(2)
    await message.answer("Супер! Ты большой молодец, потренировался на примере известных персонажей определять уровни "
                        "профессионального развития и заодно почти закончил еще один раздел. У тебя {0} {1} из 5 возможных.".format(correct_answers, word))
    await asyncio.sleep(7)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("➡️ Да!")
    keyboard.add("➡️ Не хочется, в другой раз")
    await message.answer("Прежде, чем ты пойдешь дальше, предлагаю тебе решить парочку проверочных кейсов и закрепить знания.",
                         reply_markup=keyboard)
    await Progress2.msg_17.set()

async def answer28(message: types.Message):
    await message.answer(
        "Замечательно. Это не займет больше 3-5 минут.",
        reply_markup=types.ReplyKeyboardRemove())
    await block_20(message)

async def answer29(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Готов продолжить!")
    await message.answer("Хорошо, тогда жду тебя, до связи!",
                         reply_markup=keyboard)
    await Progress2.msg_18.set()

async def answer29_2(message: types.Message):
    await block_20(message)

async def block_20(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("🅿️1️⃣")
    keyboard.add("🅿️2️⃣")
    keyboard.add("🅿️3️⃣")
    keyboard.add("🅿️4️⃣")
    await message.answer("Вопрос 1. Александр работает в команде разработчиков меньше года и ещё ни разу не выполнил "
                         "работу без ошибок. Попытки руководителя как-то «расшевелить» его, направив на обучение, "
                         "не привели к успеху. Кажется, что Александр совсем пал духом. Руководитель решил сделать "
                         "ещё одну попытку помочь ему и закрепил за ним наставника. Какой уровень профессионального "
                         "развития у Александра?",
                         reply_markup=keyboard)
    await Progress2.msg_19.set()

async def answer30(message: types.Message):
    await message.answer(
        "Не соглашусь! У Александра много ошибок, и он пал духом, что свидетельствует о неуверенности в себе и снижении мотивации",
        reply_markup=types.ReplyKeyboardRemove())
    await block_21(message)

async def answer31(message: types.Message):
    await message.answer(
        "Абсолютно точно! У Александра много ошибок, и он пал духом, что свидетельствует о неуверенности в себе и снижении мотивации. ",
        reply_markup=types.ReplyKeyboardRemove())
    await block_21(message)

async def block_21(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("🅿1")
    keyboard.add("🅿2")
    keyboard.add("🅿3")
    keyboard.add("🅿4")
    await message.answer("Вопрос 2. Если на твой вопрос, сколько тебе понадобится времени на реализацию задачи, "
                         "сотрудник отвечает срок, который сильно короче, чем тот, который действительно нужен на ее "
                         "выполнение, то он скорее всего кто по уровню профессионального развития в этой задаче?",
                         reply_markup=keyboard)
    await Progress2.msg_20.set()

async def answer32(message: types.Message):
    await message.answer(
        "Неверно! Это характерно для новичка в задаче – Р1. Именно они просят на выполнение нереалистично короткие "
        "сроки, потому что в вопросе не разбираются, а энтузиазма, желания проявить себя и мотивации у них много",
        reply_markup=types.ReplyKeyboardRemove())
    await block_22(message)

async def answer33(message: types.Message):
    await message.answer(
        "Верно! Именно новички в задаче просят на ее выполнение нереалистично короткие сроки, потому что в вопросе не "
        "разбираются, а энтузиазма, желания проявить себя и мотивации у них много",
        reply_markup=types.ReplyKeyboardRemove())
    await block_22(message)

async def block_22(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("🅿1️⃣")
    keyboard.add("🅿2️⃣")
    keyboard.add("🅿3️⃣")
    keyboard.add("🅿4️⃣")
    await message.answer("Вопрос 3. Ольга, опытный сотрудник отдела, получила новое для неё задание. Выполняет работу "
                         "с энтузиазмом, хотя испытывает серьёзные трудности и показывает низкие результаты. "
                         "Руководителю важно, чтобы Ольга справилась с заданием. Какой уровень профессионального "
                         "развития у Ольги?",
                         reply_markup=keyboard)
    await Progress2.msg_21.set()

async def answer34(message: types.Message):
    await message.answer(
        "Не могу согласиться! У Ольги низкая компетентность, так как задние новое даже для опытного сотрудника, "
        "высокая мотивация – выполняет работу с энтузиазмом. Значит, она Р1. ",
        reply_markup=types.ReplyKeyboardRemove())
    await block_23(message)

async def answer35(message: types.Message):
    await message.answer(
        "В точку! Низкая компетентность, так как задние новое даже для опытного сотрудника, высокая мотивация – "
        "выполняет работу с энтузиазмом.",
        reply_markup=types.ReplyKeyboardRemove())
    await block_23(message)

async def block_23(message: types.Message):
    await asyncio.sleep(4)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("1")
    keyboard.add("2")
    keyboard.add("3")
    keyboard.add("4")
    keyboard.add("5")
    await bot.send_sticker(chat_id = message.chat.id, sticker = 'CAACAgIAAxkBAAID22KNHELIQv32URs_wMjahYdBbfDxAAI4EQACe2KYScU9o5OriGzxJAQ')
    await message.answer("Поздравляю с завершением второго блока! Как тебе? Оцени от 0 до 5",
                         reply_markup=keyboard)
    await Progress2.msg_22.set()

async def answer36(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Да, продолжу!")
    keyboard.add("Чуть позже")
    await message.answer(
        "Спасибо за обратную связь! Если осталось желание потренироваться и закрепить изученное, то ты всегда можешь "
        "вернуться и перечитать теорию, потренироваться на кейсах. Готов идти в следующий раздел?",
        reply_markup=keyboard)
    await Progress2.msg_23.set()

async def answer38(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Готов!")
    await message.answer("Договорились, я на связи и жду, когда ты вернешься.", reply_markup=keyboard)
    await Progress2.msg_24.set()

async def answer37(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Отлично!", reply_markup=types.ReplyKeyboardRemove())
    from messages.chapter3 import third_chapter_answer_1
    await third_chapter_answer_1(message)

async def answer39(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Окей, погнали дальше",reply_markup = types.ReplyKeyboardRemove())
    from messages.chapter3 import third_chapter_answer_1
    await third_chapter_answer_1(message)
