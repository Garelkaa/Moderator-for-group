from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import cfg as cfg

btnUrlChannel = InlineKeyboardButton(text="textButton", url=cfg.CHANNEL_URL)
channelMenu = InlineKeyboardMarkup(row_width=1)
channelMenu.insert(btnUrlChannel)
