# -*- coding: utf8 -*-

import telebot
from congst import *

bot = telebot.TeleBot(api_token)

def choice1(vibor):

    if vibor == '⚖Оценка залогов':
        keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard.row('📱 SAMSUNG', '📱 IPHONE')
        keyboard.row('📱 другие модели', '💍 ЗОЛОТО')
        keyboard.row('💻 НОУТБУКИ', '🎧 НАУШНИКИ AIRPODS')
        keyboard.row('⌚ ЧАСЫ APPLE WHATCH', '📷 ФОТО АППАРАТЫ')
        keyboard.row('🧥 ШУБЫ', '↩️Назад')
        text = 'Оценка залогов'
        return keyboard, text

    elif vibor == '📞Колл-центр':
        keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard.row('1', '2', '3')
        keyboard.row('↩️Назад')
        text = 'Колл центр'
        return keyboard, text

    elif vibor == '🛡Обучение по продажам':
        keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard.row('1️⃣Вводный курс', '2️⃣Шаги продаж')
        keyboard.row('3️⃣Доп курсы', '↩️Назад')
        text = 'Обучение по продажам'
        return keyboard, text



    elif vibor == '🔐ХРАНЕНИЕ ЗАЛОГОВ':
        keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard.row('1', '2', '3')
        keyboard.row('↩️Назад')
        text = 'ХРАНЕНИЕ ЗАЛОГОВ'
        return keyboard, text

    elif vibor == '🚨Безопасность':
        keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard.row('1', '2', '3')
        keyboard.row('↩️Назад')
        text = 'Безопасность'
        return keyboard, text

    elif vibor == '⚒Рабочие процессы':
        keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard.row('1', '2', '3')
        keyboard.row('↩️Назад')
        text = 'Рабочие процессы'
        return keyboard, text

    elif vibor == '🎛Работа с оборудованием':
        keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard.row('1', '2', '3')
        keyboard.row('↩️Назад')
        text = 'Работа с оборудованием'
        return keyboard, text

    elif vibor == '🚙По выездной группы':
        keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard.row('1', '2', '3')
        keyboard.row('↩️Назад')
        text = 'По выездной группы'
        return keyboard, text

    elif vibor == '🎓Для Директоров':
        keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard.row('1', '2', '3')
        keyboard.row('↩️Назад')
        text = 'Для Директоров'
        return keyboard, text

