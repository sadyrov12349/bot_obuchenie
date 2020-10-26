# -*- coding: utf8 -*-
import telebot
from congst import *
from main_menu import *
bot = telebot.TeleBot(api_token)

def mainMenuButton(way, m1):
    m1 = '1'
    way.clear()
    way.append('🔁Главное меню')
    keys = start_menu()
    return m1, way, keys

def backButton(way, m1):
    m1 = int(m1)
    m1 -= 2
    m1 = str(m1)
    way.pop()
    w1 = way[len(way)-1]
    way.pop()
    return way, m1, w1