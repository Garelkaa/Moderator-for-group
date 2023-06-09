from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
import os
from aiogram.types import ContentType
import cfg
from aiogram.dispatcher.filters import BoundFilter

bot = Bot(token=cfg.TOKEN)
dp = Dispatcher(bot)

class IsAdminFilter(BoundFilter):
    key = "is_admin"

    def __init__(self, is_admin):
        self.is_admin = is_admin

    async def check(self, message: types.Message):
        member = await message.bot.get_chat_member(message.chat.id, message.from_user.id)
        return member.is_chat_admin()