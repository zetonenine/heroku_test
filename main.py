import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from postgresql import BD
# import redis


logging.basicConfig(level=logging.INFO)

bot = Bot(token='1233194283:AAEltBBA7sqZ7HPo5Gxef5fALXiqhyRwBqk')

dp = Dispatcher(bot, storage=RedisStorage2(host='ec2-54-86-106-10.compute-1.amazonaws.com', port=24019, password='pdf629fb003d877580494432330091be688b8366c113b0c062d56d7d742932cc1'))
# dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

# r = redis.Redis(db=5)


@dp.message_handler(state=None, commands='start')
async def starting(message: types.Message):
    db.create()
    await message.answer('Привет!')

    
@dp.message_handler(state=None, commands='add')
async def starting(message: types.Message):
    db.add_user(message.from_user.id)
    await message.answer('Добавил!')
    
    
@dp.message_handler(state=None, commands='check')
async def starting(message: types.Message):
    obj = db.user_exists(message.from_user.id)
    await message.answer(obj)
    

@dp.message_handler(content_types=['text'])
async def hey(message: types.Message):
    await message.answer(message.text)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
