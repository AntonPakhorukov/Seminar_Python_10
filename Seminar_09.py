import telebot
from Config import token
import random
import Compress

bot = telebot.TeleBot(token)

"""Команда старта"""

@bot.message_handler(commands=['start']) # декоратор - команда запуска чата /start
def welcome(message):
    bot.send_message(message.chat.id, 'Добро пожаловать!')
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True) # создаем кнопки
    item1 = telebot.types.KeyboardButton("Рандомное число")
    item2 = telebot.types.KeyboardButton("Сжать текст")
    item3 = telebot.types.KeyboardButton("Анекдот")
    markup.add(item1, item2, item3) # добавили кнопки


    bot.send_message(message.chat.id, "Добро пожаловать! Выберите нужный вам пункт меню: ", reply_markup=markup)

def random_number(message):
    bot.send_message(message.chat.id, str(random.randint(1, 10)))
# compress = False
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'привет':
        bot.send_message(message.chat.id, 'Привет, как дела?')
    elif message.text == 'Рандомное число':
        bot.send_message(message.chat.id, str(random.randint(1, 10)))
    elif message.text == 'Сжать текст':
        # Compress = True
        # @bot.message_handler(content_types=['text'])
        
        def send_RLE(message):
            my_string = 'AAAADDDGGGTSRTYYHHJJ'   
            bot.send_message(message.chat.id, Compress.Compress(my_string))
        send_RLE(message)  
    # elif compress and 
    elif message.text == 'Анекдот':
        bot.send_message(message.chat.id, str(random.randint(1, 10)))
    else:
        bot.send_message(message.chat.id, 'Данный функционал в разработке')


bot.polling(non_stop=True)
