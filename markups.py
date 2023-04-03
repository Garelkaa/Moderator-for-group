from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import cfg as cfg

btnUrlChannel = InlineKeyboardButton(text="Перейти на канал", url=cfg.CHANNEL_URL)
channelMenu = InlineKeyboardMarkup(row_width=1)
channelMenu.insert(btnUrlChannel)