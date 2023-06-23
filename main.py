from aiogram import Bot,Dispatcher,executor,types
import openai

bot = Bot('6298269361:AAFIGkSiJ4dJmxbo25dThuF3pa9bx8GyBPc')
openai.api_key = ''
dp = Dispatcher(bot)

@dp.message_handler(commands=['start']):
async def start(message: types.Message):
    await message.answer('Hello, I am ChatGPT3 and I can speak with you.Just write me any words')

@dp.message_handler()
async def sens(message: types.Message):
    response = openai.Completion.create(
    model = "text-davinci-002",
    prompt = message.text,
    temperature = 0.9,
    max_tokens = 1000,
    top_p = 1.0,
    frequency_penalty = 0.0,
    presence_penalty = 0.6,
    stop = ["You:"]
    )

    await message.answer(response['choices'][0]['text'])

executor.start_polling(dp)
