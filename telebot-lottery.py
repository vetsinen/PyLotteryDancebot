from telebot import TeleBot, types


bot = TeleBot("5616779070:AAFNDOX-H8v9Po_mmdaHWwGfv3ApwoOwjSs", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN
wild_dances_channel_id = -1001866935354

@bot.message_handler(commands=['start', 'help', 'publish'])
def send_welcome(message):
	button_bar = types.InlineKeyboardButton('Bar', callback_data='bar')
	keyboard = types.InlineKeyboardMarkup()
	keyboard.add(button_bar)

	bot.send_message(wild_dances_channel_id, text='Keyboard example', reply_markup=keyboard)
	# bot.send_message(wild_dances_channel_id, text='Message')
	# bot.reply_to(message, "Howdy, how are you doing?")

@bot.callback_query_handler(func=lambda call:True)
def callback_query(call):
	if call.data == 'bar':
		print('bar')
		bot.answer_callback_query(call.id, 'ваша заявка на участь прийнята', show_alert=True)
		# bot.send_message(chat_id=call.message.chat.id,text="1")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()