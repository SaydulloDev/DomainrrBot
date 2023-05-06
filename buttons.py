from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def basic_buttons(dictionary, action):
    basic_markup = InlineKeyboardMarkup()
    for key, value in dictionary.items():
        button = InlineKeyboardButton(text=value, callback_data=f'{action}_{key}')
        basic_markup.add(button)
    return basic_markup
