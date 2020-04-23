import telebot
import requests
import config

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def polling(message):
    if message.text == "Привет, Богдан":
        bot.send_message(message.chat.id, "Привет, меня зовут Бам-Бам Дум-Дым, как ты?")
    elif message.text == 'Охуенная цитата':
        bot.send_message(message.chat.id, 'Как бы высоко ты не летал - не забывай с кем ты ползал, АУФ БЛЯТЬ!')



print("Программа запущена")

if __name__ == '__main__':
    bot.polling(none_stop=True)