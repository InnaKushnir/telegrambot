from functools import partial

import openai
import asyncio
#from aiogram.dispatcher.filters import Command
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.types import Message

# from core.handlers.basic import get_start

BOT_TOKEN = "6053856757:AAGdf0i56NkCU67GAuUWkoVFcnHmZXODEOM"
text_ = "Hello! How are you?"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message_handler(commands=["chat"])
async def handle_user_message(message: Message, bot: Bot):
    user_message = message.text
    response_text = await process_user_message(user_message)
    await bot.send_message(message.from_user.id, response_text)


async def start_bot(bot: Bot):
    await bot.send_message(417193906, "Run bot!")


async def stop_bot(bot: Bot):
    await bot.send_message(417193906, "Stop bot!")


async def send_message_to_users(bot: Bot = Bot(token=BOT_TOKEN)):
    with open("user.txt", "r") as file:
        users = file.readlines()

    for user_id in users:
        try:
            text__ = "Це повідомлення буде надіслано всім підписаним користувачам"
            await bot.send_message(chat_id=user_id, text=text__)
            await asyncio.sleep(0.1)
        except Exception as e:
            print(f"Failed to send message to user {user_id}. Error: {str(e)}")


async def process_user_message(message_text):

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=message_text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5
    )

    response.choices[0].text.strip()
    await message_text.reply(f"{response}")


@dp.message_handler(commands=["chat"])
async def handle_user_message(message: Message, bot: Bot):
    user_message = message.text
    response_text = await process_user_message(user_message)
    await bot.send_message(message.from_user.id, response_text)


async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f"Hello! {message.from_user.first_name} !!!!")
    #await message.answer(f"Hello! {message.from_user.first_name} !!!!")
    #await message.reply(f"Hello! {message.from_user.first_name} !!!!")


async def start():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    #dp.message.register(get_start)
    dp.message.register(handle_user_message)
    dp.startup.register(send_message_to_users)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
if __name__ == '__main__':
    asyncio.run(start())













#gpt_chat_token= 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

# new_network_python_bot
#
# 6053856757:AAGdf0i56NkCU67GAuUWkoVFcnHmZXODEOM
#
# BOT_NUMBER = 6053856757
# BOT_TOKEN = AAGdf0i56NkCU67GAuUWkoVFcnHmZXODEOM