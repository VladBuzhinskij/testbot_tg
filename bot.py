import telebot
import config
from telebot import types # для указание типов
import psycopg2
from psycopg2 import Error
from random import randint

tb = telebot.TeleBot(config.tok)

tb.set_my_commands([
    telebot.types.BotCommand("/start", "main menu")
    
])
# # добавление названия комнаты в таблицу пользователей
# def update_name_room_user_status (name_room,user_id,admin):
#     try:
#         print('+')
#         # Подключение к существующей базе данных
#         connection = psycopg2.connect(user=config.user,
#         # пароль, который указали при установке PostgreSQL
#         password=config.password,
#         host=config.host,
#         port=config.port,
#         database=config.database)
#         # Курсор для выполнения операций с базой данных
#         cursor = connection.cursor()        
#         if admin:
#             rename_room=name_room[:len(name_room)-1]+'1'
#         else:
#             rename_room=name_room[:len(name_room)-1]+'0'    
#         cursor.execute("Update users_status set name_room=%s where id_user=%s  ",      (rename_room,user_id))  
#         connection.commit()
#         cursor.close()
#         connection.close()
#         return 1
#     except (Exception, Error) as error:
#         print("Ошибка при работе с PostgreSQL", error)
#         print('21')
#         return 0

# # print (update_name_room_user_status ('pandas',12,False))

# def close_room (name_room):
#     try:
#         print('+')
#         # Подключение к существующей базе данных
#         connection = psycopg2.connect(user=config.user,
#         # пароль, который указали при установке PostgreSQL
#         password=config.password,
#         host=config.host,
#         port=config.port,
#         database=config.database)
#         # Курсор для выполнения операций с базой данных
#         cursor = connection.cursor()        
#         rename_room=name_room[:len(name_room)-1]+'1'   
#         cursor.execute("ALTER TABLE %s RENAME TO %s" %(name_room,rename_room))  
#         connection.commit()
#         cursor.close()
#         connection.close()
#         return 1
#     except (Exception, Error) as error:
#         print("Ошибка при работе с PostgreSQL", error)
#         print('21')
#         return 0

# def database_select_status (id):
#     try:
#         # Подключение к существующей базе данных
#         connection = psycopg2.connect(user=config.user,
#         # пароль, который указали при установке PostgreSQL
#         password=config.password,
#         host=config.host,
#         port=config.port,
#         database=config.database)
#         # Курсор для выполнения операций с базой данных
#         cursor = connection.cursor() 
#         user_id_select = "select status from users_status where id_user=%s"        
#         cursor.execute(user_id_select, (id,))  
#         user_status = cursor.fetchall()
        
#         print(user_status)
#         cursor.close()
#         connection.close()
#         if len(user_status)==0:
#             print('11')
#             return  1
#         else:
#             print('31')
#             return (user_status[0])[0]
#     except (Exception, Error) as error:
#         print("Ошибка при работе с PostgreSQL", error)
#         print('21')
#         return 0
    
# def database_insert_status (id,status):
#     try:
#         # Подключение к существующей базе данных
#         connection = psycopg2.connect(user=config.user,
#         # пароль, который указали при установке PostgreSQL
#         password=config.password,
#         host=config.host,
#         port=config.port,
#         database=config.database)
#         # Курсор для выполнения операций с базой данных
#         cursor = connection.cursor()   
#         cursor.execute("INSERT INTO users_status (id_user, status) VALUES (%s, %s)",      (id, status))
#         connection.commit()
#         count = cursor.rowcount
#         print (count, "Запись успешно добавлена ​​в таблицу ")
#         cursor.close()
#         connection.close()        
#         print('11')
#         return  1    
    
#     except (Exception, Error) as error:
#         print("Ошибка при работе с PostgreSQL", error)
        
#         print(id,status)
#         return 0        
   

def database_open_room (name_room):
    try:
        # Подключение к существующей базе данных
        connection = psycopg2.connect(user=config.user,
        # пароль, который указали при установке PostgreSQL
        password=config.password,
        host=config.host,
        port=config.port,
        database=config.database)
        # Курсор для выполнения операций с базой данных
        cursor = connection.cursor()   
        name_room=name_room[:len(name_room)-1]+'0'   
        cursor.execute("""SELECT  FROM %s;"""%name_room)
            
         
        res=cursor.fetchmany()
        print(res)
        cursor.close()
        connection.close()        
        print('11')
        return  "ok"    
    
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
        
        
        return error     

# def database_update_status (id,status):
#     try:
#         # Подключение к существующей базе данных
#         connection = psycopg2.connect(user=config.user,
#         # пароль, который указали при установке PostgreSQL
#         password=config.password,
#         host=config.host,
#         port=config.port,
#         database=config.database)
#         # Курсор для выполнения операций с базой данных
#         cursor = connection.cursor()   
#         cursor.execute("Update users_status set status=%s where id_user=%s  ",      (status,id))
#         connection.commit()
#         cursor.close()
#         connection.close()        
#         print('11')
#         return  True    
    
