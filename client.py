import requests
import json
import subprocess
from pyrogram.types.messages_and_media import message
import helper
from pyromod import listen
from pyrogram.types import Message
import tgcrypto
import pyrogram
from pyrogram import Client, filters
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import asyncio
from pyrogram.errors import FloodWait
import time
from pyrogram.types import User, Message
from p_bar import progress_bar
import subprocess
from subprocess import getstatusoutput
import logging
import os
import sys
from get_video_info import get_video_attributes, get_video_thumb
import re
from pyrogram import Client as bot
DEF_FORMAT = "480"
from dotenv import load_dotenv
load_dotenv()
os.makedirs("./downloads", exist_ok=True)
AUTH_USERS = 1112773045
sudo_users = [-1112773045]

class Bot(Client):   
    def __init__(self):
        super().__init__(   
           "bot",
            bot_token=os.environ.get("BOT_TOKEN"),
            api_id=int(os.environ.get("API_ID")),
            api_hash=os.environ.get("API_HASH")) 
            
    async def start(self):                        
        print("⚡ Bot Started ⚡")   
    async def stop(self, *args):
        await super().stop()
    async def exec(cmd):
        return proc.returncode,stderr.decode()
     
    @bot.on_message(filters.command(["start"]))
    async def account_login(bot: Client, m: Message):
        editable = await m.reply_text("**Pradhan this side send /down download and for classplus send /cpd  for /dhurina for /vision**")
    
