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

class Progress1(StatesGroup):
    msg_1 = State()
    msg_2 = State()
    msg_3 = State()
    msg_4 = State()
    msg_5 = State()
    msg_6 = State()
    msg_7 = State()
    msg_8 = State()

def register_handlers_chapter1(dp: Dispatcher):
    dp.register_message_handler(block2, Text(equals="1. Управление. Причины невыполнения задач"))
    
    dp.register_message_handler(answer1, Text(equals="Не мог"), state=Progress1.msg_1)
    dp.register_message_handler(answer2, Text(equals="Не хотел"), state=Progress1.msg_1)
    dp.register_message_handler(answer3, Text(equals="То и другое"), state=Progress1.msg_1)

    dp.register_message_handler(answer4, Text(equals="Причем тут я?"), state=Progress1.msg_2)
    dp.register_message_handler(answer5, Text(equals="Понятное дело"), state=Progress1.msg_2)

    dp.register_message_handler(answer6, Text(equals=["Постановка целей и задач", "Планирование", "Контроль", "Мотивирование", "Обучение и развитие сотрудников"]), state=Progress1.msg_3)

    dp.register_message_handler(answer7, Text(equals="➡️ Специалист"), state=Progress1.msg_4)
    dp.register_message_handler(answer8, Text(equals="➡️ Руководитель"), state=Progress1.msg_4)

    dp.register_message_handler(answer9, Text(equals="➡️ Планирование"), state=Progress1.msg_5)
    dp.register_message_handler(answer10, Text(equals="➡️ Обучение"), state=Progress1.msg_5)
    dp.register_message_handler(answer11, Text(equals="➡️ Мотивирование"), state=Progress1.msg_5)

    dp.register_message_handler(answer12, Text(equals="➡️ Контроль"), state=Progress1.msg_6)
    dp.register_message_handler(answer13, Text(equals="➡️ Постановка целей"), state=Progress1.msg_6)
    dp.register_message_handler(answer14, Text(equals="➡️ Oбучение"), state=Progress1.msg_6)

    dp.register_message_handler(answer15, Text(equals="Да"), state=Progress1.msg_7)
    dp.register_message_handler(answer16, Text(equals="Вернусь позже"), state=Progress1.msg_7)

    dp.register_message_handler(answer17, Text(equals="Продолжить"), state=Progress1.msg_8)

async def block2(message: types.Message):
    Log().getLogger().info("Chapter 1")
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
    await Progress1.msg_1.set()

async def answer1(message: types.Message):
    await message.answer("Верно, но не только, на самом деле сотрудник мог и не хотеть, и не понять, что делать. Всего "
                         "можно выделить 4 причины", reply_markup=types.ReplyKeyboardRemove())
    await block_3(message)

async def answer2(message: types.Message):
    await message.answer("Ты прав! Но это еще не все. Сотрудник мог не понять, что делать, не иметь ресурсов и так "
                         "далее. Всего можно выделить 4 причины", reply_markup=types.ReplyKeyboardRemove())
    await block_3(message)

async def answer3(message: types.Message):
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
    await Progress1.msg_2.set()

async def answer4(message: types.Message):
    await message.answer("А при том, что значит, какая-то из управленческих функций не была реализована тобой",
                         reply_markup=types.ReplyKeyboardRemove())
    await block_4(message)

async def answer5(message: types.Message):
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
    await message.answer('Ну что ж, теперь ты знаешь, какие есть функции у руководителя и какой функции нужно уделить '
                         'больше внимания, если сотрудник не выполняет задачу')
    await asyncio.sleep(3)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Постановка целей и задач")
    keyboard.add("Планирование")
    keyboard.add("Контроль")
    keyboard.add("Мотивирование")
    keyboard.add("Обучение и развитие сотрудников")
    await message.answer('Хочу спросить у тебя, как ты думаешь, какую функцию необходимо прокачать именно тебе?',
                         reply_markup=keyboard)
    await Progress1.msg_3.set()

