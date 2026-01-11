import telebot # библиотека telebot
from config import token # импорт токена

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Я бот для управления чатом.")

@bot.message_handler(commands=['ban'])
def ban_user(message):
    if message.reply_to_message: #проверка на то, что эта команда была вызвана в ответ на сообщение 
        chat_id = message.chat.id # сохранение id чата
         # сохранение id и статуса пользователя, отправившего сообщение
        user_id = message.reply_to_message.from_user.id
        user_status = bot.get_chat_member(chat_id, user_id).status 
         # проверка пользователя
        if user_status == 'administrator' or user_status == 'creator':
            bot.reply_to(message, "Невозможно забанить администратора.")
        else:
            bot.ban_chat_member(chat_id, user_id) # пользователь с user_id будет забанен в чате с chat_id
            bot.reply_to(message, f"Пользователь @{message.reply_to_message.from_user.username} был забанен.")
    else:
        bot.reply_to(message, "Эта команда должна быть использована в ответ на сообщение пользователя, которого вы хотите забанить.")

iventparticipant = ()
question = ()
answer_admin = ()
answer_user = ()
@bot.message_handler(commands=['ivent'])
def ivent(message):
    iventparticipant(input('Выбирите 1- чтобы ответить на вопрос или 2- чтобы добавить вопрос'))
    if iventparticipant == 1:
        print(question)
        print('Выбирите вариант ответа')
        answer_user = input(answer_admin)
    if iventparticipant == 2:
        print('Введите свой вопрос')
        question= input('пример: Какое сегодня число?')
        print('Введите варианты ответа')
        answer_admin = input('пример: 1- 20.11.2025 2- 01.01.2026 3- 11.01.2026')
        print('Вы создали вопрос:', question, 'Отыетами на каторый является', answer_admin)

@bot.message_handler(content_types=['new_chat_members'])
def make_some(message):
    bot.send_message(message.chat.id, 'Я добавил нового пользователя!')
    bot.approve_chat_join_request(message.chat.id, message.from_user.id)    
bot.infinity_polling(none_stop=True)
