
import COVID19Py
import telebot
covid19 = COVID19Py.COVID19()
bot = telebot.TeleBot("5382934437:AAER9UoDpNTm10cMsl4kxq3_jHq3hVlFndA")

@bot.message_handler(commands=['start'])
def start(message):
    send_mess = f"<b>Привет {message.from_user.first_name}! </b>\n Введите страну"    
    bot.send_message(message.chat.id, send_mess, parse_mode='html')
bot.polling(non_stop=True)

@bot.message_handler(commands=['text'])
def mess(message):
    final_message = ""
    get_message_bot = message.text.strip().lower()
    if get_message_bot = 'сша'
        location = covid19.getLocationByCountryCode("US")
    elif get_message_bot == 'украина'
        location = covid19.getLocationByCountryCode("UA") 
    elif get_message_bot == 'россия'
        location = covid19.getLocationByCountryCode("RU")
    else
        location = covid19.getLatest()
        final_message = f"<u>Данные по всему миру:</u>\n Заболевшие: </b> {location ['contry ']}    


#latest = covid19.getLatest()
#location = covid19.getLocationByCountryCode("US")


































bot.polling()