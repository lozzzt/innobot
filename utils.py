#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import psycopg2
import yaml
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# Singleton
class Log(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Log, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def getLogger(self):
        return self.logger

# Singleton
class Config(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Config, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        with open("config.yaml", "r") as ymlfile:
            self.config = yaml.safe_load(ymlfile)

    def get_config(self):
        return self.config

# Singleton
class DB(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DB, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.db = Config().get_config()['DB']
        self.connect = psycopg2.connect(database=self.db['NAME'], user=self.db['USER'], password=self.db['PASSWORD'], host=self.db['HOST'], port=self.db['PORT'])
        Log().getLogger().info("Opened database successfully")
        self.cursor = self.connect.cursor()

    def get_connect_cursor(self):
        return self.connect, self.cursor

# Singleton
class MyBot(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MyBot, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.storage = MemoryStorage()
        self.bot = Bot(token=Config().get_config()['TELEGRAM']['TOKEN'])
        self.dp = Dispatcher(self.bot, storage=self.storage)

    def get_bot(self):
        return self.bot, self.dp

# Singleton
class Counter(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Counter, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.counter = 0

    def get_counter(self):
        return self.counter

    def set_counter(self, num):
        self.counter = num

    def increase_counter(self):
        self.counter += 1

    def decrease_counter(self):
        self.counter -= 1
