import telebot
import random
import time

bot = telebot.TeleBot("5594571511:AAFpZRRdyCr6KdzkWBIhfqLAj44IaASEbaU")

@bot.message_handler(commands=["start"])
def start(message):
	mess1 = f"<b>Привет!</b>"
	mess2 = f"Я бот🤖 созданный <i>Акелем</i>👨‍💻!"
	mess3 = f"Я буду просто с Вами разговаривать. 😉"
	bot.send_message(message.chat.id, mess1, parse_mode="html")
	time.sleep(1.5)
	bot.send_message(message.chat.id, mess2, parse_mode="html")
	time.sleep(1.5)
	bot.send_message(message.chat.id, mess3, parse_mode="html")

@bot.message_handler(commands=["help"])
def help(message):
	MSG1 = "--Привет"
	MSG2 = "--Пока"
	MSG3 = "--Как дела?"
	MSG4 = "--Что делаешь?"
	MSG5 = "--Напиши id чата"
	MSG6 = "--Расскажи анекдот"
	HELP = "<b>НО!</b> Нужно всё это писать <i><b>правильно</b></i>!"
	bot.send_message(message.chat.id, MSG1, parse_mode="html")
	bot.send_message(message.chat.id, MSG2, parse_mode="html")
	bot.send_message(message.chat.id, MSG3, parse_mode="html")
	bot.send_message(message.chat.id, MSG4, parse_mode="html")
	bot.send_message(message.chat.id, MSG5, parse_mode="html")
	bot.send_message(message.chat.id, MSG6, parse_mode="html")
	time.sleep(1)
	bot.send_message(message.chat.id, HELP, parse_mode="html")

@bot.message_handler()
def MSGs(message):
	if message.text == "Привет":
		bot.send_message(message.chat.id, "Привет👋!", parse_mode="html")
	elif message.text == "Пока":
		bot.send_message(message.chat.id, "Пока😞", parse_mode="html")
	elif message.text == "Как дела?":
		bot.send_message(message.chat.id, "У меня всё хорошо😊.", parse_mode="html")
	elif message.text == "Что делаешь?":
		bot.send_message(message.chat.id, "Я сейчас просто разговариваю с Вами! 😁", parse_mode="html")
	elif message.text == "Напиши id чата":
		bot.send_message(message.chat.id, message.chat.id, parse_mode="html")
	elif message.text == "Расскажи анекдот":
		anekdots = random.randint(1, 2)
		if anekdots == 1:
			bot.send_message(message.chat.id, "Приходит Чебурашка в кинотеатр:", parse_mode="html")
			time.sleep(1)
			bot.send_message(message.chat.id, " — Сколько стоит билет на фильм? ", parse_mode="html")
			time.sleep(1.2)
			bot.send_message(message.chat.id, "— Десять рублей😐.", parse_mode="html")
			time.sleep(1.5)
			bot.send_message(message.chat.id, "— У меня только пять😞.", parse_mode="html")
			time.sleep(2)
			bot.send_message(message.chat.id, "Пустите, пожалуйста, я буду смотреть одним глазом😜!", parse_mode="html")
		if anekdots == 2:
			bot.send_message(message.chat.id, "«Иду себе иду, никого не трогаю...»", parse_mode="html")
			time.sleep(1.3)
			bot.send_message(message.chat.id, "- так начинается каждый рассказ безрукого мальчика.", parse_mode="html")
	else:
		bot.send_message(message.chat.id, "Походу я не знаю этой каманды🥲", parse_mode="html")
		time.sleep(1.5)
		bot.send_message(message.chat.id, "Но Вы можете посмотреть что я могу!", parse_mode="html")
		time.sleep(1)
		bot.send_message(message.chat.id, "Просто напишите <u>/help</u>", parse_mode="html")
		print(message.from_user.first_name, "-", message.text)

bot.polling(none_stop=True)
