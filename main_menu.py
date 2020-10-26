# -*- coding: utf8 -*-
import telebot
from congst import *
bot = telebot.TeleBot(api_token)

def start_menu():
        keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard.row('⚖Оценка залогов')
        keyboard.row('📞Колл-центр')
        keyboard.row('🛡Обучение по продажам')
        keyboard.row('🔐ХРАНЕНИЕ ЗАЛОГОВ')
        keyboard.row('🚨Безопасность')
        keyboard.row('⚒Рабочие процессы')
        keyboard.row('🎛Работа с оборудованием')
        keyboard.row('🚙По выездной группы')
        keyboard.row('🎓Для Директоров')

        return keyboard