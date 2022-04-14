from telebot import types

def main_menu():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='Кино',
                                          callback_data='cinema'))
    markup.add(types.InlineKeyboardButton(text='Концерты',
                                          callback_data='concert'))
    markup.add(types.InlineKeyboardButton(text='Театр',
                                          callback_data='theatre'))
    markup.add(types.InlineKeyboardButton(text='Спорт',
                                          callback_data='sport'))
    markup.add(types.InlineKeyboardButton(text='Пушкинская карта',
                                          callback_data='pushkincard'))
    return markup
