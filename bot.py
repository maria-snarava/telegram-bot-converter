import os
import telebot
from pace import Run

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)
current_command = {'command': ''}

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hello, I could convert speed to pace. \n I's super-cool feature.")

@bot.message_handler(commands=['speed_km_h_to_pace', 'speed_km_h_to_m_s', 'miles_to_km', 'speed_m_h_to_pace'])
def command_hundler(message):
    current_command['command'] = message.text
    bot.reply_to(message, " Write the number:")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    try:
        if current_command['command'] == '/speed_km_h_to_pace':
            speed_km_h_to_pace(message)
        elif current_command['command'] == '/speed_km_h_to_m_s':
            speed_km_h_to_m_s(message)
        elif current_command['command'] == '/miles_to_km':
            miles_to_km(message)
        elif current_command['command'] == '/speed_m_h_to_pace':
            speed_m_h_to_pace(message)
        else:
            bot.reply_to(message, f'\'{current_command["command"]}\' You said {message.text}. Choose command from the list')
    except:
        bot.reply_to(message, 'Cannot print the result! Your variables are not numbers.')

def speed_km_h_to_pace(message):
    kilometers_per_hour = float(message.text)
    first_run = Run(kilometers_per_hour)

    bot.reply_to(message, f"{first_run.speed} kilometers per hour is equal to {first_run.pace} pace!")

def speed_km_h_to_m_s(message):
    ms = float(message.text) * 1000 / 3600
    formatted_ms = str("%.2f" % round(ms, 2))
    bot.reply_to(message, f"{message.text} kilometers per hour is equal to {formatted_ms} meter per second!")

def miles_to_km(message):
    km = float(message.text) * 1.60934
    formatted_km = str("%.5f" % round(km, 5))
    bot.reply_to(message, f"{message.text} miles is equal to {formatted_km} km!")

def speed_m_h_to_pace(message):
    miles_per_hour = float(message.text)
    first_run = Run(miles_per_hour * 1.60934)

    bot.reply_to(message, f"{first_run.speed} miles per hour is equal to {first_run.pace} pace!")


bot.infinity_polling()