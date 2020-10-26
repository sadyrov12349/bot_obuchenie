# -*- coding: utf8 -*-

import telebot
from congst import *


bot = telebot.TeleBot(api_token)

def choice4(vibor):

    if vibor == '❌ТЕХНИЧЕСКИАЯ':
            # VIDEO
            #текст
        keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard.row('Задание')
        keyboard.row('↩️Назад', '↪️Далее')
        text = 'ТЕХНИЧЕСКОЙ ПОДГОТОВКИ'
        return keyboard, text

    elif vibor == '3️⃣Доп курсы':
        pass


