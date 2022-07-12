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

def register_handlers_chapter4(dp: Dispatcher):
    dp.register_message_handler(fourth_chapter_welcome, commands="chapter4", state='*')
    dp.register_message_handler(fourth_chapter_welcome, Text(equals="4. Особенности управления разными типами сотрудников"))
    dp.register_message_handler(fourth_chapter_answer_1, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress4.msg_1)
    dp.register_message_handler(fourth_chapter_answer_2, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress4.msg_2)
    dp.register_message_handler(fourth_chapter_answer_3, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress4.msg_3)
    dp.register_message_handler(fourth_chapter_answer_4, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress4.msg_4)
    dp.register_message_handler(fourth_chapter_answer_5, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress4.msg_5)
    dp.register_message_handler(fourth_chapter_answer_6, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress4.msg_6)
    dp.register_message_handler(fourth_chapter_answer_7, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress4.msg_7)
    dp.register_message_handler(fourth_chapter_answer_8, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress4.msg_8)
    dp.register_message_handler(fourth_chapter_answer_9, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress4.msg_9)
    dp.register_message_handler(fourth_chapter_answer_10, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress4.msg_10)
    dp.register_message_handler(fourth_chapter_answer_11, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress4.msg_11)
    dp.register_message_handler(fourth_chapter_answer_12, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress4.msg_12)
    dp.register_message_handler(fourth_chapter_answer_13, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress4.msg_13)
    dp.register_message_handler(fourth_chapter_answer_14, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress4.msg_14)
    dp.register_message_handler(fourth_chapter_answer_15, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress4.msg_15)
    dp.register_message_handler(fourth_chapter_answer_16, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress4.msg_16)
    dp.register_message_handler(fourth_chapter_answer_17, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress4.msg_17)
    dp.register_message_handler(fourth_chapter_answer_18, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress4.msg_18)
    dp.register_message_handler(fourth_chapter_answer_19, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress4.msg_19)
    dp.register_message_handler(fourth_chapter_answer_20, ContentTypeFilter(content_types=types.ContentTypes.TEXT), state=Progress4.msg_20)

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
        await message.answer("Так держать! 👍", reply_markup=types.ReplyKeyboardRemove())
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

