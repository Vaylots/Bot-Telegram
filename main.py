import config, asyncio,logging,random,time,datetime
from aiogram.types import message
from aiogram.types.base import T
from config import db_config
from aiogram import * 
from aiogram.dispatcher.filters import Text
from aiogram.types import * 
from anime import *
from sqlz import sqlz
from parsingweek import *



# Инициализируем соединение с БД

db =sqlz(
		db_config["mysql"]["host"], 
		db_config["mysql"]["user"], 
		db_config["mysql"]["pass"],
		db_config["mysql"]["db_name"]
		)

		

# задаем уровень логов
logging.basicConfig(level = logging.INFO)

# Инициализируем бота
bot = Bot(token = config.API_TOKEN)
dp = Dispatcher(bot)


#Добавляем стартовую клавиатуру
keyboard_start = ReplyKeyboardMarkup(resize_keyboard = True) 
# Добавляем кнопки в стартовую клавиатуру
keyboard_start_buttons = ['Список команд']
keyboard_start.add(*keyboard_start_buttons)


today = datetime.datetime.today()
weekday = 1 + today.weekday()



async def mailing(wait_for):
	while True:
		await asyncio.sleep(wait_for)
		followers = db.get_followers()
		print(followers)
		for s in followers:
			print(s)
			if weekday == 1:
				try:
					print(parsing_monday())
					await bot.send_message(s[1],text = 'Сегодня вышли такие аниме: \n {} '.format(parsing_monday()))
				except:
					pass			
			elif weekday == 2:
				try:
					print(parsing_tuesday())
					await bot.send_message(s[1],text = 'Сегодня вышли такие аниме: \n {} '.format(parsing_tuesday()))
				except:
					pass
			elif weekday == 3:
				try:
					print(parsing_wednesday())
					await bot.send_message(s[1],text = 'Сегодня вышли такие аниме: \n {} '.format(parsing_wednesday()))
				except:
					pass
			elif weekday == 4:
				try:
					print(parsing_thursday())
					await bot.send_message(s[1],text = 'Сегодня вышли такие аниме: \n {} '.format(parsing_thursday()))
				except:
					pass			
			elif weekday == 5:
				try:
					print(parsing_friday())
					await bot.send_message(s[1],text = 'Сегодня вышли такие аниме: \n {} '.format(parsing_friday()))
				except:	
					pass
			elif weekday == 6:
				try:
					print(parsing_saturday())
					await bot.send_message(s[1],text = 'Сегодня вышли такие аниме: \n {} '.format(parsing_saturday()))
				except:
					pass			
			elif weekday == 6:
				try:
					print(parsing_sunday())
					await bot.send_message(s[1],text = 'Сегодня вышли такие аниме: \n {} '.format(parsing_sunday()))
				except:
					pass



# Создаем ответ на стартовую команду
@dp.message_handler(commands = ['start'])
async def start_message(Message): 
	await bot.send_message(Message.from_user.id,text = 'Привет,это бот студента ИС-2/19, Кондратьева Максима.',reply_markup=keyboard_start)

@dp.message_handler(text="Список команд")
async def command_list(Message):
	keyboard_menu = InlineKeyboardMarkup()

	key_menu_follow = InlineKeyboardButton(text = 'Меню подписки на рассылку', callback_data = 'follow_menu')
	keyboard_menu.add(key_menu_follow)

	key_anime_help = InlineKeyboardButton(text = 'Что посоветуешь посмотреть?', callback_data = 'Anime-help' )
	keyboard_menu.add(key_anime_help)

	key_top = InlineKeyboardButton(text = 'Топ Аниме', callback_data = 'TopAnime')
	keyboard_menu.add(key_top)

	await bot.send_message(Message.from_user.id, text = 'Привет, вот список доступных команд на данный момент', reply_markup = keyboard_menu)



@dp.callback_query_handler(text='follow_menu')
async def keyboard_menu_follow(Message):
	keyboard_menu_follow = InlineKeyboardMarkup()

	key_follow = InlineKeyboardButton(text = "Подписаться на рассылку", callback_data = 'follow')
	keyboard_menu_follow.add(key_follow)

	key_unfollow = InlineKeyboardButton(text = "Отписаться от рассылки", callback_data = 'unfollow')
	keyboard_menu_follow.add(key_unfollow)

	await bot.send_message(Message.from_user.id,text = 'Меню подписки на рассылку', reply_markup = keyboard_menu_follow)


# Команда активации подписки 
@dp.callback_query_handler(text="follow")
async def follow(Message):
	db.add_follower(Message.from_user.id,True)
	await Message.answer('Вы успешно подписались на рассылку! ')


# Команда отключения подписки 
@dp.callback_query_handler(text="unfollow")
async def unfollow(Message):
	db.update_follower(Message.from_user.id,False)
	await Message.answer('Вы успешно отписались от рассылки! ')


@dp.callback_query_handler(text="Anime-help")
async def Anime_help(Message):
		
	keyboard_animes = types.InlineKeyboardMarkup()

	key_jobless = types.InlineKeyboardButton(text="Реинкарнация безработного", callback_data='Jobless')
	keyboard_animes.add(key_jobless)

	key_AOT = types.InlineKeyboardButton(text="Атака титанов",callback_data='AoT')
	keyboard_animes.add(key_AOT)

	key_Horimia = types.InlineKeyboardButton(text="Хоримия", callback_data='Horimia')
	keyboard_animes.add(key_Horimia)

	await bot.send_message(Message.from_user.id,text = 'Советую посмотреть аниме:', reply_markup=keyboard_animes)


@dp.callback_query_handler(text = 'Jobless')
async def Jobless_anime(Message):
	Description = Jobless['Description']
	Trailer = Jobless['Trailer']
	await bot.send_message(Message.from_user.id,Trailer)
	await bot.send_message(Message.from_user.id,Description)


@dp.callback_query_handler(text = 'Horimia')
async def Attack_On_Titan(Message):
	Description = Horimia['Description']
	Trailer = Horimia['Trailer']
	await bot.send_message(Message.from_user.id, Trailer)
	await bot.send_message(Message.from_user.id, Description)

	
@dp.callback_query_handler(text = 'AoT')
async def Attack_On_Titan(Message):
	Description = AoT['Description']
	Trailer = AoT['Trailer']
	await bot.send_message(Message.from_user.id, Trailer)
	await bot.send_message(Message.from_user.id, Description)
	

@dp.callback_query_handler(text = 'TopAnime')
async def Top_anime(Message):
	await bot.send_message(Message.from_user.id,text = 'Топ аниме: \n' + db.database_top())


if __name__ == '__main__':
	loop = asyncio.new_event_loop()
	asyncio.set_event_loop(loop)
	loop.create_task(mailing(10))
	executor.start_polling(dp, skip_updates = True)