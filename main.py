import os
from pyrogram.enums import ChatMemberStatus, ChatMembersFilter
from pyrogram import enums
from pyrogram.types import ChatMember
import asyncio
import logging
import tgcrypto
from pyromod import listen
from config import *
import logging
from tglogging import TelegramLogHandler
from aiohttp import web
# Config 
class Client(bot):
             bot_token= "5323421782:AAFMaCslkGl5adfv7SkZ5_2jICXtkgXLL1k",
             api_id= 15178129,
             api_hash= "274a1c7f7ea99a473c6bd8facebc59ed")
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    SESSIONS = "./SESSIONS"

    AUTH_USERS = os.environ.get('AUTH_USERS', '1905890740, 5291627920').split(',')
    for i in range(len(AUTH_USERS)):
        AUTH_USERS[i] = int(AUTH_USERS[i])

    GROUPS = os.environ.get('GROUPS', '-1002080235700').split(',')
    for i in range(len(GROUPS)):
        GROUPS[i] = int(GROUPS[i])

    LOG_CH = -1001652082524
    PORT = 8080
# TelegramLogHandler is a custom handler which is inherited from an existing handler. ie, StreamHandler.
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        TelegramLogHandler(
            token=Config.BOT_TOKEN, 
            log_chat_id= Config.LOG_CH, 
            update_interval=2, 
            minimum_lines=1, 
            pending_logs=200000),
        logging.StreamHandler()
    ]
)

LOGGER = logging.getLogger(__name__)
LOGGER.info("live log streaming to telegram.")


# Store
class Store(object):
    CPTOKEN = "eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6ODU0ODUyMzIsIm9yZ0lkIjo2MzA0OCwidHlwZSI6MSwibW9iaWxlIjoiOTE5OTI1ODU1MzE2IiwibmFtZSI6IlBBTktBSiBCQVJJQSIsImVtYWlsIjoicGJhcmlhMzE4QGdtYWlsLmNvbSIsImlzSW50ZXJuYXRpb25hbCI6MCwiZGVmYXVsdExhbmd1YWdlIjoiRU4iLCJjb3VudHJ5Q29kZSI6IklOIiwiY291bnRyeUlTTyI6IjkxIiwidGltZXpvbmUiOiJHTVQrNTozMCIsImlzRGl5IjpmYWxzZSwib3JnQ29kZSI6ImpwY3p6IiwiZmluZ2VycHJpbnRJZCI6ImI0MDQwMWU0OTIxZjNiMGZhYzMzNjk0NzA1MWUyIiwiaWF0IjoxNjk3OTEzOTM2LCJleHAiOjE2OTg1MTg3MzZ9.ZisDykPc1stARemQi1sybuc5VHw0eGuwus0Vy7fJtXgYKcmkhR_hropXWBIULKBA"
    SPROUT_URL = "https://discuss.oliveboard.in/"
    ADDA_TOKEN = ""
    THUMB_URL = "https://telegra.ph/file/1f9bb59089588344bfb1f.jpg"

# Format
class Msg(object):
    START_MSG = "**Running !!**"

    TXT_MSG = "Hey <b>{user},"\
        "\n\n`I'm Multi-Talented Robot. I Can Download Many Type of Links.`"\
            "\n\nSend a TXT or HTML file :-</b>"

    ERROR_MSG = "<b>DL Failed ({no_of_files}) :-</b> "\
        "\n\n<b>Name: </b>{file_name},\n<b>Link:</b> `{file_link}`\n\n<b>Error:</b> {error}"

    SHOW_MSG = "<b>Downloading :- "\
        "\n`{file_name}`\n\nLink :- `{file_link}`</b>"

    CMD_MSG_1 = "`{txt}`\n\n**Total Links in File are :-** {no_of_links}\n\n**Send any Index From `[ 1 - {no_of_links} ]` :-**"
    CMD_MSG_2 = "<b>Uploading :- </b> `{file_name}`"
    RESTART_MSG = "✅ HI Bhai log\n✅ PATH CLEARED"

# Prefixes
prefixes = ["/", "~", "?", "!", "."]

# Client
plugins = dict(root="plugins")
if __name__ == "__main__":
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    if not os.path.isdir(Config.SESSIONS):
        os.makedirs(Config.SESSIONS)

    
