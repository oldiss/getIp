import telebot
import config
import urllib.request

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands = ['get'])
def get(message):
	ip = urllib.request.urlopen('https://api.ipify.org').read()
	bot.send_message(message.chat.id, ip)
	
bot.polling(none_stop = True)