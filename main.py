from config import tok
from aiogram import Bot, Dispatcher, executor, types
import requests
from datetime import datetime



req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
response = req.json()
sell_price = response["btc_usd"]["sell"]
current_cost = f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nЦена продажи биткойна на текущий момент: {sell_price}"



bot = Bot(token=tok)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message:types.Message):
    await message.reply('Привет, напиши следующую команду, чтобы посмотреть текущую цену на биткойн: /price')


@dp.message_handler(commands=['price'])
async def show_the_fucking_price(message:types.Message):
    await message.reply(current_cost)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)