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
bot = Client("mybot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)
CHANNEL_USERNAME = "HackingCraze24_7d"

ss = getenv("STRING")
if ss is not None:
	acc = Client("myacc" ,api_id=api_id, api_hash=api_hash, session_string=ss)
	acc.start()
else: acc = None

# Define the handler function
@ bot.on_message(filters.command(["start"]))
def start_command(client, message):
    user_id = message.from_user.id
    channel_id = client.get_chat_member(chat_id=CHANNEL_USERNAME, user_id=user_id)

    # Check if the user is a member of the channel
    try:
        member = client.get_chat_member(chat_id=CHANNEL_USERNAME, user_id=user_id)
        if member in ["member", "administrator", "creator"]:
            channel_id = member.chat.id
    except Exception as e:
        print(f"Error: {e}")

    # If the user is a member, proceed; otherwise, ask them to join
    if channel_id:
        message.reply_text("You are a member of the channel. You can proceed.{member}")
    else:
        message.reply_text("You must join the channel to proceed.{member}")


# Start the bot
bot.run()