async def fourth_chapter_block_3(message: types.Message):
    await asyncio.sleep(1)

    await message.answer("SMART – это метод описания цели, включающий в себя: конкретность, измеримость, достижимость, важность и определённость по срокам. "
                             , reply_markup=types.ReplyKeyboardRemove())

    #картинка

    await asyncio.sleep(2)

    await message.answer("Например, «Написать книгу» – некорректная формулировка цели. А вот «выпустить книгу на тему “Управление со смыслом”"
    "объёмом не меньше 300 страниц к августу 2026 г. – это цель по SMART. Конкретная, измеримая, реалистичная, но главное определенная во времени."
    " Так вот, смартируя цели для разных типов сотрудников, важно делать акцент на определенные критерии. ", reply_markup=types.ReplyKeyboardRemove())


    await asyncio.sleep(3)


    await message.answer("Вы ставите задачу сотруднику Р1, такому сотруднику сложно поставить задачу реалистичную, "
    "ведь с новичком в задаче мы не всегда можем понять компетентность, но и с другой стороны, сильная мотивация поможет новичку "
    "справиться даже с задачей, которая для него немного на вырост. Поэтому при постановке задач делайте акценты на максимальной "
    "конкретности, измеримости, определённости во времени.", reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(3)


    await message.answer("Для Р2, все критерии должны быть максимально выражены. То есть для Р2 используем SMART в полном объеме. ", reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(2)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Конкретность")
    keyboard.add("Измеримость")
    keyboard.add("Временной параметр")

    await message.answer("Как ты думаешь, а ставя цели по SMART для Р3, на какой критерий можно  не делать сильного акцента? ", reply_markup=keyboard)

    await Progress4.msg_5.set()

async def fourth_chapter_answer_5(message: types.Message):
    await asyncio.sleep(1)

    if(message.text == "Конкретность!"):
        await message.answer("Верно", reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer("Не соглашусь с тобой!", reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(1)

    await fourth_chapter_block_5(message)


async def fourth_chapter_block_5(message: types.Message):
    await message.answer("Для Р3 можно снизить конкретность, ведь у сотрудника довольно высокая компетентность, но низкая мотивация. "
                         "Смартируя задачу для Р3, важно уделить много времени, реалистичности цели, обсудить амбициозность цели и согласованности с другими целями, "
                         "ведь возможно мотивации не хватает сотруднику из-за несогласованности того, к чему он стремится. ", reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(3)

    await message.answer("Для Р4 обозначите, как будете измерять результат, спросите о возможностях, обозначьте срок, сотрудник такого уровня мотивации и "
    "компетентности сам конкретизирует способ реализации задачи. ", reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(3)

    await message.answer("Таким образом, получается такая картина.  ", reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(1)

    #picture 2


    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Да, все по полочкам")
    keyboard.add("Надо будет попробовать и проверить")

    await message.answer("С постановкой целей мы разобрались! Все ли понятно? ", reply_markup=keyboard)

    await Progress4.msg_6.set()


async def fourth_chapter_answer_6(message: types.Message):
    await asyncio.sleep(1)

    if(message.text == "Да, все по полочкам"):
        await message.answer("Супер! Осталось только применить на практике. ", reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer("Обязательно попробуй и проверь, как это работает на практике!", reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(1)

    await fourth_chapter_block_6(message)


async def fourth_chapter_block_6(message: types.Message):
    await message.answer("Перейдем к контролю разных типов сотрудников."
"Важно! О контроле необходимо договариваться с сотрудником на берегу, то есть заранее, тогда, когда вы поставили ему задачу. Зачем это? "
"- сотрудник воспримет контроль адекватно как помощь и обратную связь;"
"- ты сделаешь работу более структурированной и организованной;"
"- повысишь вероятность того, что задачи будут выполнены качественно и в срок.  ", reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(2)

    await message.answer("Контроль – функция управления, которая является сравнением того, что было задумано, с тем, что получилось.", reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(1)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Нет!")
    keyboard.add("Нормально отношусь")

    await message.answer("Скажи, а ты любишь, чтобы тебя контролировали?", reply_markup=keyboard)

    await Progress4.msg_7.set()

async def fourth_chapter_answer_7(message: types.Message):
    if(message.text == "Нет!"):
        await message.answer("Это очень по-человечески, понимаю! ", reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer("Хорошо! При этом надо помнить, что многие люди не очень радостно относятся к тому, что их постоянно контролируют.", reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(1)

    await fourth_chapter_block_7(message)


async def fourth_chapter_block_7(message: types.Message):
    await message.answer("Хочу сфокусировать твое внимание на том, что очень важно контролировать деятельность, а не самого человека. "
    "Фишка в том, что люди чаще всего спокойно  относятся к контролю деятельности, но негативно реагируют в случае перехода на личности. ", reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(2)

    await message.answer("Какие виды контроля бывают? "
    "По процессу или по результату. ", reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(1)

    await message.answer("КАРТИНКА"
"Контроль процесса: руководитель смотрит, КАК сотрудник выполняет задачу и корректирует, говорит, "
"как можно сделать эффективнее Контроль результата: Руководитель оценивает, что получилось"
" и дает обратную связь о качестве выполненной работы. ", reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(2)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("В процессе")
    keyboard.add("По факту выполнения")
    keyboard.add("Так и так")

    await message.answer("А ты сам как предпочитаешь контролировать?", reply_markup=keyboard)

    await Progress4.msg_8.set()


async def fourth_chapter_answer_8(message: types.Message):
    if(message.text == "В процессе"):
        await message.answer("Обрати внимание, что это очень затратный по времени способ, но для многих сотрудников необходимый. ", reply_markup=types.ReplyKeyboardRemove())
    elif(message.text == "По факту выполнения"):
        await message.answer("Неплохой вариант, но для некоторых сотрудников этого точно недостаточно", reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer("Отлично, однако это потребует от тебя много времени и энергии!", reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(1)

    await fourth_chapter_block_8(message)

async def fourth_chapter_block_8(message: types.Message):
    await asyncio.sleep(1)

    await message.answer("А теперь давай поговорим о том, как контролировать сотрудников с разным уровнем профессионального развития. ", reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(2)

    await message.answer("Давай представим, что тебе нужно проконтролировать задачу, на выполнение которой запланировано 2 недели. "
    "Для Р1 необходимо разделить весь срок выполнения на интервалы. В нашем случае, это будет, к примеру, 2 раза в неделю.  "
    "В конце каждого отрезка анализируем, что сделано и планируем, что делаем дальше до следующей контрольной точки.  ", reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(3)


    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Вообще не отходить от него")
    keyboard.add("Встреча один раз в день")

    await message.answer("Как думаешь, а как контролировать Р2?", reply_markup=keyboard)

    await Progress4.msg_9.set()

async def fourth_chapter_answer_9(message: types.Message):
    await asyncio.sleep(1)

    await message.answer("Для Р2 целесообразно в конце недели обсудить достигнутый результат, похвалить его за прогресс, а в начале недели договориться, чем он будет заниматься на предстоящей неделе. "
    , reply_markup=types.ReplyKeyboardRemove())

    await fourth_chapter_block_9(message) 


async def fourth_chapter_block_9(message: types.Message):

    await asyncio.sleep(1)

    await message.answer("Р3 необходимо контролировать в два этапа: чуть раньше половины срока, примерно в конце одной трети всего времени. Вторая точка контроля будет незадолго до дедлайна, в начале последней трети. "
    , reply_markup=types.ReplyKeyboardRemove())

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Нет, он профи")
    keyboard.add("Да, несмотря на то, что он профи")

    await message.answer("Как считаешь, нужно ли контролировать Р4?", reply_markup=keyboard)

    await Progress4.msg_10.set()

async def fourth_chapter_answer_10(message: types.Message):
    await asyncio.sleep(1)

    await message.answer("И последний важный момент:  сотрудников Р1 и Р2 необходимо контролировать в процессе, а с Р3 и Р4 достаточно сверяться по результатам. "
    , reply_markup=types.ReplyKeyboardRemove())

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Огонь! Очень зашла")
    keyboard.add("Так себе…")
    keyboard.add("Было кое-что полезное")

    await message.answer("Как тебе тема контроля? Зашла?", reply_markup=keyboard)

    await Progress4.msg_11.set()

async def fourth_chapter_answer_11(message: types.Message):
    await asyncio.sleep(1)

    await message.answer("Спасибо тебе за ответ!", reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(1)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Классная тема")
    keyboard.add("Это самое сложное")

    await message.answer("Мы поговорили с тобой о постановке задач и контроле разных типов сотрудников. Давай теперь немного о мотивации!", reply_markup=keyboard)

    await Progress4.msg_12.set()


async def fourth_chapter_answer_12(message: types.Message):
    await asyncio.sleep(1)

    if(message.text == "Классная тема"):
        await message.answer("Однозначно! Мотивировать и вовлекать – дело важное. ", reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer("Для многих руководителей да, согласен с тобой ", reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(1)

    await fourth_chapter_block_10(message)


async def fourth_chapter_block_10(message: types.Message):
    await message.answer("Мотивация – желание человека тратить силы и время на выполнение задачи и уверенность в том, что он может эту задачу выполнить.  ", reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(2)


    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Р1")
    keyboard.add("Р2")
    keyboard.add("Р2 и P3")
    keyboard.add("Р4")
    keyboard.add("Р3")

    await message.answer("Помнишь, у сотрудников с каким УПР есть сложности с мотивацией? Помнишь, у сотрудников с каким УПР есть сложности с мотивацией? ", reply_markup=keyboard)

    await Progress4.msg_13.set()

async def fourth_chapter_answer_13(message: types.Message):
    await asyncio.sleep(1)

    if(message.text == "Р1" or message.text == "Р4"):
        await message.answer("Нет, у сотрудников Р2 и Р3 ", reply_markup=types.ReplyKeyboardRemove())
    elif(message.text == "Р2" or message.text == "Р3"):
        await message.answer("Ты прав, но ответ неполный. У Р2 и Р3.  ", reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer("В точку! ", reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(1)

    await fourth_chapter_block_11(message)



async def fourth_chapter_block_11(message: types.Message):
    await message.answer("Давай начнем с Р2. Это разочаровавшиеся ребята с не очень высокой компетентностью. Они требуют от руководителя очень много внимания и “вложений” времени и сил.",
     reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(2)

    await message.answer("КАРТИНКА - Как повысить мотивацию Р2?"
"• Ставь задачи адекватного уровня сложности."
"• Предоставляй дополнительные ресурсы: информацию, время, деньги, поддержку и т.д."
"• Рассказывай истории успеха, как подобные цели были достигнуты."
"• Поднимай его самооценку, делай акцент на том, что получается."
"• Дай ему пробовать, подстрахуй от ошибок."
"• Помоги найти пользу для сотрудника в самом процессе достижения цели.",
     reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(3)


    await message.answer("Теперь про Р3. Он очень компетентен, но мотивация его шалит и то взлетает, то снова падает. ",  reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(1)

    await message.answer("КАРТИНКА"
"Как повысить мотивацию Р3?"
"• Найти его личные мотиваторы и “дать” ему их"
"• Обсудить смысл и ценность выполнения задачи"
"• Рассказать о возможных потерях в случае невыполнения задачи."
"• Предоставить свободу и самостоятельность в достижении цели. ",  reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(3)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Да")
    keyboard.add("Не очень")

    await message.answer("Все ли тебе понятно? ", reply_markup=keyboard)

    await Progress4.msg_14.set()

async def fourth_chapter_answer_14(message: types.Message):
    await asyncio.sleep(1)

    if(message.text == "Да"):
        await message.answer("Отлично. ", reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer("Ты всегда можешь вернуться в начало раздела и перечитать. ", reply_markup=types.ReplyKeyboardRemove())

    await fourth_chapter_block_12(message)



async def fourth_chapter_block_12(message: types.Message):
    await asyncio.sleep(1)

    await message.answer("Мотивировать Р1 и Р4 тоже нужно, но этому уделяется не так много времени, скорее тебе важно не допускать демотивации этих сотрудников, поддерживать их.  ", 
     reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(2)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Да, все мы люди")
    keyboard.add("Думаю, по-разному")

    await message.answer("Обсуждая тему мотивации, я не могу не сказать о похвале. Она важна для сотрудников абсолютно всех типов :) Как ты думаешь, всех нужно хвалить одинаково?  ", reply_markup=keyboard)

    await Progress4.msg_15.set()

async def fourth_chapter_answer_15(message: types.Message):
    await asyncio.sleep(1)

    await message.answer("Спасибо, что поделился своим мнением! Расскажу, как это вижу я, давай поговорим о нюансах похвалы сотрудников с разным УПР. ", 
     reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(2)

    await fourth_chapter_block_13(message)

async def fourth_chapter_block_13(message: types.Message):

    await message.answer("Если перед нами новичок, то ему важно подсвечивать то, что получается. Иногда найти эти моменты сложно, но я подскажу тебе варианты. "
    "Например,"
  "• Ты быстро учишься, быстро растешь"
  "• Ты сделал почти все верно (совершил меньше ошибок, чем обычно новички)"
  "• Ты справила почти без помощи"
  "• Ты запомнил почти все"
  "• Молодец, что обратился за помощью.  "
  "***********************"
  "А еще можно: "
  "• Похвалить за находчивость или догадливость"
  "• Похвалить за настрой, настойчивость ", 
     reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(4)

    await message.answer("Как хвалить Р2? "
"• После выполнения спроси, почему он делал нечто так, а не иначе и хвали, если сотрудник объяснил логику верно"
"• Хвали за точность формулировки вопроса"
"• Хвали за попытки понять, разобраться ", 
     reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(3)

    await message.answer("Почему именно за это? Компетентность есть, но невысокая, поверхностная, а понимания глубины, логики многих процессов нет. "
    "Поэтому мы его хвалим, когда он хочет в чем-то разобраться, изучить вопрос детально, сделать свои выводы", 
    reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(3)


    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Задача важная, могу поручить только тебе")
    keyboard.add("Ты как всегда на высоте")
    keyboard.add("Я рад, что мы работаем вместе")
    keyboard.add("Все бы так работали, как ты!")

    await message.answer("Как хвалить капризных Р3? Что думаешь, что бы ты выбрал? ", reply_markup=keyboard)

    await Progress4.msg_16.set()



async def fourth_chapter_answer_16(message: types.Message):
    await asyncio.sleep(1)

    await message.answer("Отлично! Все эти варианты хороши для Р3. ", reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(1)

    await fourth_chapter_block_14(message)


async def fourth_chapter_block_14(message: types.Message):

    await message.answer("Как еще похвалить и замотивировать Р3?"
    "Задача делается за 3 дня, но, думаю, ты справишься за 2"
    "• Задача сложная, потребуется твой талант (находить подход" 
    "к людям, нестандартные пути, нужных людей)"
    "• Поручаю тебе, задача важная, нужен кто-то, кто точно не упустит важных деталей"
    "• Нужен кто-то, кому хватит опыта, сообразительности"
    "• Ты как всегда отлично справился"
    "• Спасибо, на тебя всегда можно положиться ", reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(3)

    await message.answer("Спасибо, что поделился своим мнением! Расскажу, как это вижу я, давай поговорим о нюансах похвалы сотрудников с разным УПР.  ", reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(1)
    
    await message.answer("Как хвалим профессионала? Мы его благодарим. Мы ценим, что он с нами. "
    "• Очень тебе благодарен!"
    "• Ты всегда выручаешь"
    "• Я ценю все, что ты делаешь для нашей команды."
    "Этот человек, который сам может сделать все идеально. Его очень важно поощрять, чтобы не демонизировать.", reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(3)

    await message.answer("Ура!! Поздравляю тебя! Теория уже позади, ответь на несколько моих вопросов, чтобы понять, насколько хорошо ты усвоил информацию из этого раздела.   ", reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(2)

    await message.answer("Ответь на несколько вопросов по кейсу. ", reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(1)

    await message.answer("КЕЙС"
    "Тимлид Рома поговорил с новой сотрудницей Аней, которая работает всего пару месяцев и ей все очень нравится, поставил ей задачи с четким обозначением, "
    "что и в какой срок нужно сделать, расписал подробный план и попросил отчитываться каждый вечер в 18:00. "
    "Сказал, что всегда на связи и готов ответить на все вопросы.  ", reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(3)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Да")
    keyboard.add("Нет")

    counter.set_counter(0)

    await message.answer("Вопрос 1. Как ты думаешь, совершил ли управленческую ошибку Роман? ", reply_markup=keyboard)

    await Progress4.msg_17.set()


async def fourth_chapter_answer_17(message: types.Message):
    await asyncio.sleep(1)

    if(message.text == "Да"):
        await message.answer("Интересно было бы обсудить, мне кажется, что в целом все ок ", reply_markup=types.ReplyKeyboardRemove())
    else:
        counter.increase_counter()
        await message.answer("Согласен с тобой! ", reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(1)

    await fourth_chapter_block_15(message)

async def fourth_chapter_block_15(message: types.Message):
    await message.answer("Спасибо, что поделился своим мнением! Расскажу, как это вижу я, давай поговорим о нюансах похвалы сотрудников с разным УПР.  ", reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(2)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Да, так как Аня Р1")
    keyboard.add("Нет, можно не так подробно и не так часто")

    await message.answer("Вопрос 2. Как ты думаешь, правильно ли Роман поставил задачи и обозначил точки контроля?", reply_markup=keyboard)

    await Progress4.msg_18.set()

async def fourth_chapter_answer_18(message: types.Message):
    await asyncio.sleep(1)

    if(message.text == "Да, так как Аня Р1"):
        await message.answer("Согласен! Для новичка это самый хороший вариант.  ", reply_markup=types.ReplyKeyboardRemove())
        counter.increase_counter()
    else:
        await message.answer("Не совсем согласен. Для новичка это как раз самый хороший вариант ", reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(1)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Только по процессу")
    keyboard.add("По процессу и результату")
    keyboard.add("По результату")

    await message.answer("Вопрос 3. Как Роману стоит мотивировать Анну? ", reply_markup=keyboard)

    await Progress4.msg_19.set()    


async def fourth_chapter_answer_19(message: types.Message):
    await asyncio.sleep(1)

    if(message.text == "Только по процессу"):
        await message.answer("Хороший вариант, но неполный: проанализировать результат и дать обратную связь тоже важно. ", reply_markup=types.ReplyKeyboardRemove())
    elif(message.text == "По процессу и результату"):
        await message.answer("Это наиболее удачный вариант!  ", reply_markup=types.ReplyKeyboardRemove())
        counter.increase_counter()
    else:
        await message.answer("Этого будет недостаточно для сотрудника уровня Р1 ", reply_markup=types.ReplyKeyboardRemove())

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Конкретность и реалистичность")
    keyboard.add("Да, так как Аня Р1")
    keyboard.add("Нет, можно не так подробно и не так часто")

    await message.answer("Вопрос 4. Какие из перечисленных критериев постановки целей по SMART можно упустить, ставя цели Анне? ", reply_markup=keyboard)

    await Progress4.msg_20.set()   

async def fourth_chapter_answer_20(message: types.Message):
    await asyncio.sleep(1)

    if(message.text == "Нет, можно не так подробно и не так часто"):
        await message.answer("Абсолютно точно!"
        "Ставя цели для Р1, лучше использовать все критерии SMART. Иногда можно упустить только реалистичность (в связи с тем, что мы не знаем всего потенциала сотрудника) ",
        reply_markup=types.ReplyKeyboardRemove())
        counter.increase_counter()
    else:
        await message.answer("Увы, нет! Ставя цели для Р1 лучше использовать все критерии SMART. Иногда можно упустить только реалистичность (в связи с тем, что мы не знаем всего потенциала сотрудника) ",
        reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(2)

    correct_answers = counter.get_counter()
    if correct_answers == 0:
        word = 'правильных ответов'
    elif correct_answers == 1:
        word = 'правильный ответ'
    else:
        word = 'правильных ответа'

    await message.answer("ЕЕЕ! Ты ответил на все вопросы! И у тебя {0} {1} из 4. У тебя остался всего один маленький шажок до финала – итоговый тест!".format(correct_answers, word),
    reply_markup=types.ReplyKeyboardRemove()) 