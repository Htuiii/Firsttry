# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import telebot
import time
bot = telebot.TeleBot('7254822664:AAHE39qs-0cpwDud3ODnDZ5JLSqxZf7DSIM')
@bot.message_handler(commands=['/start'])
@bot.message_handler(func=lambda msg: msg.text == '/start')
def start_message(message):
    bot.send_message(message.from_user.id, "if you want to see the power of this bot send /go")
@bot.message_handler(func=lambda msg: msg.text == '/go')
def tthousend_memes(message):
    for i in range(0,10):
        time.sleep(0.3)
        bot.send_photo(message.from_user.id, photo=open('meme.jpg', 'rb'))
    bot.send_message(message.from_user.id, "if you want to see the power of this bot send /go")

bot.infinity_polling()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
