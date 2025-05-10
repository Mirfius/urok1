from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Токен вашего бота (получите у BotFather)
API_TOKEN = '6403405667:AAEF8AQPPRDHyRkHQb-y3mjpLxpJ0odmofg'

# Создаем экземпляры бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Это простой бот. Введите /help, чтобы увидеть доступные команды.")

# Обработчик команды /help
@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.reply("Доступные команды:\n/start - приветствие\n/help - список команд")
    await bot.send_message(message.chat.id, text="😡")

@dp.message_handler()  ##  commands=['start']
async def start(message: types.Message):  #  асинхронно запускаем
    if message.text=='foto':
        await bot.send_photo(chat_id=message.chat.id,photo = "https://yrokiwp.ru/wp-content/uploads/2023/02/how-to-identify-fake-websites-2.png")
    else:
        await message.reply(text="Доступные команды:\n/start - приветствие\n/help - список команд")  # ответ




# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
