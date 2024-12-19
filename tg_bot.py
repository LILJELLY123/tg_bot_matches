import telebot
import requests

BOT_TOKEN = '8031786381:AAGeSljDFGo-x2q6nRTwbfgyOpIAjXfc1qA' #Мой токен
bot = telebot.TeleBot(BOT_TOKEN)

# Функция для загрузки данных из JSON-файла
def load_matches():
    with open('sports_events.json', 'r') as file:
        data = json.load(file)
        return data['matches']
