from telebot import *
from output import *
import processing

API_TOKEN = '6075150372:AAFcAHmSXr-XfOCej8LD58yu4JYblt9fceo'

bot = TeleBot(API_TOKEN)

criteria = []
choices = {}
id = 0


@bot.message_handler(commands=["start"])
def welcome(message):
    global id, choices, criteria

    id = 0

    choices = {
        'lang': None,
        'gadget': None,
        'confidence_status': None,
        'calls': None
    }

    criteria = []

    key = types.InlineKeyboardMarkup()

    lang_ua = types.InlineKeyboardButton(text=ua, callback_data=ua)
    lang_en = types.InlineKeyboardButton(text=en, callback_data=en)

    key.add(lang_ua, lang_en)

    bot.send_message(message.chat.id, "Виберіть мову / Choose a language", reply_markup=key)


def process_data(user_message, criteria, language, gadget):
    result = processing.process(criteria, language)[0][0]
    key = types.InlineKeyboardMarkup()
    if gadget == devices[language][0]:
        link = types.InlineKeyboardButton(text="Перейти до тарифу", url=links[gadget][result][1])
        key.add(link)
        bot.edit_message_text(
            links[gadget][result][0],
            chat_id=user_message.message.chat.id,
            message_id=user_message.message.message_id,
            reply_markup=key
        )
    else:
        link = types.InlineKeyboardButton(text="Перейти до тарифу", url=links[gadget][1])
        key.add(link)
        bot.edit_message_text(
            links[gadget][result],
            chat_id=user_message.message.chat.id,
            message_id=user_message.message.message_id,
            reply_markup=key
        )

@bot.callback_query_handler(func=lambda user_message: id < 2)
def main_questions(user_message):
    print(choices)
    global id
    key = types.InlineKeyboardMarkup()

    if choices['lang'] is None: choices['lang'] = user_message.data
    language = choices['lang']

    button_lst = []
    for option_id in range(len(questions[language][id]['options'])):
        option = questions[language][id]['options'][option_id]
        button_lst.append(types.InlineKeyboardButton(text=option, callback_data=option))

    key.add(*button_lst)

    bot.edit_message_text(
        questions[language][id]['text'],
        chat_id=user_message.message.chat.id,
        message_id=user_message.message.message_id,
        reply_markup=key
    )
    id += 1


@bot.callback_query_handler(func=lambda user_message: id == 2)
def additional_questions(user_message):
    print(choices)
    global id

    if choices['gadget'] is None: choices['gadget'] = user_message.data

    key = types.InlineKeyboardMarkup()

    gadget = choices['gadget']
    language = choices['lang']

    if gadget in devices[language][2:]:
        process_data(user_message, criteria, language, gadget)
    else:
        question = questions[language][gadget][0]

        button_lst = []
        for option_id in range(len(question['options'])):
            option = question['options'][option_id]
            button_lst.append(types.InlineKeyboardButton(text=option, callback_data=option))

        key.add(*button_lst)

        bot.edit_message_text(
            question['text'],
            chat_id=user_message.message.chat.id,
            message_id=user_message.message.message_id,
            reply_markup=key
        )
        id += 1


@bot.callback_query_handler(func=lambda user_message: id > 2)
def concrete_questions(user_message):
    print(choices)
    global id
    language = choices['lang']
    gadget = choices['gadget']

    phone = questions[language][1]['options'][0]
    tablet = questions[language][1]['options'][1]
    watch = questions[language][1]['options'][2]
    router = questions[language][1]['options'][3]
    other = questions[language][1]['options'][4]

    if gadget == phone:
        if choices['confidence_status'] is None: choices['confidence_status'] = user_message.data
    elif gadget == tablet:
        if choices['calls'] is None: choices['calls'] = user_message.data
    elif gadget == watch: print('Гаджет')
    elif gadget == router: print('Гаджет')
    elif gadget == other: print('Гаджет')

    if choices['calls'] == questions[language][tablet][0]['options'][0]:
        choices['calls'] = 'processed'
        choices['gadget'] = phone
        id -= 1
        additional_questions(user_message)

    else:
        try:
            criteria.append(user_message.data)

            key = types.InlineKeyboardMarkup()

            gadget = choices['gadget']
            language = choices['lang']
            confidence_call_status = choices['calls'] if choices['confidence_status'] is None else choices[
                'confidence_status']

            print(id)
            question = questions[language][gadget][confidence_call_status][id - 3]

            button_lst = []
            for option_id in range(len(question['options'])):
                option = question['options'][option_id]
                button_lst.append(types.InlineKeyboardButton(text=option, callback_data=option))

            key.add(*button_lst)

            bot.edit_message_text(
                question['text'],
                chat_id=user_message.message.chat.id,
                message_id=user_message.message.message_id,
                reply_markup=key
            )
            id += 1
        except KeyError:
            print(criteria)
            process_data(user_message, criteria, language, gadget)


bot.infinity_polling()
