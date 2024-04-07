#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    pass
    ""
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7177479550:AAGnc7qOC2xVdd_BDGPK4iy5YVO9oow1J-Q")
    API_ID = int(os.environ["API_ID", "22335135"])
    API_HASH = os.environ["API_HASH", "4273237df621d621f6caeb9c4a3b5495"]
    AUTH_USERS = "6949761949, 5361994895, 1905890740"
    
