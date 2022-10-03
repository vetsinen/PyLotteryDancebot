from telebot import TeleBot, types
from os import path
import pickle

bot = TeleBot("5616779070:AAFNDOX-H8v9Po_mmdaHWwGfv3ApwoOwjSs",
              parse_mode=None)  # You can set parse_mode by default. HTML or MARKDOWN
wild_dances_channel_id = -1001866935354

datafile = "participants.pickle"
if path.exists(datafile):
    with open(datafile, 'rb') as f:
        participants = pickle.load(f)
else:
    participants = []

text = 'Запрошуємо вас взяти участь в розіграші безкоштовного входу '
'на бачакіз вечірку в середу, '
'для цього клацніть на кнопку нижче'
' щоб виграти вхід на двох після натискання кнопки, '
'напишіть як звати партнера чи партнерку'
' боту @PyLotteryDancebot'

dummy = 'вигравайте безкоштовну подорож центром Києва на 3 жовтня'

@bot.message_handler(commands=['publish'])
def send_lottery(message):
    button_bar = types.InlineKeyboardButton('Хочу безкоштовний вхід', callback_data='bachakizz')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(button_bar)
    bot.send_message(wild_dances_channel_id, text=dummy,
    reply_markup = keyboard)

    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.reply_to(message, "Добрий вечір. Ми з України!")

    @bot.message_handler(commands=['list'])
    def send_list(message):
        bot.reply_to(message, str(participants))

    @bot.callback_query_handler(func=lambda call: True)
    def callback_query(call):
        if call.data == 'bachakizz':
            user = call.from_user
            participant = {'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name,
                           'username': user.username}
            print(participant)
            if participant not in participants:  # TODO: change to user.id checking
                participants.append(participant)
                with open(datafile, 'wb') as f:
                    pickle.dump(participants, f)
                bot.answer_callback_query(call.id, 'ваша заявка на участь прийнята', show_alert=True)
            else:
                bot.answer_callback_query(call.id, 'ви вже подавала заявку на участь раніше', show_alert=True)

        print(participants)

bot.infinity_polling()
