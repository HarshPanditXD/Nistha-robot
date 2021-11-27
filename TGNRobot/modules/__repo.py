import os
from pyrogram import Client, filters
from pyrogram.types import *

from TGNRobot.conf import get_str_key
from TGNRobot import pbot

REPO_TEXT = "**A Powerful [BOT](t.me/Nistha_robot) to Make Your Groups Secured and Organized ! \n\n↼ Øwñêr ⇀ : 『 [𝗛𝗮𝗿𝘀𝗵](t.me/Proud_of_Indian) 』\n╭──────────────\n┣─ » Python ~ 3.8.6\n┣─ » Update ~ Recently\n╰──────────────\n\n»»» 😈🇮🇳😈🇮🇳😈 «««"
  
BUTTONS = InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("⚡ ʀᴇᴘᴏꜱɪᴛᴏʀᴇᴍ🔥", url=f"http://github.com/TEAM-BLAZ/BLAZE-SPAMMER-ROBOT"),
      ],[
        InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ ⚡", url="https://t.me/The_Secret_worlds"),
      ]]
    )
  
  
@pbot.on_message(filters.command(["repo"]))
async def repo(pbot, update):
    await update.reply_text(
        text=REPO_TEXT,
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )
