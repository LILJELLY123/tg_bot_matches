import telebot
import requests

BOT_TOKEN = '8031786381:AAGeSljDFGo-x2q6nRTwbfgyOpIAjXfc1qA' #Мой токен
bot = telebot.TeleBot(BOT_TOKEN)

# Функция для загрузки данных из JSON-файла
def load_matches():
    with open('sports_events.json', 'r') as file:
        data = json.load(file)
        return data['matches']
        
# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "Привет! Я спортивный бот, который может предоставить информацию о спортивных событиях.\n"
        "Используйте следующие команды:\n"
        "/matches - Посмотреть список спортивных событий\n"
        "/help - Получить помощь по командам"
    )
    bot.send_message(message.chat.id, welcome_text)

# Команда /help
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "Доступные команды:\n"
        "/start - Приветствие и информация о боте\n"
        "/matches - Посмотреть список спортивных событий"
    )
    bot.send_message(message.chat.id, help_text)
