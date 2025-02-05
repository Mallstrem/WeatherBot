import asyncio

from aiogram import Bot, Dispatcher, Router, types
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.enums import ParseMode
from aiogram.utils.markdown import hbold
from aiogram.client.session.aiohttp import AiohttpSession

from data.token import bot_token, id_token
from weather import get_today_weather

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"start weather monitorung")


async def start_bot() -> None:
    bot = Bot(bot_token, parse_mode=ParseMode.HTML)

async def get_weather() -> None:
    cur_weather = await get_today_weather()
    message_txt = ''
    message_txt = message_txt + 'Максимальная температура: ' + str(cur_weather['tempmax']) + '°C 🌡\n'
    message_txt = message_txt + 'Минимальная температура: ' + str(cur_weather['tempmin']) + '°C 🌡\n'
    message_txt = message_txt + 'Вероятность выпадения осадков: ' + str(cur_weather['precipprob']) + '%\n'
    message_txt = message_txt + 'Вид осадков: '
    if cur_weather['preciptype'] == None:
        message_txt = message_txt + 'нет осадков'
    else:
        for el in cur_weather['preciptype']:
            if el == 'rain':
                message_txt = message_txt + 'Дождь 🌧  '
            if el == 'snow':
                message_txt = message_txt + 'Снег 🌨  '
            if el == 'storm':
                message_txt = message_txt + 'Гроза 🌩  '
            if el not in ('rain', 'snow', 'storm'):
                message_txt = message_txt + 'Новый вид осадков: ' + el
    message_txt = message_txt + '\n'
    message_txt = message_txt + 'Снег: ' + str(cur_weather['snow']) + ' ❄️\n'
    message_txt = message_txt + 'Глубина снега: ' + str(cur_weather['snowdepth']) + 'мм ⛄️\n'
    message_txt = message_txt + 'Порыв ветра: ' + str(cur_weather['windgust']) + ' 💨\n'
    message_txt = message_txt + 'Скорость ветра: ' + str(cur_weather['windspeed']) + 'м/с 💨\n'
    message_txt = message_txt + 'Давление: ' + str(cur_weather['pressure']) + 'мм рт ст 🌡\n'
    message_txt = message_txt + 'Облачность: ' + str(cur_weather['cloudcover']) + ' ☁️\n'
    message_txt = message_txt + 'UV-индекс: ' + str(cur_weather['uvindex']) + ' ☀️\n'
    message_txt = message_txt + 'Описание: ' 
    if 'Overcast' in cur_weather['conditions']:
        message_txt = message_txt + 'Облачно ☁️  '
    if 'Rain' in cur_weather['conditions']:
        message_txt = message_txt + 'Дождь 🌧  '
    if 'Snow' in cur_weather['conditions']:
        message_txt = message_txt + 'Снег 🌨  '
    if 'cloudy' in cur_weather['conditions']:
        message_txt = message_txt + 'Облачность ☁️  '
    message_txt = message_txt + '   Неизвестная погода ' +  cur_weather['conditions']
    message_txt = message_txt + '\n'
    message_txt = message_txt + 'Дополнительно: ' + str(cur_weather['description']) + '\n'

    session = AiohttpSession()
    bot = Bot(bot_token, session=session)
    await bot.send_message(id_token, message_txt)
    await bot.session.close()

async def take_umberella() -> None:
    cur_weather = await get_today_weather()
    message_txt = ''
    if cur_weather['preciptype']:
        if ((cur_weather['precipprob'] > 0) or ('rain' in cur_weather['preciptype'])):
            message_txt += 'Возьми с собой зонт ☂️ \n'
        if 'snow' in cur_weather['preciptype']:
            message_txt += 'Там снег 🌨 \n'
    if cur_weather['windgust'] > 10:
        message_txt += 'Там сильный ветер 💨 \n'
    if cur_weather['uvindex'] >= 3:
        message_txt += 'Возьми с собой солнцезащитные очки 🕶 \n'
    if cur_weather['uvindex'] >= 3 and cur_weather['uvindex'] <= 5:
        message_txt += 'SPF 15 🧴 \n'
    if cur_weather['uvindex'] > 5:
        message_txt += 'SPF 50 🧴 \n'
    bot = Bot(bot_token)
    await bot.send_message(id_token, message_txt)
    await bot.session.close()