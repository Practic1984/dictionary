import telebot
from selenium import webdriver
from time import sleep
from telebot import types

driver = webdriver.Chrome()

bot = telebot.TeleBot("5232657425:AAHppVYNS-5vqYmGwx2-FUXNuHK5ZK0ResI")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('Поиск в Yotube')
    item2 = types.KeyboardButton('Меню2')
    item3 = types.KeyboardButton('Меню3')
    item4  = types.KeyboardButton('Меню4')
    markup.add(item1,item2,item3,item4)
    bot.send_message(message.chat.id, "Привет, {0.first_name}!".format(message.from_user), reply_markup=markup) 

@bot.message_handler(commands=['search_videos'])
def search_videos(message):
    msg = bot.send_message(message.chat.id, "Введите текст, который вы хотите найти в YouTube")
    bot.register_next_step_handler(msg, search)


@bot.message_handler(content_types=['text'])
def text(message):
bot.send_message(message.chat.id, "Ты что то хотел?")

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Поиск в Yotube':         
            bot.send_message(message.chat.id, )
def search(message):
    bot.send_message(message.chat.id, "Начинаю поиск")
    video_href = "https://www.youtube.com/results?search_query=" + message.text
    driver.get(video_href)
    sleep(2)
    videos = driver.find_elements_by_id("video-title")
    for i in range(len(videos)):
        bot.send_message(message.chat.id, videos[i].get_attribute('href'))
        if i == 10:
            break
  
    
bot.polling()
 
