from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
from id_bot import id_bot as api

bot = Bot(api.bot)
dp = Dispatcher(bot)

executor.start_polling(dp)


@dp.message_handlers(commands=['start'])
async def start(massage: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButtonPollType('Открыть веб страницу', web_app=WebAppInfo(
        url='https://github.com/maksimd31/tg_bot/blob/master/index.html')))
    await massage.answer('Привет', reply_markup=markup)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass
