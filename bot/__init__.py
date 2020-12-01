
""" credentials """

import logging
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler
from .get_config import get_config

load_dotenv("config.env")

# Get these values from my.telegram.org or Telegram: @useTGxBot
API_HASH = get_config("API_HASH", should_prompt=True)
APP_ID = get_config("APP_ID", should_prompt=True)
# get a token from @BotFather
TG_BOT_TOKEN = get_config("TG_BOT_TOKEN", should_prompt=True)
# array to store the channel ID who are authorized to use the bot
AUTH_CHANNEL = int(get_config(
        "AUTH_CHANNEL",
        "-100",
        should_prompt=True
    )
)
# sqlalchemy Database for the bot to operate
DB_URI = get_config(
    "DATABASE_URL",
    should_prompt=True
)
TG_BOT_WORKERS = int(get_config("TG_BOT_WORKERS", "4"))
#
COMMM_AND_PRE_FIX = get_config("COMMM_AND_PRE_FIX", "/")
#
BAN_COMMAND = get_config("BAN_COMMAND", "ban")
#
UN_BAN_COMMAND = get_config("UN_BAN_COMMAND", "unban")
# start command
START_COMMAND = get_config("START_COMMAND", "start")
# /start message when other users start your bot
START_OTHER_USERS_TEXT = get_config(
    "START_OTHER_USERS_TEXT",
    (
        "Hi. this is personal assistant of @peru_monster .leave your comment here.my master will reply as soon as possible☺️\n"
    )
)
# check online status of your bot
ONLINE_CHECK_START_TEXT = get_config(
    "ONLINE_CHECK_START_TEXT",
    (
        "i am online <b>master</b>\n\n"
    )
)
# IDEKWBYRW
DERP_USER_S_TEXT = get_config(
    "DERP_USER_S_TEXT",
    "😐"
)
# message to show when user is banned
IS_BLACK_LIST_ED_MESSAGE_TEXT = get_config(
    "IS_BLACK_LIST_ED_MESSAGE_TEXT",
    (
        "You have been <b>banned</b> forever.\n\n"
        "<u>Reason</u>: <code>{reason}</code>"
    )
)
# IDEKWBYRW
REASON_DE_LIMIT_ER = get_config(
    "REASON_DE_LIMIT_ER",
    "\n\n"
)
# message to show when user is unbanned
IS_UN_BANED_MESSAGE_TEXT = get_config(
    "IS_UN_BANED_MESSAGE_TEXT",
    (
        "You have been <b>un-banned</b>.\n\n"
        "<u>Reason</u>: <code>{reason}</code>"
    )
)
# message to show if bot was blocked by user
BOT_WS_BLOCKED_BY_USER = get_config(
    "BOT_WS_BLOCKED_BY_USER",
    "Bot was blocked by the user."
)
# path to store LOG files
LOG_FILE_ZZGEVC = get_config("LOG_FILE_ZZGEVC", "NoPMsBot.log")

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_ZZGEVC,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    """ get a Logger object """
    return logging.getLogger(name)
