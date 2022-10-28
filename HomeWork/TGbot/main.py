import telebot 
from telebot import types
import configparser

bot = telebot.TeleBot('5737065984:AAGD3OC_RY65k0yLU7mwDrx4BpEktwBytAk')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    btn2 = types.KeyboardButton("❓ Задать вопрос")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я тестовый бот для твоей статьи для habr.com".format(message.from_user), reply_markup=markup)

# @bot.message_handler(commands=['start'])
# def start_message(message):
#     mess = f"Привет, <b> {message.from_user.first_name} {message.from_user.last_name} </b> ✌️ Этот бот предназначен для игры 'Конфеты', чтобы узнать правила, введи сообщение 'rules'"
#     bot.send_message(message.chat.id, mess, parse_mode='html')
    
# @bot.message_handler()
# def get_user_text(message):
#     if message.text == "rules":
#        bot.send_message(message.chat.id,"На столе лежит 150 конфет. Каждый ход вы по очереди будете брать от 1 до 28 конфет. Проиграет тот, кто сделает ход последним, так как все конфеты в таком случае достаются игроку сделавшему ход предпоследним", parse_mode='html') 

# def play_game(message):
#     markup = types.ReplyKeyboardMarkup()
#     game = types.KeyboardButton('Погнали')
#     markup.add(game)
#     bot.send_message(message.chat.id, "гоу", reply_markup=markup)

bot.infinity_polling()