import mysql.connector,json,codecs
from aiogram.types import user
from mysql.connector import Error
from mysql.connector.optionfiles import read_option_files
from config import *

class sqlz:

    def __init__(self,db_host,user_name,user_password,db_name ):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = mysql.connector.connect(
                host = db_host,
                user = user_name,
                passwd = user_password,
                database = db_name
            )
        self.cursor = self.connection.cursor()
        self.anime_db_message = ''

    def get_followers(self, status = True):
        mass = []
        """Получаем всех активных подписчиков бота"""
        self.cursor.execute('''SELECT * FROM `users` WHERE `status` = {}'''.format(status))
        results = self.cursor.fetchall()
        for row in results:
            print(row[1])
            mass.append(row[1])
        print(mass)
        return results


    def add_follower(self,user_id,status):
        self.cursor.execute('''INSERT INTO `users` (user_id, status )
                            SELECT * FROM (SELECT '{user_id}','{status}') AS tmp
                            WHERE NOT EXISTS (SELECT user_id FROM `users` WHERE user_id = '{user_id}') LIMIT 1;'''.format(user_id = user_id,status = status))
        self.cursor.execute("UPDATE `users` SET `status` = {} WHERE `user_id` = {}".format(status, user_id))
        self.connection.commit()

    def update_follower(self, user_id, status):
        """Обновляем статус подписки пользователя"""
        self.cursor.execute("UPDATE `users` SET `status` = {} WHERE `user_id` = {}".format(status, user_id))
        self.connection.commit()

   
    def database_top(self):
        self.cursor.execute(" SELECT `name` FROM `animes`  ")
        results = self.cursor.fetchall()
        anime_mass = []
        count = 0
        for i in results:
            x = ''.join(i)
            anime_mass.append(x)
        
        for anime in anime_mass:
            count+=1
            self.anime_db_message = self.anime_db_message + anime + '\n'
        
        return self.anime_db_message
       

    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()




db =sqlz(
		db_config["mysql"]["host"], 
		db_config["mysql"]["user"], 
		db_config["mysql"]["pass"],
		db_config["mysql"]["db_name"]
		)
