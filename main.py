import telebot
from telebot import types
import main_menu


token = '5397618648:AAElaUJa9lBJwDGCNN6nJVk3AhgUwzrrOy8'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
   keyboard = types.ReplyKeyboardRemove()
   bot.send_message(message.chat.id, text="Привет! С помощью нашего бота ты с легкостью сможешь разнообразить свой досуг. Просто выбери понравившееся мероприятие.",
                    reply_markup=keyboard)
   markup = main_menu.main_menu()
   bot.send_message(message.chat.id, text="Выберите нужную категорию.", reply_markup=markup) #предлагаем пользователю выбрать запрос



@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
   bot.answer_callback_query(callback_query_id=call.id, text='Результат вашего запроса.')

   if call.data == 'cinema':
       keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
       keyboard.add(*[types.KeyboardButton(element) for element in
                      ['Все фильмы',
                       'Фильмы по жанрам',
                       'Фильмы по возрастному ограничению',
                       'Вернуться назад']])
       bot.send_message(call.message.chat.id, text='Выберите нужную категорию.',
                        reply_markup=keyboard)

   elif call.data == 'concert':
       keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
       keyboard.add(*[types.KeyboardButton(element) for element in
                      ['Все концерты',
                       'Стендап',
                       'Музыка',
                       'Вернуться назад']])
       bot.send_message(call.message.chat.id, text='Выберите нужную категорию.',
                        reply_markup=keyboard)

   elif call.data == 'theatre':
       keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
       keyboard.add(*[types.KeyboardButton(element) for element in
                      ['Все спектакли',
                       'Спектакли по жанру',
                       'Спектакли по возрастному ограничению',
                       'Вернуться назад']])
       bot.send_message(call.message.chat.id, text='Выберите нужную категорию.',
                        reply_markup=keyboard)


   elif call.data == 'sport':
       keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
       keyboard.add(*[types.KeyboardButton(element) for element in
                      ['Все матчи',
                       'Вернуться назад']])
       bot.send_message(call.message.chat.id, text='Выберите нужную категорию.',
                        reply_markup=keyboard)

   elif call.data == 'pushkincard':
       keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
       keyboard.add(*[types.KeyboardButton(element) for element in
                      ['Cписок мероприятий',
                       'Вернуться назад']])
       bot.send_message(call.message.chat.id, text='Выберите нужную категорию.',
                        reply_markup=keyboard)



