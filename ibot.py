#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gc import callbacks
import logging
from datetime import datetime
from pydoc import text

import psycopg2
import yaml
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram.utils.callback_data import CallbackData
import asyncio


class Form(StatesGroup):
    name = State()


with open("config.yaml", "r") as ymlfile:
    config = yaml.safe_load(ymlfile)

db = config['DB']
connect = psycopg2.connect(database=db['NAME'], user=db['USER'], password=db['PASSWORD'], host=db['HOST'],
                           port=db['PORT'])
print("Opened database successfully")
cur = connect.cursor()
today = datetime.now()
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
BIO, BIO_BUTTON, BLOCK_1_BUTTON = range(3)

storage = MemoryStorage()
# Объект бота
bot = Bot(token=config['TELEGRAM']['TOKEN'])
# Диспетчер для бота
dp = Dispatcher(bot, storage=storage)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands="start")
async def cmd_answer(message: types.Message):
    await Form.name.set()
    await message.answer("Здравствуйте! Как вас зовут?")


@dp.message_handler(state=Form.name)
async def process_name(message: types.Message, state: FSMContext):
    logger.info("Name is %s", message.text)
    postgres_insert_query = """INSERT INTO clients (NAME, REG_DATE) VALUES (%s,%s) ON CONFLICT DO NOTHING"""
    record_to_insert = (message.text, today)
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
    await state.finish()


@dp.message_handler(Text(equals="Не удивил"))
async def cmd_answer(message: types.Message):
    await message.answer("А ты серьезный человек, уверен, что мы найдём общий язык:-)",
                         reply_markup=types.ReplyKeyboardRemove())
    await block_1(message)


@dp.message_handler(Text(equals="Да супер"))
async def cmd_answer(message: types.Message):
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


@dp.message_handler(Text(equals="Готов на все 100!"))
async def cmd_answer(message: types.Message):
    await message.answer("Отлично, с таким настроем мы с тобой быстро во всем разберемся:-)",
                         reply_markup=types.ReplyKeyboardRemove())
    await block_2(message)


@dp.message_handler(Text(equals="Давай попробуем"))
async def cmd_answer(message: types.Message):
    await message.answer("Сделаю все возможное, чтобы тебе понравилось и было полезно! Поехали!",
                         reply_markup=types.ReplyKeyboardRemove())
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


@dp.message_handler(Text(equals="1. Управление. Причины невыполнения задач"))
async def cmd_answer(message: types.Message):
    await message.answer("Давай начнем с того, что обсудим, что такое управление. Я буду рассказывать просто, "
                         "без тяжеловесных терминов", reply_markup=types.ReplyKeyboardRemove())
    await asyncio.sleep(3)
    await message.answer("Управление - это деятельность над деятельностью. То есть управляя, руководитель не сам "
                         "выполняет какие-либо рабочие операции, а организует работу других людей, действует их руками")
    await asyncio.sleep(3)
    await message.answer("Конечно, иногда руководитель тоже работает как специалист, но он должен делать это только в "
                         "том случае, когда сотрудники не справляются, тогда руководитель это компенсирует. Самое "
                         "важное помнить: чем больше ты работаешь как специалист, тем меньше управляешь!")
    await asyncio.sleep(3)
    await message.answer("КАРТИНКА: Руководитель - это сотрудник, который выполняет задачи руками других людей")
    await asyncio.sleep(2)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Не мог")
    keyboard.add("Не хотел")
    keyboard.add("То и другое")
    await message.answer("Цель руководителя - организовать процесс выполнения задач и достижения целей. Но бывает "
                         "такое, что сотрудник не выполняет задачи, которые поставил перед ним руководитель. Как ты "
                         "думаешь, почему так происходит?", reply_markup=keyboard)


@dp.message_handler(Text(equals="Не мог"))
async def cmd_answer(message: types.Message):
    await message.answer("Верно, но не только, на самом деле сотрудник мог и не хотеть, и не понять, что делать. Всего "
                         "можно выделить 4 причины", reply_markup=types.ReplyKeyboardRemove())
    await block_3(message)


@dp.message_handler(Text(equals="Не хотел"))
async def cmd_answer(message: types.Message):
    await message.answer("Ты прав! Но это еще не все. Сотрудник мог не понять, что делать, не иметь ресурсов и так "
                         "далее. Всего можно выделить 4 причины", reply_markup=types.ReplyKeyboardRemove())
    await block_3(message)


@dp.message_handler(Text(equals="То и другое"))
async def cmd_answer(message: types.Message):
    await message.answer("В точку! Но есть еще пара причин. Сейчас все расскажу",
                         reply_markup=types.ReplyKeyboardRemove())
    await block_3(message)


async def block_3(message: types.Message):
    await asyncio.sleep(1)
    await message.answer('Итак, есть 4 причины, по которым сотрудник может не выполнить поставленную перед ним '
                         'задачу: не мог, не понял, не умел, не хотел. Если твой подчиненный не выполнил задачу или '
                         'сделал это с ненадлежащим качеством или не в срок, проверять причины необходимо именно в '
                         'этом порядке')
    await asyncio.sleep(3)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Причем тут я?")
    keyboard.add("Понятное дело")
    await message.answer('И знаешь, что самое интересное? Если сотрудник не выполнил задачу, то в этом есть доля и '
                         'твоей управленческой недоработки. Согласен?', reply_markup=keyboard)


@dp.message_handler(Text(equals="Причем тут я?"))
async def cmd_answer(message: types.Message):
    await message.answer("А при том, что значит, какая-то из управленческих функций не была реализована тобой",
                         reply_markup=types.ReplyKeyboardRemove())
    await block_4(message)


@dp.message_handler(Text(equals="Понятное дело"))
async def cmd_answer(message: types.Message):
    await message.answer("Солидарен с тобой! Смотри на картинку, и станет понятно, в чем управленческая ошибка в "
                         "зависимости от причины невыполнения задачи",
                         reply_markup=types.ReplyKeyboardRemove())
    await block_4(message)


