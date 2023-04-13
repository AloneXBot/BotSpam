from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message

from Data import Data
from LegendGirl.Config import *

from ..core.clients import *


@Client.on_message(filters.command(["help"], prefixes=HANDLER))
async def help(Legend: Client, message: Message):
    HELP_MSG = "Help Menu Powered By @kimjikoinsupport"
    if ".jpg" in HELP_PIC or ".png" in HELP_PIC:
        await Legend.send_photo(
            message.chat.id,
            HELP_PIC,
            caption=HELP_MSG,
            reply_markup=InlineKeyboardMarkup(Data.HELP_MENU1),
        )
    elif ".mp4" in HELP_PIC.lower():
        await Legend.send_video(
            message.chat.id,
            HELP_PIC,
            caption=HELP_MSG,
            reply_markup=InlineKeyboardMarkup(Data.HELP_MENU1),
        )
    else:
        await Legend.send_message(
            message.chat_id,
            HELP_MSG,
            reply_markup=InlineKeyboardMarkup(Data.HELP_MENU1),
        )
