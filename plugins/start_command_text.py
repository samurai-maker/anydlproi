from pyrogram import Client, filters, StopPropagation
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import time
bot_start_time = time.time()



@Client.on_message(filters.command(["start"]), group=-2)
async def start(client, message):
    bot_uptime = time.strftime("%Hh %Mm %Ss", time.gmtime(time.time() - bot_start_time)) 
    joinButton = InlineKeyboardMarkup( [
                [
                    InlineKeyboardButton("мσνιє яєqυєѕт gяσυρ 📲", url="https://t.me/WORLD_WIDE_MOVIES")],
                    [InlineKeyboardButton("➕ ѕнαяє мє ➕", url="https://telegram.me/share/url?url=%20t.me/wwm_rename_bot")
                ]
            ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\nThis is Multipurpose Bot of @world_wide_movies.\n\n /help for More info \n Bot Uptime : {bot_uptime}"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
