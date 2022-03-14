#!/usr/bin/python3

import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
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
conn = psycopg2.connect(database = "здесь имя БД", user = "здесь имя пользователя БД", password = "здесь пароль от БД", host = "127.0.0.1", port = "5432")
print ("Opened database successfully")
cur = conn.cursor()
#today = date.today()
today = datetime.now()
# Enable logging
#logging.basicConfig(
#    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
#)
#logger = logging.getLogger(__name__)
BIO = range(4)


def start (update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        'Здравствуйте! Пожалуйста напишите, как Вас зовут?'
    )

    return  BIO

def bio (update: Update, context: CallbackContext) -> int:
    """Stores the info about the user and ends the conversation."""
    user = update.message.from_user
#    name = update.message.text
#    logger.info("Bio of %s: %s", user.first_name, update.message.text)

    postgres_insert_query = """ INSERT INTO clients (ID, NAME, POSITION, REG_DATE) VALUES (%s,%s,%s, %s) ON CONFLICT DO NOTHING"""
    record_to_insert = (user.id, update.message.text, 0, today)
    cur.execute(postgres_insert_query, record_to_insert)

    conn.commit()
    conn.close()

    update.message.reply_text('Большое спасибо! Приятно познакомиться!')
    keyboard = [
        [
            InlineKeyboardButton("Обучение", callback_data='learning'),
            InlineKeyboardButton("Тестирование", callback_data='testing'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Здравствуйте! Пожалуйста, выберите:', reply_markup=reply_markup)

    return ConversationHandler.END

def button(update, _):
    query = update.callback_query
    variant = query.data

    query.answer()
    if variant == 'learning':
        query.edit_message_text(text=f"Выбранный вариант: Обучение")
    else:
        query.edit_message_text(text=f"Выбранный вариант: Тестирование")
def cancel(update: Update, context: CallbackContext) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text(
        'Bye! I hope we can talk again some day.', reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


def main() -> None:
    """Run the bot."""
    updater = Updater("здесь токен")
    dispatcher = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            BIO: [MessageHandler(Filters.text & ~Filters.command, bio)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dispatcher.add_handler(conv_handler)
    updater.dispatcher.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