#     except (Exception, Error) as error:
#         print("Ошибка при работе с PostgreSQL", error)
        
#         print(id,status)
#         return False  



# def database_create_table (table_name):
#     try:
#         # Подключение к существующей базе данных
#         connection = psycopg2.connect(user=config.user,
#         # пароль, который указали при установке PostgreSQL
#         password=config.password,
#         host=config.host,
#         port=config.port,
#         database=config.database)
#         # Курсор для выполнения операций с базой данных
#         cursor = connection.cursor()   
#         # cursor.execute(("CREATE TABLE test (id int PRIMARY KEY, num int, data int  );"))
#         table_name=table_name[:len(table_name)-1]+'0'   
#         cursor.execute("CREATE TABLE %s (user_id int PRIMARY KEY, admin_status, gahalth BOOL, halth_id INT,charact BOOL, charact_id INT,bio BOOL, bio_id INT, add_inf BOOL, add_inf_id INT,fobias BOOL,fobias_id INT,hobby BOOL, hobby_id INT,prof BOOL, prof_id INT, admin BOOL,FOREIGN KEY (halth_id) REFERENCES halth(halth_id), FOREIGN KEY (charact_id) REFERENCES charact(charac_id),FOREIGN KEY (bio_id) REFERENCES bio(bio_id),FOREIGN KEY (add_inf_id) REFERENCES add_inf(add_inf_id),FOREIGN KEY (fobias_id) REFERENCES fobias(fobias_id),FOREIGN KEY (hobby_id) REFERENCES hobby(hobby_id),FOREIGN KEY (prof_id) REFERENCES prof(prof_id) );" %(table_name))
#         # cursor.execute(("ALTER TABLE test ADD CONSTRAINT fk FOREIGN KEY (num) REFERENCES system(id_t);"))
#         connection.commit()
#         cursor.close()
#         connection.close()        
#         print('11')
#         return  True    
    
#     except (Exception, Error) as error:
#         print("Ошибка при работе с PostgreSQL", error)
        
#         print(21)
#         return False


# def database_selected ():
#     try:
#         # Подключение к существующей базе данных
#         connection = psycopg2.connect(user=config.user,
#         # пароль, который указали при установке PostgreSQL
#         password=config.password,
#         host=config.host,
#         port=config.port,
#         database=config.database)
#         # Курсор для выполнения операций с базой данных
#         cursor = connection.cursor() 
       
#         cursor.execute("select bags from test JOIN system ON num = id_t   ")  
#         user_status = cursor.fetchall()
        
#         print(user_status)
#         cursor.close()
#         connection.close()
#         if len(user_status)==0:
#             print('11')
#             return  1
#         else:
#             print('31')
#             return (user_status[0])[0]
#     except (Exception, Error) as error:
#         print("Ошибка при работе с PostgreSQL", error)
#         print('21')
#         return 0
    
# def database_insert_room (id, name_room, admin):
#     try:
#         # Подключение к существующей базе данных
#         connection = psycopg2.connect(user=config.user,
#         # пароль, который указали при установке PostgreSQL
#         password=config.password,
#         host=config.host,
#         port=config.port,
#         database=config.database)
#         # Курсор для выполнения операций с базой данных
#         cursor = connection.cursor()  
#         halth_id=randint(1,30)
#         charact_id =randint(1,30)
#         bio_id=randint(1,30)
#         add_inf_id=randint(1,30)
#         fobias_id=randint(1,30)
#         hobby_id=randint(1,30)
#         prof_id=randint(1,50)
#         name_room=name_room[:len(name_room)-1]+'0'  
#         cursor.execute("INSERT INTO %s (user_id, amin_status, halth, halth_id,charact,charact_id, bio, bio_id, add_inf, add_inf_id, fobias, fobias_id, hobby, hobby_id, prof, prof_id,admin) VALUES (%s,%s,%s,FALSE, %s,FALSE,%s,FALSE,%s,FALSE,%s,FALSE,%s,FALSE, %s,FALSE,%s,%s)"    %( name_room,id,halth_id, charact_id,bio_id,add_inf_id,fobias_id,hobby_id,prof_id,admin))
#         connection.commit()
#         count = cursor.rowcount
#         print (count, "Запись успешно добавлена ​​в таблицу ")
#         cursor.close()
#         connection.close()        
#         print('11')
#         return  1    
    
#     except (Exception, Error) as error:
#         print("Ошибка при работе с PostgreSQL", error)
        
#         print(id)
#         return 0

# # print(database_selected())
# # print(database_create_table ('stat'))
# # print(database_insert_room (13, 'tests'))

# # print(database_update_status (100,3))
# # print(database_open_room ("bags"))
# # id=12

# # print(database_select_status (id))


