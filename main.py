from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
from id_bot import id_bot as api

bot = Bot(api.bot)
dp = Dispatcher(bot)
sti = 'CAACAgIAAxkBAAEGNZdjWXnu4KTX3oGTRnt6mxm5b4HbQQACIRQAAiHvyUvdPulOAgvvMSoE'


@dp.message_handler(commands=['start'])
async def start(massage: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть веб страницу', web_app=WebAppInfo(
        url='https://maksimd31.github.io/tg_bot/')))
    await massage.answer('Привет <b>Dungeon Master</b>', reply_markup=markup,parse_mode='HTML')
    await bot.send_sticker(massage.from_user.id, sti)


@dp.message_handler(commands=['give'])
async def start(massage: types.Message):
    await bot.send_sticker(massage.from_user.id, sti)


# # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    executor.start_polling(dp)

#     pass
