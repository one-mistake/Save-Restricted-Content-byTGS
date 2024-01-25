import pyrogram
from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant, InviteHashExpired, UsernameNotOccupied
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import Message

import time
import os
import threading
import json

with open('config.json', 'r') as f: DATA = json.load(f)
def getenv(var): return os.environ.get(var) or DATA.get(var, None)

bot_token = getenv("TOKEN") 
api_hash = getenv("HASH") 
api_id = getenv("ID")
# bot = Client("mybot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)
bot = pyrogram.Bot(token=bot_token)
CHANNEL_ID = -1001639497734

ss = getenv("STRING")
if ss is not None:
	acc = Client("myacc" ,api_id=api_id, api_hash=api_hash, session_string=ss)
	acc.start()
else: acc = None

# Define the handler function
@bot.message_handler(filters.command(["start"]))
def start(client, message):
    # Check if the user is already in the channel
    if message.from_user.id not in get_channel_members(bot, CHANNEL_ID):
        # If not, reply with the join link
        bot.send_message(
            chat_id=message.chat.id,
            text=f"Please join our channel: ",
        )
    else:
        # If the user is already in the channel, proceed with the bot's functionality
        bot.send_message(
            chat_id=message.chat.id,
            text="Hello, welcome to our bot!",
        )
        
def get_channel_members(bot, channel_id):
    members = []
    offset_id = None
    while True:
        result = bot.get_chat_members(channel_id, limit=100, offset=offset_id)
        members.extend(result.users)
        if not result.next_offset:
            break
        offset_id = result.next_offset
    return [member.id for member in members]


# Start the bot
bot.run()