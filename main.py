#!/usr/bin/env python3

import pyrogram as pyro
from pyrogram import Client as PyroClient, filters as PyroFilters
from pyrogram.errors import UserAlreadyParticipant as PyroUserAlreadyParticipant, InviteHashExpired as PyroInviteHashExpired, UsernameNotOccupied as PyroUsernameNotOccupied
from pyrogram.types import InlineKeyboardMarkup as PyroInlineKeyboardMarkup, InlineKeyboardButton as PyroInlineKeyboardButton
from pyrogram.types import Message as PyroMessage

import time
import os
import threading
import json

with open('config.json', 'r') as f: DATA = json.load(f)
def getenv(var): return os.environ.get(var) or DATA.get(var, None)

bot_token = getenv("TOKEN") 
api_hash = getenv("HASH") 
api_id = getenv("ID")
bot = PyroClient("mybot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)
CHANNEL_USERNAME = "HackingCraze24_7d"

ss = getenv("STRING")
if ss is not None:
	acc = PyroClient("myacc" ,api_id=api_id, api_hash=api_hash, session_string=ss)
	acc.start()
else: acc = None

# Define the handler function
@ bot.on_message(PyroFilters.command(["start"]))
def start_command(client, message):
    user_id = message.from_user.id
    channel_id = None

    # Check if the user is a member of the channel
    try:
        member = client.get_chat_member(chat_id=CHANNEL_USERNAME, user_id=user_id)
        if member.status in ["member", "administrator", "creator"]:
            channel_id = member.chat.id
    except Exception as e:
        print(f"Error: {e}")

    # If the user is a member, proceed; otherwise, ask them to join
    if channel_id:
        message.reply_text("You are a member of the channel. You can proceed.")
    else:
        message.reply_text("You must join the channel to proceed.")

# Start the bot
bot.run()