async def block_4(message: types.Message):
    await asyncio.sleep(1)
    await message.answer('Картинка\n'
                         'Не мог -> руководитель плохо запланировал\n'
                         'Не понял -> руководитель нечетко поставил задачу\n'
                         'Не умеет -> не реализована функция обучения\n'
                         'Не хотел -> руководитель не замотивировал')
    await asyncio.sleep(3)
    await message.answer('Теперь ты знаешь, что нужно делать, чтобы избежать таких досадных управленческих '
                         'недоразумений и в разы увеличить процент выполненных задач. Для этого нужно знать и '
                         'выполнять ключевые управленческие функции')
    await asyncio.sleep(3)
    await message.answer('Картинка:\n'
                         'Основные функции руководителя\n'
                         'Постановка целей и задач\n'
                         'Планирование\n'
                         'Контроль\n'
                         'Мотивирование\n'
                         'Обучение и развитие сотрудников')
    await asyncio.sleep(3)
    await message.answer('Ну что ж, теперь ты знаешь какие есть функции у руководителя и какой функции нужно уделить '
                         'больше внимания, если сотрудник не выполняет задачу')
    await asyncio.sleep(3)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Постановка целей и задач")
    keyboard.add("Планирование")
    keyboard.add("Контроль")
    keyboard.add("Мотивация")
    keyboard.add("Обучение")
    await message.answer('Хочу спросить у тебя, как ты думаешь, какую функцию необходимо прокачать именно тебе?',
                         reply_markup=keyboard)


@dp.message_handler(Text(equals=["Постановка целей и задач", "Планирование", "Контроль", "Мотивация", "Обучение"]))
async def cmd_answer(message: types.Message):
    await message.answer('Спасибо, что поделился. В этом курсе мы коротко рассмотрим некоторые из этих функций в '
                         'рамках изучаемых тем',
                         reply_markup=types.ReplyKeyboardRemove())
    await asyncio.sleep(2)
    await message.answer('Мы с тобой узнали, что такое управление, а также о причинах невыполнения задач. Давай я '
                         'задам тебе пару вопросов, чтобы ты мог проверить, насколько хорошо усвоил материал')
    await asyncio.sleep(3)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("➡️ Специалист")
    keyboard.add("➡️ Руководитель")
    await message.answer('Вопрос 1\n'
                         'Тимлид Денис сегодня целый час разговаривал со своей сотрудницей Анной, которая в последнее '
                         'время пала духом и ничего не хочет, совершает ошибки. Денис пытался подбодрить её и найти '
                         'для неё интересные задачи. Денис в данном случае выполнял функцию специалиста или '
                         'руководителя?', reply_markup=keyboard)


@dp.message_handler(Text(equals="➡️ Специалист"))
async def cmd_answer(message: types.Message):
    await message.answer("Не согласен с тобой! В данном случае он проводил мотивационную беседу, а значит, "
                         "работал как руководитель",
                         reply_markup=types.ReplyKeyboardRemove())
    await block_5(message)


@dp.message_handler(Text(equals="➡️ Руководитель"))
async def cmd_answer(message: types.Message):
    await message.answer("В точку! Мотивирование - функция руководителя",
                         reply_markup=types.ReplyKeyboardRemove())
    await block_5(message)


async def block_5(message: types.Message):
    await asyncio.sleep(2)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("➡️ Планирование")
    keyboard.add("➡️ Обучение")
    keyboard.add("➡️ Мотивирование")
    await message.answer('Вопрос 2\n'
                         'Если для выполнения задачи руководитель выбрал сотрудника, у которго на данный момент нет '
                         'ресурса для выполнения задачи, то какую функцию он не реализовал?', reply_markup=keyboard)


@dp.message_handler(Text(equals="➡️ Планирование"))
async def cmd_answer(message: types.Message):
    await message.answer("Верно! Выбирая, кому поручить задачу, нужно всегда анализировать, у кого есть время, "
                         "силы и другие ресурсы для её выполнения, то есть планировать",
                         reply_markup=types.ReplyKeyboardRemove())
    await block_6(message)


@dp.message_handler(Text(equals="➡️ Обучение"))
async def cmd_answer(message: types.Message):
    await message.answer("Не соглашусь! Выбирая, кому поручить задачу, нужно всегда анализировать, у кого есть время, "
                         "силы и другие ресурсы для её выполнения, то есть планировать",
                         reply_markup=types.ReplyKeyboardRemove())
    await block_6(message)


@dp.message_handler(Text(equals="➡️ Мотивирование"))
async def cmd_answer(message: types.Message):
    await message.answer("Увы нет. Выбирая, кому поручить задачу, нужно всегда анализировать, у кого есть время, "
                         "силы и другие ресурсы для её выполнения, то есть планировать",
                         reply_markup=types.ReplyKeyboardRemove())
    await block_6(message)


async def block_6(message: types.Message):
    await asyncio.sleep(2)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("➡️ Контроль")
    keyboard.add("➡️ Постановка целей")
    keyboard.add("➡️ Обучение")
    await message.answer('Вопрос 3\n'
                         'Сотрудник не понял, что именно нужно делать. Какая функция в данном случае "хромает" у '
                         'руководителя?', reply_markup=keyboard)


@dp.message_handler(Text(equals="➡️ Контроль"))
async def cmd_answer(message: types.Message):
    await message.answer("Неверно!",
                         reply_markup=types.ReplyKeyboardRemove())
    await block_7(message)


@dp.message_handler(Text(equals="➡️ Постановка целей"))
async def cmd_answer(message: types.Message):
    await message.answer("Именно так!",
                         reply_markup=types.ReplyKeyboardRemove())
    await block_7(message)


@dp.message_handler(Text(equals="➡️ Обучение"))
async def cmd_answer(message: types.Message):
    await message.answer("Не совсем!",
                         reply_markup=types.ReplyKeyboardRemove())
    await block_7(message)


async def block_7(message: types.Message):
    await message.answer('Чтобы сотрудник понимал, что ему делать и четко видел образ конечного результата, '
                         'руководителю нужно грамотно ставить цели')
    await asyncio.sleep(2)
    await message.answer('Спасибо что ответил на все вопросы! И у тебя <подставить значение> правильных ответов из 3')
    await asyncio.sleep(2)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Да")
    keyboard.add("Вернусь позже")
    await message.answer('Готов перейти к следующему блоку, в котором мы поговорим об уровнях профессионального '
                         'развития сотрудников?', reply_markup=keyboard)


