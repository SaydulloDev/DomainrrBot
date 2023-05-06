from telebot import TeleBot

import buttons
import db
import domainr
import messages
import utils

API_TOKEN = 'YOUR TOKEN'

bot = TeleBot(API_TOKEN, parse_mode='HTML')


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    result_db = db.check_user_registry(user_id=chat_id)
    print(result_db)
    if result_db:
        lang_user = db.get_lang_user(user_id=chat_id)
        bot.send_message(chat_id, messages.START.get(lang_user))

    else:
        bot.send_message(chat_id, messages.LANG,
                         reply_markup=buttons.basic_buttons(utils.LANGUAGES, 'lang'))


@bot.message_handler(commands=['language'])
def change_language(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, messages.LANG, reply_markup=buttons.basic_buttons(utils.LANGUAGES, 'lang'))


@bot.callback_query_handler(lambda c: c.data.startswith('lang'))
def select_lang(call):
    chat_id = call.message.chat.id
    lang = call.data.split('_')[1]
    if db.check_user_registry(chat_id):
        result = db.update_language(lang, user_id=chat_id)
        if result:
            lang_user = db.get_lang_user(user_id=chat_id)
            bot.send_message(chat_id, messages.LANG_RESULT.get(lang_user))
            bot.delete_message(chat_id, call.message.id)
    else:
        first_name = call.message.chat.first_name
        username = call.message.chat.username
        bot.delete_message(chat_id, call.message.id)
        if username:
            result = db.registry_user(chat_id, first_name, lang, username)
            if result:
                bot.send_message(chat_id, messages.LANG_RESULT.get(lang))
        else:
            result = db.registry_user(chat_id, first_name, lang)
            if result:
                bot.send_message(chat_id, messages.LANG_RESULT.get(lang))


@bot.message_handler(commands=['stat'])
def stat(message):
    chat_id = message.chat.id
    lang_user = db.get_lang_user(chat_id)
    statistics = db.stat()
    bot.send_message(chat_id, messages.stat(lang_user, statistics))


@bot.message_handler(commands=['status'])
def search(message):
    chat_id = message.chat.id
    lang_user = db.get_lang_user(chat_id)
    msg = bot.send_message(chat_id, messages.STATUS.get(lang_user))
    bot.register_next_step_handler(msg, search_answer)


def search_answer(message):
    chat_id = message.chat.id
    request = message.text
    if utils.is_ascii(request) and not request.startswith('/') and request.find('.') != -1:
        info_request = domainr.get_domain_status(request)
        sorted_info = utils.list_to_dict(info_request)
        bot.send_message(chat_id, messages.info(sorted_info))


if __name__ == '__main__':
    print('Starting...')
    bot.infinity_polling()
