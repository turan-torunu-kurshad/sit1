import telebot
from telebot import types
bot =telebot.TeleBot('8065800506:AAFw5I0eNnqX8PrIG5ZEOspjlLzaxOND3A4')
@bot.message_handler(commands=["start"])
def a12(message):
    bot.send_message(message,"salam gardash")
"""@bot.message_handler(commands=["aboutwe"])  """

if __name__=="__main__":
    bot.polling()


