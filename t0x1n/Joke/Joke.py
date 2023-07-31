from config import tg_bot_token # импорт токена бота
from randomejoke import lst # импорт списка ответов
from aiogram import Bot, types, Dispatcher, executor # импорт бота и нужностей 
import random # импорт рандомайзера

bot = Bot(token=tg_bot_token) # токен бота берём в переменную
dp = Dispatcher(bot) # делаем короткий вызов функций бота с токеном

@dp.message_handler() # обьявляем функцию
async def echo_message(msg: types.Message): # асинхронная функция срабатывающая при поступлении сообщения
        alst = random.choices(lst) # выбираем рандомный ответ
        aalst = str(alst)[2:-2] # форматируем рандомный ответ (убираем по 2 лишних символа [' '])
        await bot.send_message(msg.from_user.id, aalst) # отправляем в личку написавшему сгенерированный и отформатированный ответ

if __name__ == '__main__':
    executor.start_polling(dp) # повторять безконца 
    