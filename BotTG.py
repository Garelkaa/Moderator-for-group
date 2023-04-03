import logging
from create_bot import bot, dp
from aiogram import executor, types
import markups as nav
import cfg as cfg

from create_bot import IsAdminFilter

dp.filters_factory.bind(IsAdminFilter)


@dp.message_handler(content_types=["new_chat_members"])
async def user_joined(message: types.Message):
    await message.answer("Здравствуйте!", reply_markup=nav.channelMenu)

@dp.message_handler(content_types=["left_chat_member"])
async def left_chat(message: types.Message):
    await message.delete()


@dp.message_handler(is_admin=True, commands=["ban"], commands_prefix="!/")
async def ban(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Надо ответить на сообщение!")
        return
    
    await message.bot.delete_message(cfg.GROUP_ID, message.message_id)
    await message.bot.ban_chat_member(chat_id=cfg.GROUP_ID, user_id=message.reply_to_message.from_user.id)
    await message.reply_to_message.reply('Пользователь в бане')

@dp.message_handler(is_admin=True, commands=["kick"], commands_prefix="!/")
async def kick(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Надо ответить на сообщение!")
        return
    
    await message.bot.delete_message(cfg.GROUP_ID, message.message_id)
    await message.bot.kick_chat_member(chat_id=cfg.GROUP_ID, user_id=message.reply_to_message.from_user.id)
    await message.reply_to_message.reply('Пользователь кикнут\n xD')

@dp.message_handler(content_types=['text'])
async def filter_message(message: types.Message):

    text = message.text.lower()
    for word in cfg.WORDS:
        if word in text:
            await message.delete()
            await message.answer("Упом/Оск родни незя")

    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
