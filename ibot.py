#!/usr/bin/python3
# -*- coding: utf-8 -*-

from aiogram import executor
from utils import MyBot
from messages.intro import *
from messages.chapter1 import *
from messages.chapter2 import *
from messages.chapter3 import *
from messages.chapter4 import *
from messages.chapter5 import *

if __name__ == "__main__":
      
    bot, dp = MyBot().get_bot()
    register_handlers_intro(dp)
    register_handlers_chapter1(dp)
    register_handlers_chapter2(dp)
    register_handlers_chapter3(dp)
    register_handlers_chapter4(dp)
    register_handlers_chapter5(dp)
    executor.start_polling(dp, skip_updates=True)