# # sql = "SELECT table_name FROM information_schema.tables WHERE table_schema='public'"
# # cursor.execute(sql)
# # tables = cursor.fetchall()
    
   
  

        



bot = telebot.TeleBot(config.tok)

@bot.message_handler(commands=['start'])
def start(message):

    
    bot.send_message(message.chat.id, text="Hello")

@bot.message_handler(content_types=['text'])
def func(message):
    
        bot.send_message(message.chat.id, text=database_open_room (message.text))
    
        

#     # select=database_select_status(message.from_user.id)
#     # if select==1:
#     #     database_insert_status (message.from_user.id,2)
#     # select=database_select_status(message.from_user.id)
#     # if select==2: 
#     #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     #     btn1 = types.KeyboardButton("Зайти в комнату")
#     #     btn2 = types.KeyboardButton("Создать комнату")
#     #     markup.add(btn1, btn2)
       
#     #     bot.send_message(message.chat.id, text="Добро пожаловать", reply_markup=markup)
#     # elif select ==0:
#     #     bot.send_message(message.chat.id, text="Ошибка.Попробуйте еще раз")


    
# # @bot.message_handler(commands=['1'])
# # def stop_database(message):
# #     bot.send_message(message.chat.id, text="закрытие базы данных")


# @bot.message_handler(regexp='Зайти в комнату')
# def open_room(message):
#     select=database_select_status(message.from_user.id)
    
#     if select==2 and database_update_status (message.from_user.id,3):
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         btn1 = types.KeyboardButton("Назад")
#         markup.add(btn1)
#         bot.send_message(message.chat.id, text="Введите название комнаты:")
        
    
# @bot.message_handler(regexp='Создать комнату')
# def open_room(message):
#     select=database_select_status(message.from_user.id)
    
#     if select==2 and database_update_status (message.from_user.id,4):
#         bot.send_message(message.chat.id, text="Введите название комнаты:")


# @bot.message_handler(content_types=['text'])
# def func(message):
#     select=database_select_status(message.from_user.id)
#     if select==3 and message.text!='Назад':
#         if database_open_room (message.text):
#             if database_insert_room (message.from_user.id, message.text,False):
#                 if database_update_status (message.from_user.id,5):
#                     if update_name_room_user_status (message.text,message.from_user.id,False):
#                         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#                         btn1 = types.KeyboardButton("Начать игру")
#                         markup.add(btn1)
#                         bot.send_message(message.chat.id, text="Вы вошли в комнату "+ message.text)

#     elif select==4 and message.text!='Назад':
#         if database_create_table (message.text):
#             if database_insert_room (message.from_user.id, message.text,True):
#                 if database_update_status (message.from_user.id,6):
#                     if update_name_room_user_status (message.text,message.from_user.id,True):
#                         bot.send_message(message.chat.id, text="Вы создали комнату. Ожидайте начало игры "+ message.text)

# @bot.message_handler(regexp='Назад')
# def open_room(message):
#     select=database_select_status(message.from_user.id)
#     if select==3 or select==4:
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         btn1 = types.KeyboardButton("Зайти в комнату")
#         btn2 = types.KeyboardButton("Создать комнату")
#         markup.add(btn1, btn2)
#         database_insert_status (message.from_user.id,2)

# # bot.message_handler(regexp='Начать игру')
# # def open_room(message):
# #     select=database_select_status(message.from_user.id)
# #     if select==6:
        





            
        







# # @bot.message_handler(content_types=['text'])
# # def func(message):
# #     if(message.text == "👋 Поздороваться"):
# #         bot.send_message(message.chat.id, text="Привеет.. Спасибо что читаешь статью!)")
# #     elif(message.text == "❓ Задать вопрос"):
# #         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
# #         btn1 = types.KeyboardButton("Как меня зовут?")
# #         btn2 = types.KeyboardButton("Что я могу?")
# #         back = types.KeyboardButton("Вернуться в главное меню")
# #         markup.add(btn1, btn2, back)
# #         bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)
    
# #     elif(message.text == "Как меня зовут?"):
# #         bot.send_message(message.chat.id, "У меня нет имени..")
    
# #     elif message.text == "Что я могу?":
# #         bot.send_message(message.chat.id, text="Поздороваться с читателями")
    
# #     elif (message.text == "Вернуться в главное меню"):
# #         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
# #         button1 = types.KeyboardButton("👋 Поздороваться")
# #         button2 = types.KeyboardButton("❓ Задать вопрос")
# #         markup.add(button1, button2)
# #         bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
# #     else:
# #         bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")

bot.polling(none_stop=True)



# # import telebot
# # from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# # token='6072913589:AAHgdsCMX0erjBeUmEeSOu5aRO0KhVjZ3-Y'
# # bot=telebot.TeleBot(token)


# # @bot.message_handler(text= ' start')
# # def function_name(message):
# # 	bot.reply_to(message, "This is a message handler")
    


bot.infinity_polling()