async def answer6(message: types.Message):
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
    counter.set_counter(0)
    await Progress1.msg_4.set()

async def answer7(message: types.Message):
    await message.answer("Не согласен с тобой! В данном случае он проводил мотивационную беседу, а значит, "
                         "работал как руководитель",
                         reply_markup=types.ReplyKeyboardRemove())
    await block_5(message)

async def answer8(message: types.Message):
    counter.increase_counter()
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
    await Progress1.msg_5.set()

async def answer9(message: types.Message):
    counter.increase_counter()
    await message.answer("Верно! Выбирая, кому поручить задачу, нужно всегда анализировать, у кого есть время, "
                         "силы и другие ресурсы для её выполнения, то есть планировать",
                         reply_markup=types.ReplyKeyboardRemove())
    await block_6(message)

async def answer10(message: types.Message):
    await message.answer("Не соглашусь! Выбирая, кому поручить задачу, нужно всегда анализировать, у кого есть время, "
                         "силы и другие ресурсы для её выполнения, то есть планировать",
                         reply_markup=types.ReplyKeyboardRemove())
    await block_6(message)

async def answer11(message: types.Message):
    await message.answer("Увы нет. Выбирая, кому поручить задачу, нужно всегда анализировать, у кого есть время, "
                         "силы и другие ресурсы для её выполнения, то есть планировать",
                         reply_markup=types.ReplyKeyboardRemove())
    await block_6(message)

async def block_6(message: types.Message):
    await asyncio.sleep(2)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("➡️ Контроль")
    keyboard.add("➡️ Постановка целей")
    keyboard.add("➡️ Oбучение")
    await message.answer('Вопрос 3\n'
                         'Сотрудник не понял, что именно нужно делать. Какая функция в данном случае "хромает" у '
                         'руководителя?', reply_markup=keyboard)
    await Progress1.msg_6.set()

async def answer12(message: types.Message):
    await message.answer("Неверно!",
                         reply_markup=types.ReplyKeyboardRemove())
    await block_7(message)

async def answer13(message: types.Message):
    counter.increase_counter()
    await message.answer("Именно так!",
                         reply_markup=types.ReplyKeyboardRemove())
    await block_7(message)

async def answer14(message: types.Message):
    await message.answer("Не совсем!",
                         reply_markup=types.ReplyKeyboardRemove())
    await block_7(message)

async def block_7(message: types.Message):
    correct_answers = counter.get_counter()
    if correct_answers == 0:
        word = 'правильных ответов'
    elif correct_answers == 1:
        word = 'правильный ответ'
    else:
        word = 'правильных ответа'
    Log().getLogger().info("{0} {1} из 3".format(correct_answers, word))
    await message.answer('Чтобы сотрудник понимал, что ему делать и четко видел образ конечного результата, '
                         'руководителю нужно грамотно ставить цели')
    await asyncio.sleep(2)
    await message.answer("Спасибо что ответил на все вопросы! И у тебя {0} {1} из 3".format(correct_answers, word))
    await asyncio.sleep(2)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Да")
    keyboard.add("Вернусь позже")
    await Progress1.msg_7.set()
    await message.answer('Готов перейти к следующему блоку, в котором мы поговорим об уровнях профессионального '
                         'развития сотрудников?', reply_markup=keyboard)
    
async def answer16(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Продолжить")
    await Progress1.msg_8.set()
    await message.answer("Хорошо, возвращайся, я всегда на связи!",
                         reply_markup=keyboard)

async def answer15(message: types.Message, state: FSMContext):
    await message.answer("Отлично, продолжаем!",
                         reply_markup=types.ReplyKeyboardRemove())
    await state.finish()
    from messages.chapter2 import block_8
    await block_8(message)
    
async def answer17(message: types.Message, state: FSMContext):
    await state.finish()
    from messages.chapter2 import block_8
    await block_8(message)