@bot.message_handler(content_types=['text'])
def answer_on_message(message):

    if message.text == 'Вернуться назад':
       return start_message(message)


    elif message.text =='Все матчи':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(element) for element in ['Вернуться назад']])
        bot.send_message(message.chat.id, text='Список всех доступных матчей:', reply_markup=keyboard)



    elif message.text =='Cписок мероприятий':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(element) for element in ['Вернуться назад']])
        bot.send_message(message.chat.id, text='Список всех доступных мероприятий по пушкинской карте:',
                         reply_markup=keyboard)


    elif message.text == 'Все фильмы':
       keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
       keyboard.add(*[types.KeyboardButton(element) for element in
                       ['Вернуться назад']])
       bot.send_message(message.chat.id, 'Список всех доступных фильмов.', reply_markup=keyboard)
    elif message.text == 'Фильмы по жанрам':
       bot.send_message(message.chat.id, text='Выберите нужную категорию.')
       keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
       keyboard.add(*[types.KeyboardButton(element) for element in
                      ['Вернуться назад']])
       bot.send_message(message.chat.id, 'Список всех доступных фильмов по выбранному жанру.', reply_markup=keyboard)

    elif message.text == 'Фильмы по возрастному ограничению':
       bot.send_message(message.chat.id, text='Выберите нужную категорию.')
       keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
       keyboard.add(*[types.KeyboardButton(element) for element in
                      ['Фильмы 0+',
                       'Фильмы 6+',
                       'Фильмы 12+',
                       'Фильмы 16+',
                       'Фильмы 18+',
                       'Вернуться назад']])
       bot.send_message(message.chat.id, 'Список всех доступных фильмов по выбранной возрастной категории.',
                        reply_markup=keyboard)
    elif message.text == 'Фильмы 0+':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(element) for element in ['Вернуться назад']])
        bot.send_message(message.chat.id, text='Список всех доступных фильмов 0+:', reply_markup=keyboard)
    elif message.text == 'Фильмы 6+':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(element) for element in ['Вернуться назад']])
        bot.send_message(message.chat.id, text='Список всех доступных фильмов 6+:', reply_markup=keyboard)
    elif message.text == 'Фильмы 12+':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(element) for element in ['Вернуться назад']])
        bot.send_message(message.chat.id, text='Список всех доступных фильмов 12+:', reply_markup=keyboard)
    elif message.text == 'Фильмы 16+':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(element) for element in ['Вернуться назад']])
        bot.send_message(message.chat.id, text='Список всех доступных фильмов 16+:', reply_markup=keyboard)
    elif message.text == 'Фильмы 18+':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(element) for element in ['Вернуться назад']])
        bot.send_message(message.chat.id, text='Список всех доступных фильмов 18+:', reply_markup=keyboard)



    elif message.text == 'Все концерты':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(element) for element in ['Вернуться назад']])
        bot.send_message(message.chat.id, text='Список всех доступных концертов.', reply_markup=keyboard)
    elif message.text == 'Стендап':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(element) for element in
                       ['Все стендап-концерты',
                        'Стендап-концерты определенного артиста',
                        'Вернуться назад']])
        bot.send_message(message.chat.id, text='Выберите нужную категорию.', reply_markup=keyboard)
    elif message.text == 'Все стендап-концерты':
       keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
       keyboard.add(*[types.KeyboardButton(element) for element in
                       ['Вернуться назад']])
       bot.send_message(message.chat.id, text='Список всех доступных стендап-концертов.', reply_markup=keyboard)
    elif message.text == 'Стендап-концерты определенного артиста':
       keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
       keyboard.add(*[types.KeyboardButton(element) for element in
                       ['Вернуться назад']])
       bot.send_message(message.chat.id, text='Выберите нужного артиста.', reply_markup=keyboard)
    elif message.text == 'Музыка':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(element) for element in
                       ['Все музыкальные концерты',
                        'Музыкальные концерты определенного исполнителя',
                        'Вернуться назад']])
        bot.send_message(message.chat.id, text='Выберите нужную категорию.', reply_markup=keyboard)
    elif message.text == 'Все музыкальные концерты':
       keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
       keyboard.add(*[types.KeyboardButton(element) for element in
                       ['Вернуться назад']])
       bot.send_message(message.chat.id, text='Список всех доступных музыкальных концертов.',
                        reply_markup=keyboard)
    elif message.text == 'Музыкальные концерты определенного исполнителя':
       keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
       keyboard.add(*[types.KeyboardButton(element) for element in
                       ['Вернуться назад']])
       bot.send_message(message.chat.id, text='Выберите нужного исполнителя.', reply_markup=keyboard)




    elif message.text =='Все спектакли':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(element) for element in
                       ['Вернуться назад']])
        bot.send_message(message.chat.id, text='Список всех доступных спектаклей:', reply_markup=keyboard)
    elif message.text =='Спектакли по жанру':
        bot.send_message(message.chat.id, text='Список всех доступных спектаклей по выбранному жанру:')
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(element) for element in
                       ['Вернуться назад']])
        bot.send_message(message.chat.id, text='Выберите нужную категорию.',
                         reply_markup=keyboard)
    elif message.text =='Спектакли по возрастному ограничению':
        bot.send_message(message.chat.id, 'Список всех доступных спектаклей по выбранной возрастной категории.')
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(element) for element in
                       ['Спектакли 0+',
                        'Спектакли 6+',
                        'Спектакли 12+',
                        'Спектакли 16+',
                        'Спектакли 18+',
                        'Вернуться назад']])
        bot.send_message(message.chat.id, text='Выберите нужную категорию.',
                         reply_markup=keyboard)
    elif message.text == 'Спектакли 0+':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(element) for element in ['Вернуться назад']])
        bot.send_message(message.chat.id, text='Список всех доступных спектаклей 0+:', reply_markup=keyboard)
    elif message.text == 'Спектакли 6+':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(element) for element in ['Вернуться назад']])
        bot.send_message(message.chat.id, text='Список всех доступных спектаклей 6+:', reply_markup=keyboard)
    elif message.text == 'Спектакли 12+':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(element) for element in ['Вернуться назад']])
        bot.send_message(message.chat.id, text='Список всех доступных спектаклей 12+:', reply_markup=keyboard)
    elif message.text == 'Спектакли 16+':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(element) for element in ['Вернуться назад']])
        bot.send_message(message.chat.id, text='Список всех доступных спектаклей 16+:', reply_markup=keyboard)
    elif message.text == 'Спектакли 18+':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(element) for element in ['Вернуться назад']])
        bot.send_message(message.chat.id, text='Список всех доступных спектаклей 18+:', reply_markup=keyboard)



bot.polling(none_stop=True)