@dp.message_handler(Text(equals="Да"))
async def cmd_answer(message: types.Message):
    await message.answer("Отлично, продолжаем!",
                         reply_markup=types.ReplyKeyboardRemove())
    await block_8(message)


@dp.message_handler(Text(equals="Вернусь позже"))
async def cmd_answer(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Продолжить")
    await message.answer("Хорошо, возвращайся, я всегда на связи!",
                         reply_markup=keyboard)


@dp.message_handler(Text(equals=["Продолжить", "2. Уровни проф развития сотрудников"]))
async def cmd_answer(message: types.Message):
    await block_8(message)


async def block_8(message: types.Message):
    await message.answer('И снова привет! В этом разделе тебя ждет информация об уровнях профессионального развития и '
                         'о том, чем отличаются сотрудники с разным уровнем. Также мы поговорим о том, '
                         'как диагностировать этот самый уровень. Начнем!', reply_markup=types.ReplyKeyboardRemove())
    await asyncio.sleep(4)
    await message.answer('КАРТИНКА: Уровень профессионального развития (УПР) – умение и желание сотрудника выполнить '
                         'поставленную перед ним задачу.')
    await asyncio.sleep(3)
    await message.answer('УПР зависит от сочетания 2-х факторов: компетентности и мотивации.')
    await asyncio.sleep(2)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Нет конечно!")
    keyboard.add("Да, если он старательный")
    await message.answer('Компетентность – знания и навыки,  которые нужны для выполнения конкретной задачи. Как '
                         'думаешь, сотрудник будет одинаково компетентен в решении всех задач?', reply_markup=keyboard)


@dp.message_handler(Text(equals="Нет конечно!"))
async def cmd_answer(message: types.Message):
    await message.answer("Согласен с тобой! смайл или гифка Класс", reply_markup=types.ReplyKeyboardRemove())
    await block_9(message)


@dp.message_handler(Text(equals="Да, если он старательный"))
async def cmd_answer(message: types.Message):
    await message.answer("Я подумаю об этом. Но похоже это что-то из области фантастики!",
                         reply_markup=types.ReplyKeyboardRemove())
    await block_9(message)


async def block_9(message: types.Message):
    await asyncio.sleep(2)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Конечно!")
    keyboard.add("Нет, я идеален!")
    await message.answer('Уровень компетентности всегда привязан к КОНКРЕТНОЙ задаче. То есть сотрудник может быть '
                         'профессионалом  в одной задаче и полным дилетантом в другой. Если ты сейчас обратишься к '
                         'своему опыту, то наверняка найдешь и те задачи,  в которых ты суперпрофи, и те, '
                         'в которых тебе есть, куда расти. Есть такое?', reply_markup=keyboard)


@dp.message_handler(Text(equals="Конечно!"))
async def cmd_answer(message: types.Message):
    await bot.send_animation(chat_id = message.chat.id, 
                            reply_markup = types.ReplyKeyboardRemove(), 
                             animation = open('media/like.gif', 'rb'))
    await block_10(message)


@dp.message_handler(Text(equals="Нет, я идеален!"))
async def cmd_answer(message: types.Message):
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
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Какие группы?")
    keyboard.add("Понятно")
    await message.answer('Сочетание компетентности и мотивации в разных пропорциях и составляют 4 уровня '
                         'профессионального развития. По каждой типовой задаче и по двум этим параметрам (уровень '
                         'мотивации и компетентности) всех сотрудников можно разбить на 4 неравные группы.',
                         reply_markup=keyboard)


@dp.message_handler(Text(equals=["Какие группы?", "Понятно"]))
async def cmd_answer(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Полезная картинка")
    keyboard.add("Ок, принято!")
    await message.answer(
        'В зависимости от уровня развития (Р – развитие) по отношению к конкретной задаче выделяют следующие типы сотрудников:\n'
        'Р1 (новичок) – высокая мотивация, низкая компетентность;\n'
        'Р2 (разуверившийся ученик) – низкая мотивация, низкая (или умеренная) компетентность;\n'
        'Р3 (специалист) – переменная мотивация, высокая компетентность;\n'
        'Р4 (профессионал) – высокая мотивация, высокая компетентность.', reply_markup=keyboard)


@dp.message_handler(Text(equals="Полезная картинка"))
async def cmd_answer(message: types.Message):
    await message.answer("Спасибо, что оценил мои старания!", reply_markup=types.ReplyKeyboardRemove())
    await asyncio.sleep(1)
    await block_11(message)


@dp.message_handler(Text(equals="Ок, принято!"))
async def cmd_answer(message: types.Message):
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
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Знакомо")
    keyboard.add("Понятно, дальше!")
    await message.answer("Если ты спросишь у сотрудников, кто готов выполнить конкретную задачу, то он (Р1) скорее "
                         "всего откликнется в первых рядах (и не очень важно, есть ли у него опыт и умения), скажет, "
                         "что ему надо очень мало времени, он быстро справится! А если ты уточнишь, как он будет "
                         "выполнять задачу, то ответит что-то типа “по ходу разберусь”.",
                         reply_markup=keyboard)


@dp.message_handler(Text(equals=["Знакомо", "Понятно, дальше!"]))
async def cmd_answer(message: types.Message):
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
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Да, много таких")
    keyboard.add("Меня такие люди не радуют")
    await message.answer("Если его попросить “взять” задачу, он нередко начинает торговаться в стиле “А что мне за "
                         "это будет?”, немного растягивать сроки (не так сильно, как Р2), но при этом сможет хорошо и "
                         "в деталях описать технологию выполнения задачи. Деталей будет много. А знаешь почему? "
                         "Потому что надо создать видимость, как много человеку нужно сделать.", reply_markup=keyboard)


@dp.message_handler(Text(equals=["Да, много таких", "Меня такие люди не радуют"]))
async def cmd_answer(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Не то слово!")
    keyboard.add("Побольше бы таких!")
    await message.answer("Профессионалы «Р4»  способны длительное время самостоятельно выполнять сложные задания. Как "
                         "правило, руководитель ощущает рядом с Р4 спокойную уверенность. Человек умеет и хочет. "
                         "Здорово, правда?", reply_markup=keyboard)


@dp.message_handler(Text(equals="Не то слово!"))
async def cmd_answer(message: types.Message):
    await message.answer("Вот и я так считаю", reply_markup=types.ReplyKeyboardRemove())
    await block_12(message)


@dp.message_handler(Text(equals="Побольше бы таких!"))
async def cmd_answer(message: types.Message):
    await message.answer("Да-а-а, мечта! Желаю тебе таких сотрудников!", reply_markup=types.ReplyKeyboardRemove())
    await block_12(message)


async def block_12(message: types.Message):
    await asyncio.sleep(2)
    await message.answer("Как его определить? На выполнение задачи берет оптимальные сроки, технологию выполнения, "
                         "если спросишь, описывает крупноблочно, при этом ты сразу поймешь, что он знает, "
                         "о чем говорит.")
    await asyncio.sleep(4)
    await message.answer("КАРТИНКА: Диагностика разных типов сотрудников\n"
                         "Спроси о сроках и способе выполнения – и ты услышишь…\n"
                         "Р1: ставит нереалистично короткие сроки, не может четко описать, как будет выполнять задачу, но уверен, что справится\n"
                         "Р2: отказывается от задачи, ставит непомерно большой срок выполнения, не знает, как будет выполнять\n"
                         "Р3: растягивает сроки, торгуется, очень точно и подробно описывает технологию выполнения\n"
                         "Р4: ставит оптимальный срок, описывает технологию выполнения в общих чертах.\n")
    await asyncio.sleep(6)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Да!")
    keyboard.add("Приведи пример")
    await message.answer("Все ли теперь по полочкам, все ли понятно?", reply_markup=keyboard)


@dp.message_handler(Text(equals="Да!"))
async def cmd_answer(message: types.Message):
    await message.answer("Я рад!", reply_markup=types.ReplyKeyboardRemove())
    await block_13(message)


@dp.message_handler(Text(equals="Приведи пример"))
async def cmd_answer(message: types.Message):
    await message.answer("С удовольствием!", reply_markup=types.ReplyKeyboardRemove())
    await block_13(message)


async def block_13(message: types.Message):
    await asyncio.sleep(1)
    await message.answer("Андрей очень хочет стать тимлидом, но при этом еще никогда не управлял людьми, проектами, "
                         "не читал ни одной книги по управлению. К какому типу его отнести? Это Р1, так как у него "
                         "много мотивации, но мало (нет) опыта.")
    await asyncio.sleep(5)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Р2")
    keyboard.add("Р3")
    await message.answer("Сергей по настоянию руководителя прошел пару тренингов, прочитал книгу “Мама, я тимлид”, "
                         "она ему не особенно зашла. Он как не хотел никем и ничем управлять, так и не хочет. Как "
                         "думаешь, какой тип?", reply_markup=keyboard)


@dp.message_handler(Text(equals=["Р2", "Р3"]))
async def cmd_answer(message: types.Message):
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
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("➡️ Да")
    keyboard.add("➡️ Позже пройду")
    await message.answer("Но знать не равно уметь!  Давай потренируемся определять типы сотрудников. У меня есть "
                         "короткий и нескучный тренажер на диагностику УПР,  надеюсь, что тебе понравится :) . "
                         "Готов?", reply_markup=keyboard)


@dp.message_handler(Text(equals="➡️ Да"))
async def cmd_answer(message: types.Message):
    await message.answer("Отлично!", reply_markup=types.ReplyKeyboardRemove())
    await block_14(message)


@dp.message_handler(Text(equals="➡️ Позже пройду"))
async def cmd_answer(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("➡️ Продолжить")
    await message.answer("Ок, как будешь готов, возвращайся, я на связи!", reply_markup=keyboard)


@dp.message_handler(Text(equals="➡️ Продолжить"))
async def cmd_answer(message: types.Message):
    await block_14(message)


async def block_14(message: types.Message):
    #await message.answer('ЗАДАНИЕ 1. (КАРТИНКА с Холмсом. Актер: Камбербэтч)', reply_markup=types.ReplyKeyboardRemove())
    await bot.send_photo(chat_id = message.chat.id, 
                         photo = open('media/sherlock.jpeg', 'rb'),
                         caption = 'ЗАДАНИЕ 1.')
    await asyncio.sleep(1)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("➡️ Р1")
    keyboard.add("➡️ Р2")
    keyboard.add("➡️ Р3")
    keyboard.add("➡️ Р4")
    await message.answer("Шерлок Холмс по отношению к дедуктивному методу решения задач. Какой тип?",
                         reply_markup=keyboard)


@dp.message_handler(Text(equals=["➡️ Р1", "➡️ Р2", "➡️ Р3"]))
async def cmd_answer(message: types.Message):
    await message.answer("Увы, нет. Холмс по отношению к этой задаче типичный Р4: умеет, может и хочет",
                         reply_markup=types.ReplyKeyboardRemove())
    await block_15(message)


@dp.message_handler(Text(equals="➡️ Р4"))
async def cmd_answer(message: types.Message):
    await message.answer("Верно! Он и прекрасно умеет, и хочет решать задачи с помощью этого метода.",
                         reply_markup=types.ReplyKeyboardRemove())
    await block_15(message)


async def block_15(message: types.Message):
    await bot.send_photo(chat_id = message.chat.id, photo = open('media/potter.jpeg', 'rb'), caption= 'ЗАДАНИЕ 2.')
    await asyncio.sleep(1)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("1️⃣ Р1")
    keyboard.add("2️⃣ Р2")
    keyboard.add("3️⃣ Р3")
    keyboard.add("4️⃣ Р4")
    await message.answer("Гарри Поттер по отношению к борьбе с темными силами в 1 книге (фильме)",
                         reply_markup=keyboard)


@dp.message_handler(Text(equals=["2️⃣ Р2", "3️⃣ Р3", "4️⃣ Р4"]))
async def cmd_answer(message: types.Message):
    await message.answer(
        "Не соглашусь! Должной компетенцией Гарри еще точно не обладал, но при этом хотел бороться с темными силами. Он Р1.",
        reply_markup=types.ReplyKeyboardRemove())
    await block_16(message)


@dp.message_handler(Text(equals="1️⃣ Р1"))
async def cmd_answer(message: types.Message):
    await message.answer(
        "Я тоже так считаю. Должной компетенцией Гарри еще точно не обладал, но при этом хотел бороться с темными силами.",
        reply_markup=types.ReplyKeyboardRemove())
    await block_16(message)


async def block_16(message: types.Message):
    await bot.send_photo(chat_id = message.chat.id, 
                         photo = open('media/houseMD.jpeg', 'rb'),
                         caption = 'ЗАДАНИЕ 3.')
    await asyncio.sleep(1)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("▶️ Р1")
    keyboard.add("▶️ Р2")
    keyboard.add("▶️ Р3")
    keyboard.add("▶️ Р4")
    await message.answer("Доктор Хаус по отношению к общению с пациентами по сбору анамнеза",
                         reply_markup=keyboard)


@dp.message_handler(Text(equals=["▶️ Р1", "▶️ Р2", "4️⃣ Р4"]))
async def cmd_answer(message: types.Message):
    await message.answer(
        "Неверно, потому что умения у него явно есть и при этом никакого желания.",
        reply_markup=types.ReplyKeyboardRemove())
    await block_17(message)


@dp.message_handler(Text(equals="▶️ Р3"))
async def cmd_answer(message: types.Message):
    await message.answer(
        "Да, он точно это умеет, но совершенно не горит желанием и всячески избегает.",
        reply_markup=types.ReplyKeyboardRemove())
    await block_17(message)


async def block_17(message: types.Message):
    await bot.send_photo(chat_id = message.chat.id, 
                         photo = open('media/aria.jpeg', 'rb'),
                         caption = 'ЗАДАНИЕ 4.')
    await asyncio.sleep(1)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("⏺ Р1")
    keyboard.add("⏺ Р2")
    keyboard.add("⏺ Р3")
    keyboard.add("⏺️ Р4")
    await message.answer("Арья по отношению к соблюдению правил этикета",
                         reply_markup=keyboard)


@dp.message_handler(Text(equals=["⏺ Р1", "⏺ Р3", "⏺️ Р4"]))
async def cmd_answer(message: types.Message):
    await message.answer(
        "Не соглашусь! Она типичный Р2: совершенно не испытывала радости от необходимости соблюдать правила этикета и не особенно стремилась их освоить",
        reply_markup=types.ReplyKeyboardRemove())
    await block_18(message)


@dp.message_handler(Text(equals="⏺ Р2"))
async def cmd_answer(message: types.Message):
    await message.answer(
        "Да, согласен! Она совершенно не испытывала радости от необходимости соблюдать правила этикета и не особенно стремилась их освоить.",
        reply_markup=types.ReplyKeyboardRemove())
    await block_18(message)


async def block_18(message: types.Message):
    await bot.send_photo(chat_id = message.chat.id, 
                         photo = open('media/neznaika.jpeg', 'rb'),
                         caption = 'ЗАДАНИЕ 5.')
    await asyncio.sleep(1)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("⏹ Р1")
    keyboard.add("⏹ Р2")
    keyboard.add("⏹ Р3")
    keyboard.add("⏹ Р4")
    await message.answer("К какому типу относится Незнайка, который писал стихи?",
                         reply_markup=keyboard)


@dp.message_handler(Text(equals=["⏹ Р1", "⏹ Р3", "⏹ Р4"]))
async def cmd_answer(message: types.Message):
    await message.answer(
        "Не думаю! Скорее он Р2:  у него и не получалось, и он не горел желанием это делать.",
        reply_markup=types.ReplyKeyboardRemove())
    await block_19(message)


@dp.message_handler(Text(equals="⏹️ Р2"))
async def cmd_answer(message: types.Message):
    await message.answer(
        "В точку! У него и не получалось, и он не горел желанием это делать.",
        reply_markup=types.ReplyKeyboardRemove())
    await block_19(message)


async def block_19(message: types.Message):
    await asyncio.sleep(2)
    await message.answer('Супер! Ты большой молодец, потренировался на примере известных персонажей определять уровни '
                         'профессионального развития и заодно почти закончил еще один раздел. У тебя … верных ответов'
                         ' из 5 возможных.')
    await asyncio.sleep(7)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("➡️ Да!")
    keyboard.add("➡️ Не хочется, в другой раз")
    await message.answer("Прежде, чем ты пойдешь дальше, предлагаю тебе решить парочку проверочных кейсов и закрепить знания.",
                         reply_markup=keyboard)


@dp.message_handler(Text(equals="➡️ Да!"))
async def cmd_answer(message: types.Message):
    await message.answer(
        "Замечательно. Это не займет больше 3-5 минут.",
        reply_markup=types.ReplyKeyboardRemove())
    await block_20(message)


@dp.message_handler(Text(equals="➡️ Не хочется, в другой раз"))
async def cmd_answer(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Готов продолжить!")
    await message.answer("Хорошо, тогда жду тебя, до связи!",
                         reply_markup=keyboard)


@dp.message_handler(Text(equals="Готов продолжить!"))
async def cmd_answer(message: types.Message):
    await block_20(message)


async def block_20(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
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


@dp.message_handler(Text(equals=["🅿️1️⃣", "🅿️3️⃣", "🅿️4️⃣"]))
async def cmd_answer(message: types.Message):
    await message.answer(
        "Не соглашусь! У Александра много ошибок, и он пал духом, что свидетельствует о неуверенности в себе и снижении мотивации",
        reply_markup=types.ReplyKeyboardRemove())
    await block_21(message)


@dp.message_handler(Text(equals="🅿️2️⃣"))
async def cmd_answer(message: types.Message):
    await message.answer(
        "Абсолютно точно! У Александра много ошибок, и он пал духом, что свидетельствует о неуверенности в себе и снижении мотивации. ",
        reply_markup=types.ReplyKeyboardRemove())
    await block_21(message)


async def block_21(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("🅿1")
    keyboard.add("🅿2")
    keyboard.add("🅿3")
    keyboard.add("🅿4")
    await message.answer("Вопрос 2. Если на твой вопрос, сколько тебе понадобится времени на реализацию задачи, "
                         "сотрудник отвечает срок, который сильно короче, чем тот, который действительно нужен на ее "
                         "выполнение, то он скорее всего кто по уровню профессионального развития в этой задаче?",
                         reply_markup=keyboard)


@dp.message_handler(Text(equals=["🅿2", "🅿3", "🅿4"]))
async def cmd_answer(message: types.Message):
    await message.answer(
        "Неверно! Это характерно для новичка в задаче – Р1. Именно они просят на выполнение нереалистично короткие "
        "сроки, потому что в вопросе не разбираются, а энтузиазма, желания проявить себя и мотивации у них много",
        reply_markup=types.ReplyKeyboardRemove())
    await block_22(message)


@dp.message_handler(Text(equals="🅿1"))
async def cmd_answer(message: types.Message):
    await message.answer(
        "Верно! Именно новички в задачи просят на ее выполнение нереалистично короткие сроки, потому что в вопросе не "
        "разбираются, а энтузиазма, желания проявить себя и мотивации у них много",
        reply_markup=types.ReplyKeyboardRemove())
    await block_22(message)


async def block_22(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("P1️⃣")
    keyboard.add("P2️⃣")
    keyboard.add("P3️⃣")
    keyboard.add("P4️⃣")
    await message.answer("Вопрос 3. Ольга, опытный сотрудник отдела, получила новое для неё задание. Выполняет работу "
                         "с энтузиазмом, хотя испытывает серьёзные трудности и показывает низкие результаты. "
                         "Руководителю важно, чтобы Ольга справилась с заданием. Какой уровень профессионального "
                         "развития у Ольги?",
                         reply_markup=keyboard)


@dp.message_handler(Text(equals=["P2️⃣", "P3️⃣", "P4️⃣"]))
async def cmd_answer(message: types.Message):
    await message.answer(
        "Не могу согласиться! У Ольги низкая компетентность, так как задние новое даже для опытного сотрудника, "
        "высокая мотивация – выполняет работу с энтузиазмом. Значит, она Р1. ",
        reply_markup=types.ReplyKeyboardRemove())
    await block_23(message)


@dp.message_handler(Text(equals="P1️⃣"))
async def cmd_answer(message: types.Message):
    await message.answer(
        "В точку! Низкая компетентность, так как задние новое даже для опытного сотрудника, высокая мотивация – "
        "выполняет работу с энтузиазмом.",
        reply_markup=types.ReplyKeyboardRemove())
    await block_23(message)


async def block_23(message: types.Message):
    await asyncio.sleep(4)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("1")
    keyboard.add("2")
    keyboard.add("3")
    keyboard.add("4")
    keyboard.add("5")
    await bot.send_sticker(chat_id = message.chat.id, sticker = 'CAACAgIAAxkBAAID22KNHELIQv32URs_wMjahYdBbfDxAAI4EQACe2KYScU9o5OriGzxJAQ')
    await message.answer("Поздравляю с завершением второго блока! Как тебе? Оцени от 0 до 5",
                         reply_markup=keyboard)


@dp.message_handler(Text(equals=["1", "2", "3", "4", "5"]))
async def cmd_answer(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Да, продолжу!")
    keyboard.add("Чуть позже")
    await message.answer(
        "Спасибо за обратную связь! Если осталось желание потренироваться и закрепить изученное, то ты всегда можешь "
        "вернуться и перечитать теорию, потренироваться на кейсах. Готов идти в следующий раздел?",
        reply_markup=keyboard)


@dp.message_handler(Text(equals="Да, продолжу!"))
async def cmd_answer(message: types.Message):
    await message.answer("Отлично!", reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(Text(equals="Чуть позже"))
async def cmd_answer(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Готов!")
    await message.answer("Договорились, я на связи и жду, когда ты вернешься.", reply_markup=keyboard)


#3й раздел
@dp.message_handler(Text(equals="3. Стили руководства"))
async def third_chapter_answer_1(message: types.Message):

    await asyncio.sleep(2)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_video(chat_id = message.chat.idmessage.chat.id, video = "https://ok.ru/video/200996426023" )
    keyboard.add("Oтлично!")
    keyboard.add("Сойдет")
    keyboard.add("Хуже некуда")

    await message.answer("Вот мы и снова вместе!" 
                         "Приветствую тебя в 3 разделе. Тут мы поговорим о стилях руководства (управления). Как настроение?", 
                         reply_markup=keyboard)

@dp.message_handler(Text(equals=["Хуже некуда", "Oтлично!", "Сойдет"]))
async def third_chapter_answer_2(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    await asyncio.sleep(1)
    if (message.text == "Хуже некуда"):
        keyboard.add("Готов!")
        await message.answer("Договорились, я на связи и жду, когда ты вернешься.", reply_markup=keyboard)
    elif (message.text == "Oтлично!"):
        await message.answer("Вот и хорошо, тогда приступим.", reply_markup=keyboard)
        await third_chapter_block_1(message)
    else :
        await message.answer("Надеюсь, что в процессе настроение улучшится.", reply_markup=keyboard)
        await third_chapter_block_1(message)



async def third_chapter_block_1(message: types.Message):
    await message.answer("Ты уже знаешь, что есть 4 типа сотрудников по отношению к задаче и научился их диагностировать."
                         "С каждым таким сотрудником важно взаимодействовать по-разному."
                         , reply_markup=types.ReplyKeyboardRemove())
    await asyncio.sleep(3)
    await message.answer("Стили складываются из комплекса действий руководителя. "
                         "Каких именно? Инструктирующих и мотивирующих (или вовлекающих). ")
    await asyncio.sleep(3)
    await message.answer("КАРТИНКА"
                        "Инструктирующие действия — это постановка задач, разъяснение сотруднику, что, "
                        "к какому сроку и как делать, обозначение точек контроля.")
    await asyncio.sleep(2)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Однозначно!")
    keyboard.add("Хотелось бы пример.")
    await message.answer("Все ли тебе понятно?", reply_markup=keyboard)



@dp.message_handler(Text(equals=["Однозначно!", "Хотелось бы пример."]))
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
    await message.answer("КАРТИНКА "
                         "Мотивирующие действия — стимулы, которые вовлекают сотрудника в процесс работы, повышают его желание "
                         "работать и уверенность в собственных силах.")

    await asyncio.sleep(3)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Нет, все ясно!")
    keyboard.add("Кoнечно!")


    await message.answer("Привести пример?", reply_markup=keyboard)


@dp.message_handler(Text(equals=["Нет, все ясно!", "Кoнечно!"]))
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
    await asyncio.sleep(1)
    await message.answer("Давай я задам тебе несколько вопросов, чтобы ты закрепил понимание, где инструктирующие, "
                         "а где мотивирующие действия. "
                         , reply_markup=types.ReplyKeyboardRemove())
    
    await asyncio.sleep(2)

    await message.answer("Итак, задание очень простое. Прочитай описание действия руководителя и определи, "
                         "это инструктирование или  мотивирование?")
    await asyncio.sleep(2)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Мотивирующее")
    keyboard.add("Инстрyктирующее")

    await message.answer("1. Руководитель похвалил сотрудника за качественно выполненную работу." 
                        "Это мотивирующее или инcтруктирующее действие? ", reply_markup=keyboard)

@dp.message_handler(Text(equals=["Мотивирующее", "Инстрyктирующее"]))
async def third_chapter_answer_5(message: types.Message):
    await asyncio.sleep(1)
    if (message.text == "Мотивирующее"):
        await message.answer("Верно!", reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer("Мимо:( Это про мотивирование", reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(2)
    await third_chapter_block_4(message)


async def third_chapter_block_4(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Мoтивирующее")
    keyboard.add("Инструктирующeе")
    await message.answer("2. Руководитель подробно рассказал, почему эта задача интересная и перспективная для сотрудника.",
                        reply_markup=keyboard)



@dp.message_handler(Text(equals=["Мoтивирующее","Инструктирующeе"]))
async def third_chapter_answer_6(message: types.Message):
    await asyncio.sleep(1)
    if(message.text == "Мoтивирующее"):
        await message.answer("В точку!", reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer("Увы, нет, это мотивирование", reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(2)
    await third_chapter_block_5(message)

async def third_chapter_block_5(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Mотивирующее")
    keyboard.add("Инструктирующеe")
    await message.answer("3. Руководитель прислал подробное описание того, что нужно сделать. ",
                        reply_markup=keyboard)

@dp.message_handler(Text(equals=["Mотивирующее", "Инструктирующеe"]))
async def third_chapter_answer_7(message: types.Message):
    await asyncio.sleep(1)
    if(message.text == "Mотивирующее"):
        await message.answer("Увы, нет", reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer("Да, согласен!", reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(2)
    await third_chapter_block_6(message)

async def third_chapter_block_6(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Мотивирующeе")
    keyboard.add("Инструктирyющее")
    await message.answer("4. Руководитель поинтересовался мнением сотрудника, какую технологию лучше выбрать для выполнения этой задачи. ",
                        reply_markup=keyboard)

@dp.message_handler(Text(equals=["Мотивирующeе", "Инструктирyющее"]))
async def third_chapter_answer_8(message: types.Message):
    await asyncio.sleep(1)
    if(message.text == "Мотивирующeе"):
        await message.answer("Однозначно!", reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer("Нет, это мотивационное действие", reply_markup=types.ReplyKeyboardRemove())
    
    await asyncio.sleep(2)
    await third_chapter_block_7(message)


async def third_chapter_block_7(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Мотивирующеe")
    keyboard.add("Инструктирующee")
    await message.answer("5. Руководитель на личном примере показал, как выполнить задачу. ",
                        reply_markup=keyboard)

@dp.message_handler(Text(equals=["Мотивирующеe", "Инструктирующee"]))
async def third_chapter_answer_9(message: types.Message):
    await asyncio.sleep(1)
    if(message.text == "Мотивирующеe"):
        await message.answer("Увы, нет.", reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer("Точно!", reply_markup=types.ReplyKeyboardRemove())
    await asyncio.sleep(2)
    await third_chapter_block_8(message)


async def third_chapter_block_8(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Мотивирующee")
    keyboard.add("Инструктирующее")
    await message.answer("6. Руководитель обозначил критерии достижения результата ",
                        reply_markup=keyboard)

@dp.message_handler(Text(equals=["Мотивирующee", "Инструктирующее"]))
async def third_chapter_answer_10(message: types.Message):
    await asyncio.sleep(1)
    if(message.text == "Мотивирующee"):
        await message.answer("Нет, это инструктирующее действие", reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer("Ты абсолютно прав!", reply_markup=types.ReplyKeyboardRemove())
    await asyncio.sleep(2)
    await third_chapter_block_9(message)

async def third_chapter_block_9(message: types.Message):
    await message.answer("Отлично! Ты выполнил все 6 заданий и у тебя … правильных ответов из 6. "
                         , reply_markup=types.ReplyKeyboardRemove())
    
    await asyncio.sleep(2)

    await message.answer("Хочу подарить тебе шпаргалку с описанием мотивирующих и инструктирующих действий. " 
                         "Ты можешь сохранить картинки в галерею телефона и по необходимости обращаться к ним. ")
    await asyncio.sleep(2)

    await message.answer("КАРТИНКА "
                         "Основные инструктирующие действия "
                         "  1.     Постановка целей и задач."
                         "  2.     Определение критериев достижения результата."
                         "  3.     Знакомство с должностной инструкцией (вводный инструктаж)."
                         "  4.     Навигация на рабочем месте (разметка)."
                         "  5.     Стандарты деятельности, критерии качества."
                         "  6.     Рекомендация, совет."
                         "  7.    Планирование работы, график выполнения задания."
                         "  8.    Определение ресурсов."
                         "  9.    Нормирование деятельности, установление сроков."
                         " 10.   Разграничение ответственности, определение границ полномочий."
                         " 11.   Указание / распоряжение. ")

    await asyncio.sleep(6)

    await message.answer("КАРТИНКА "
                         "Основные мотивирующие действия "
                         "  1.     Похвала за прогресс."
                         "  2.     Поощрение, награда."
                         "  3.     Благодарность, публичное признание заслуги."
                         "  4.     Демонстрация ценности сотрудника в глазах его близких."
                         "  5.     Выслушивание проблем."
                         "  6.     Личностная поддержка."
                         "  7.     Помощь (предложение помощи)."
                         "  8.     Повышение самооценки."
                         "  9.     Интересоваться мнением сотрудника."
                         "  10.    Участие сотрудника в постановке целей, принятии решения, формулировании задания."
                         "  11.    Содействие в продвижении решений и инициатив."
                         "  12.    Поощрение инициативы."
                         "  13.    Возможность попробовать, разрешение риска."
                         "  14.    «Разбор полетов», консультация."
                         "  15.    Сделать наставником новичка.")

    await asyncio.sleep(6)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Конечно, легко")
    keyboard.add("Пока не очень")

    await message.answer("Теперь я уверен, что ты знаешь и умеешь различать мотивирующие и инструктирующие действия. "
                         "Да?", reply_markup=keyboard)

@dp.message_handler(Text(equals=["Конечно, легко", "Пока не очень"]))
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

    await message.answer("КАРТИНКА "
                         "ИНСТРУКТИРУЮЩИЙ СТИЛЬ (С1) предполагает много инструктирующих и мало вовлекающих действий. "
                         "НАСТАВНИЧЕСКИЙ СТИЛЬ (С2) предполагает много инструктирующих действий и много вовлекающих. "
                         "Руководитель решает задачу вместе с сотрудником.")

    await asyncio.sleep(4)

    await message.answer("КАРТИНКА "
                        "ВОВЛЕКАЮЩИЙ СТИЛЬ  (С3) предполагает мало инструктирующих и много вовлекающих действий. "
                        "Руководитель мотивирует подчинённого к решению задачи, вовлекая его в принятие решений. "      
                        "ДЕЛЕГИРУЮЩИЙ СТИЛЬ  (С4): мало как инструктирующих, так и вовлекающих действий. "
                        "Руководитель делегирует подчиненному ответственность за принятие решений и достижение результатов. ")

    await asyncio.sleep(6)

    await message.answer("КАРТИНКА с 4 стилями * дополнительно запросить у Инны*")

    await asyncio.sleep(3)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Инстрyктирующий")
    keyboard.add("Нaставнический")
    keyboard.add("Вoвлекающий")
    keyboard.add("Дeлегирующий")
    keyboard.add("Всe понемногу")

    await message.answer("Что ж, теперь ты знаешь про 4 стиля управления. Как думаешь, а какой применять лучше всего? ", 
                        reply_markup=keyboard)

@dp.message_handler(Text(equals=["Инстрyктирующий", "Нaставнический", "Вoвлекающий", "Дeлегирующий", "Всe понемногу"]))
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
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("От настроения")
    keyboard.add("От характера руководителя")
    keyboard.add("От уровня профессионального развития сотрудника")

    await message.answer("Руководителю очень важно применять все эти стили. Как думаешь, от чего это зависит? "
                         , reply_markup=keyboard)


@dp.message_handler(Text(equals=["От настроения", "От характера руководителя", "От уровня профессионального развития сотрудника"]))
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

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Дa!")
    keyboard.add("Не совсем")

    await message.answer("Сложилась ли картинка, все ли тебе понятно? ", reply_markup=keyboard)

@dp.message_handler(Text(equals=["Дa!", "Не совсем"]))
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

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Кoнечно")
    keyboard.add("Не сейчас")

    await message.answer("Давай закрепим понимание стилей на видеопримерах. "
                         "Твоя задача будет посмотреть фрагмент  и определить, какой стиль управления применяет руководитель. "
                         "Ты готов?  ", reply_markup=keyboard)

@dp.message_handler(Text(equals=["Кoнечно", "Не сейчас"]))
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
    # Итак, первое видео. 
    # Видео 1.
    # https://ok.ru/video/200996426023
    

    await asyncio.sleep(2)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Инструктирyющий")
    keyboard.add("Настaвнический")
    keyboard.add("Вовлeкающий")
    keyboard.add("Делегирyющий")

    await message.answer("Какой это стиль? ", reply_markup=keyboard)

@dp.message_handler(Text(equals=["Инструктирyющий", "Настaвнический", "Вовлeкающий","Делегирyющий"]))
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

    await asyncio.sleep(2)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Инcтруктирующий")
    keyboard.add("Наcтавнический")
    keyboard.add("Вoвлeкающий")
    keyboard.add("Дeлeгирующий")

    await message.answer("Какой это стиль? ", reply_markup=keyboard)

@dp.message_handler(Text(equals=["Инcтруктирующий", "Наcтавнический", "Вoвлeкающий","Дeлeгирующий"]))
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

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Инструктирующий")
    keyboard.add("Наставнический")
    keyboard.add("Вовлекающий")
    keyboard.add("Делегирующий")

    await message.answer("Какой это стиль? ", reply_markup=keyboard)

@dp.message_handler(Text(equals=["Инструктирующий", "Наставнический", "Вовлекающий","Делегирующий"]))
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

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Все отлично!")
    keyboard.add("Я запутался.")

    await message.answer("Какой это стиль? ", reply_markup=keyboard)

@dp.message_handler(Text(equals=["Все отлично!", "Я запутался."]))
async def third_chapter_answer_19(message: types.Message):
    await asyncio.sleep(1)

    await message.answer("Спасибо за обратную связь! Если осталось желание потренироваться и закрепить изученное, то "
                         "ты всегда можешь вернуться и перечитать теорию, потренироваться на кейсах. ", reply_markup=types.ReplyKeyboardRemove())

if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
