#!/usr/bin/python3

import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, KeyboardButton
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
    CallbackQueryHandler,
)
import psycopg2
import datetime
from datetime import datetime

conn = psycopg2.connect(database="cot", user="postgres", password="postgres", host="127.0.0.1", port="5432")
print("Opened database successfully")
cur = conn.cursor()
today = datetime.now()
# Enable logging
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
# logger = logging.getLogger(__name__)
BIO, BIO_BUTTON, BLOCK_1_BUTTON = range(3)


def start (update: Update, context: CallbackContext) -> range:
    update.message.reply_text(
        'Здравствуйте! Пожалуйста напишите, как Вас зовут?'
    )

    return BIO


def bio(update: Update, context: CallbackContext) -> range:
    """Stores the info about the user and ends the conversation."""
    user = update.message.from_user
    #    name = update.message.text
    #    logger.info("Bio of %s: %s", user.first_name, update.message.text)

    postgres_insert_query = """INSERT INTO clients (ID, NAME, POSITION, REG_DATE) VALUES (%s,%s,%s,%s) ON CONFLICT DO NOTHING"""
    record_to_insert = (user.id, update.message.text, 0, today)
    cur.execute(postgres_insert_query, record_to_insert)

    conn.commit()

    update.message.reply_text('Большое спасибо! Приятно познакомиться, {0}!'.format(update.message.text))

    keyboard = [
        [
            InlineKeyboardButton("Не удивил", callback_data='serious'),
            InlineKeyboardButton("Да, супер", callback_data='not_serious'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        'Меня зовут ИнноБот, я умный и веселый, а еще я много знаю про управление и очень хочу поделиться с тобой! Знаешь в чем моя суперсила? В том, что я на связи 24/7 и ты можешь поболтать со мной в любое время дня и ночи, когда будет свободная минутка! Правда, здорово?',
        reply_markup=reply_markup)

    return BIO_BUTTON

def bio_button(update: Update, context: CallbackContext) -> range:
    query = update.callback_query
    variant = query.data

    query.answer()
    if variant == 'serious':
        query.edit_message_text(text=f"А ты серьезный человек, уверен, что мы найдём общий язык:-)")
    else:
        query.edit_message_text(text=f"Я рад что ты оценил:-)", )

    keyboard = [
        [
            InlineKeyboardButton("Готов на все 100!", callback_data='left'),
            InlineKeyboardButton("Давай попробуем", callback_data='right'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Планирую рассказать тебе о том что такое ситуационное управление сотрудниками. Как ты на это смотришь, готов начать?",
        reply_markup=reply_markup
    )

    return BLOCK_1_BUTTON

def block_1_button(update: Update, context: CallbackContext) -> range:
    query = update.callback_query
    variant = query.data

    query.answer()
    if variant == 'left':
        query.edit_message_text(text=f"Отлично, с таким настроем мы с тобой быстро во всем разберемся:-)")
    else:
        query.edit_message_text(text=f"Сделаю все возможное, чтобы тебе понравилось и было полезно! Поехали!")

    keyboard = [
        InlineKeyboardButton("1. Управление. Причины невыполнения задач", callback_data='1'),
        InlineKeyboardButton("2. Уровни проф развития сотрудников", callback_data='2'),
        InlineKeyboardButton("3. Стили руководства", callback_data='3'),
        InlineKeyboardButton("4. Особенности управления разными типами сотрудников", callback_data='4'),
        InlineKeyboardButton("5. Общее тестирование", callback_data='5')
    ]

    reply_markup = InlineKeyboardMarkup(inline_keyboard=[], resize_keyboard=True).from_column(button_column=keyboard)

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Я рекомендую тебе открывать темы последовательно в этом порядке:",
        reply_markup=reply_markup
    )

    return ConversationHandler.END

def cancel(update: Update, context: CallbackContext) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text(
        'Bye! I hope we can talk again some day.', reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


def main() -> None:
    """Run the bot. t.me/test_innotechbot"""
    updater = Updater("5158951780:AAHl7Zt7vhaSUsYuIJCrtLvvSdZCiwY5RWA")
    dispatcher = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            BIO: [MessageHandler(Filters.text & ~Filters.command, bio)],
            BIO_BUTTON: [CallbackQueryHandler(bio_button)],
            BLOCK_1_BUTTON: [CallbackQueryHandler(block_1_button)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
