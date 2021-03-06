import os

CLIENT_ID = os.environ.get("CLIENT_ID",None)
CLIENT_SECRET = os.environ.get("CLIENT_SECRET",None)
API_ID = os.environ.get("API_ID",None)
API_HASH = os.environ.get("API_HASH",None)
SESSION_KEY = os.environ.get("SESSION_KEY",None)
INITIAL_TOKEN = os.environ.get("INITIAL_TOKEN",None)
INITIAL_BIO = "Existence is painfull! Zoldyck Family™♥️//Spam here @MedevilofMarvel"
SCREENSHOT_LAYER_ACCESS_KEY = os.environ.get("SCREENSHOT_LAYER_ACCESS_KEY",None)
BOT_TOKEN = os.environ.get("BOT_TOKEN",None)
BOTLOG = True 
LOG = os.environ.get('LOG_CHANNEL', None)
# the escaping is necessary since we are testing against a regex pattern with it.
CMD_PREFIX = '\?' 
# The key which is used to determine if the current bio was generated from the bot ot from the user. This means:
# NEVER use whatever you put here in your original bio. NEVER. Don't do it!
CONSOLE_LOGGER_VERBOSE = False

KEY = '🎶'
# The bios MUST include the key. The bot will go though those and check if they are beneath telegrams character limit.
BIOS = [KEY + ' Now Playing Spotify: {interpret} - {title} {progress}/{duration}',
        KEY + ' Now Playing Spotify: {interpret} - {title}',
        KEY + ' : {interpret} - {title}',
        KEY + ' Now Playing Spotify: {title}',
        KEY + ' : {title}']

OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID",None)
# Mind that some characters (e.g. emojis) count more in telegram more characters then in python. If you receive an
# AboutTooLongError and get redirected here, you need to increase the offset. Check the special characters you either
# have put in the KEY or in one of the BIOS with an official Telegram App and see how many characters they actually
# count, then change the OFFSET below accordingly. Since the standard KEY is one emoji and I don't have more emojis
# anywhere, it is set to one (One emoji counts as two characters, so I reduce 1 from the character limit).
OFFSET = 1
# reduce the OFFSET from our actual 70 character limit
LIMIT = 70 - OFFSET
