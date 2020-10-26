# -*- coding: utf8 -*-

import telebot
from congst import *
import os
bot = telebot.TeleBot(api_token)

def choice5(vibor):

    if vibor == '↪️Далее':
        keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard.row('↩️Назад', '❌ЭМОЦИОНАЛЬНЯ')
        text = 'Далее'
        return keyboard, text

def choice6(vibor):
    if vibor == '❌ЭМОЦИОНАЛЬНЯ':
        # VIDEO
        #текст
        keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard.row('Задание')
        keyboard.row('↩️Назад', '↪️Далее')
        text = 'ЭМОЦИОНАЛЬНОЙ ПОДГОТОВКИ'
        return keyboard, text

def choice7(vibor):
    if vibor == '↪️Далее':
        keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard.row('ШАГ 2️⃣ ПРИВЕТСТВИЕ. УСТАНОВЛЕНИЕ КОНТАКТА')
        keyboard.row('↩️Назад')
        text = '↪️Далее'
        return keyboard, text

def choice8(vibor):
    if vibor == 'ШАГ 2️⃣ ПРИВЕТСТВИЕ. УСТАНОВЛЕНИЕ КОНТАКТА':
        #Video
        keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard.row('Задание')
        keyboard.row('↩️Назад', '↪️Далее')
        text = 'ШАГ 2️⃣ ПРИВЕТСТВИЕ. УСТАНОВЛЕНИЕ КОНТАКТА'
        return keyboard, text

def choice9(vibor):
    if vibor == '↪️Далее':
        keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard.row('ШАГ 3️⃣ ВЫЯВЛЕНИЕ ПОТРЕБНОСТЕЙ')
        keyboard.row('↩️Назад')
        text = '↪️Далее'
        return keyboard, text

def choice10(vibor):
    if vibor == 'ШАГ 3️⃣ ВЫЯВЛЕНИЕ ПОТРЕБНОСТЕЙ':
        #Video
        #Test
        keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard.row('↩️Назад', '↪️Далее')
        text = 'ШАГ 3️⃣ ВЫЯВЛЕНИЕ ПОТРЕБНОСТЕЙ'
        return keyboard, text

def choice11(vibor):
    if vibor == '↪️Далее':
        keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard.row('↩️Назад', '↪️Далее')
        text = '↪️Далее'
        return keyboard, text
# zadanie1 = str(input("Что мы делаем?: "))
# zadanie2 = str(input("Что ты делаешь?: "))

def choice12(vibor):
    if vibor == '↪️Далее':
        keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard.row('ШАГ 4️⃣ ПРЕЗЕНТАЦИЯ')
        keyboard.row('↩️Назад')
        text = '↪️Далее'
        return keyboard, text

def choice13(vibor):
    if vibor == 'ШАГ 4️⃣ ПРЕЗЕНТАЦИЯ':
        #Video
        #Test
        keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard.row('↩️Назад', '↪️Далее')
        text = 'ПРЕЗЕНТАЦИИ'
        return keyboard, text

def choice14(vibor):
    if vibor == '↪️Далее':
        keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard.row('↩️Назад', '↪️Далее')
        text = '↪️Далее'
        return keyboard, text

def choice15(vibor):
    if vibor == '↪️Далее':
        keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard.row('ШАГ 5️⃣ ОТРАБОТКА ВОЗВРАЖЕНИЙ')
        keyboard.row('↩️Назад')
        text = '↪️Далее'
        return keyboard, text

def choice16(vibor):
    if vibor == 'ШАГ 5️⃣ ОТРАБОТКА ВОЗВРАЖЕНИЙ':
        #Video
        #Test
        keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard.row('↩️Назад', '↪️Далее')
        text = 'ШАГ 5️⃣ ОТРАБОТКА ВОЗВРАЖЕНИЙ'
        return keyboard, text

def choice17(vibor):
    if vibor == '↪️Далее':
        keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard.row('↩️Назад', '↪️Далее')
        text = '↪️Далее'
        return keyboard, text

def choice18(vibor):
    if vibor == '↪️Далее':
        keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard.row('ШАГ 6️⃣ ЗАВЕРШЕНИЕ СДЕЛКИ')
        keyboard.row('↩️Назад')
        text = '↪️Далее'
        return keyboard, text

def choice19(vibor):
    if vibor == 'ШАГ 6️⃣ ЗАВЕРШЕНИЕ СДЕЛКИ':
        #Video
        #Test
        keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard.row('↩️Назад', '↪️Далее')
        text = 'ШАГ 6️⃣ ЗАВЕРШЕНИЕ СДЕЛКИ'
        return keyboard, text

def choice20(vibor):
    if vibor == '↪️Далее':
        keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard.row('↩️Назад', '↪️Далее')
        text = '↪️Далее'
        return keyboard, text

def choice21(vibor):
    if vibor == '↪️Далее':
        keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard.row('↩️Назад', 'ШАГ 8️⃣ АНАЛИЗ')
        text = '↪️Далее'
        return keyboard, text

def choice22(vibor):
    if vibor == 'ШАГ 8️⃣ АНАЛИЗ':
        #PDF
        keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard.row('↩️Назад', '🔁Главное меню')
        text = 'ШАГ 8️⃣ АНАЛИЗ'
        return keyboard, text




