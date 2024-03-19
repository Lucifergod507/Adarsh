#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    pass
    ""
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5323421782:AAFMaCslkGl5adfv7SkZ5_2jICXtkgXLL1k")
    API_ID = int(os.environ["API_ID", "15178129"])
    API_HASH = os.environ["API_HASH", "274a1c7f7ea99a473c6bd8facebc59ed"]
    AUTH_USERS = "5291627920"
    
