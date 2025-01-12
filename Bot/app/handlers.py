import os, logging
from telebot import TeleBot, types
from telebot.types import Message
import requests


# t.me/PersonalTrainin_5finger_bot/My_Some_App - обёртка в котором храниться реальный url приложения

def start(message: Message, bot: TeleBot) -> None:
    # ВАЖНО: запустить веб-приложение через mini apps можно около 7 способов, но чтобы приложение можно получить данные о телеграм-пользователе нужно юзать через inline кнопки
    
    # Все будет корректно обработано и в window.Telegram.WebApp.initDataUnsafe.user (в JS) данные о пользователе будут
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text="Открыть сайт", url=os.getenv("APP_URL"))
    markup.add(button)
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку, чтобы открыть сайт.", reply_markup=markup)
  
def some_call_api_1(message: Message, bot: TeleBot) -> None:
    response = requests.get('http://localhost:8000/api/catalog')
    # Если просто обратиться к response по это просто оболочка ответа (код 200 усех, или 404 ненайден или...) нужно обращаться к телу .text
    bot.send_message(message.chat.id, text=f"get 1 = {response.text}")
    
def some_call_api_2(message: Message, bot: TeleBot) -> None:
    payload = {"product_id": '111', "user_id": '1111'}
    response = requests.post('http://localhost:8000/api/orders/create', json=payload)
    bot.send_message(message.chat.id, text=f"post 1 = {response}")