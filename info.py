import re
from os import getenv, environ
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)
id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if isinstance(value, bool):
        return value
    if str(value).lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif str(value).lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information *
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', 29277139))
API_HASH = environ.get('API_HASH', 'e17c47f66af6ce385ab8d8fd9974fe96')
BOT_TOKEN = environ.get('BOT_TOKEN', '8649195046:AAG1sT6mvOtYSKui9r1ZGFM4jW2aAht4SWk')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = is_enabled(environ.get('USE_CAPTION_FILTER', 'False'), False)
PICS = (environ.get('PICS', 'https://i.ibb.co/1Gr1fHgD/5994bd963d94.jpg')).split()
PRIME_LOGO = environ.get('PRIME_LOGO', 'https://i.ibb.co/1Gr1fHgD/5994bd963d94.jpg')

# Admins, Channels & Users *
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '8874980751').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1004427480653').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL', '-1004427480653')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information *
DATABASE_URI = environ.get('DATABASE_URI', 'mongodb+srv://Pankaj9876:Pankaj9876@cluster0.klljsmr.mongodb.net/?appName=Cluster0')
DATABASE_NAME = environ.get('DATABASE_NAME', 'Cluster0')
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# LOG CHANNELS *
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1004336076887'))
LAZY_GROUP_LOGS = int(environ.get('LAZY_GROUP_LOGS', 0))
REQ_CHANNEL = int(environ.get('REQ_CHANNEL', '-1004429117242'))
PRIME_MEMBERS_LOGS = int(environ.get('PRIME_MEMBERS_LOGS', '0'))

# PREMIUM ACCESS *
lazydownloaders = [int(lz) if id_pattern.search(lz) else lz for lz in environ.get('PRIME_DOWNLOADERS', '').split()]
PRIME_USERS = lazydownloaders if lazydownloaders else []
lazy_renamers = [int(lz) if id_pattern.search(lz) else lz for lz in environ.get('LAZY_RENAMERS', '').split()]
LAZY_RENAMERS = (lazy_renamers + ADMINS) if lazy_renamers else []
LZURL_PRIME_USERS = [int(lazyurlers) if id_pattern.search(lazyurlers) else lazyurlers for lazyurlers in environ.get('LZURL_PRIME_USERS', '5965340120').split()]

QR_CODE_IMG = environ.get('QR_CODE_IMG', 'https://telegra.ph/file/ca18e2c794f4ea1c3135b.jpg')
UPI_ID = environ.get('UPI_ID', 'lazydeveloper@ybl')

# Others
TUTORIAL = environ.get('TUTORIAL', 'https://t.me/real_MoviesAdda3/186')
IS_TUTORIAL = is_enabled(environ.get('IS_TUTORIAL', 'True'), True)
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'LazyDeveloper')
P_TTI_SHOW_OFF = is_enabled(environ.get('P_TTI_SHOW_OFF', "False"), False)
IMDB = is_enabled(environ.get('IMDB', "True"), True)
SINGLE_BUTTON = is_enabled(environ.get('SINGLE_BUTTON', "False"), False)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "⚡<b>File uploaded by [Movies Adda™](https://t.me/real_MoviesAdda3)</b>⚡\n\n📂<b>File Name:</b> ⪧ {file_caption} \n <b>Size: </b>{file_size}\n\n❤")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>Your Query: {query}</b> \n‌‌‌‌🎁Support: @LazyDeveloper 🎁\n\n🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating}</a> / 10 \n\n♥️ we are nothing without you ♥️ \n\n💛 Please Share Us 💛\n\n⚠️Click on the button 👇 below to get your query privately")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), False)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in environ.get('FILE_STORE_CHANNEL', '-1004352536150').split()]
MELCOW_NEW_USERS = is_enabled(environ.get('MELCOW_NEW_USERS', "True"), True)
PROTECT_CONTENT = is_enabled(environ.get('PROTECT_CONTENT', "True"), False)
PUBLIC_FILE_STORE = is_enabled(environ.get('PUBLIC_FILE_STORE', "False"), False)

# LazyRenamer Configs
FLOOD = int(environ.get("FLOOD", "10"))
LAZY_MODE = is_enabled(environ.get("LAZY_MODE", "False"), False)

# Requested Content template variables
ADMIN_USRNM = environ.get('ADMIN_USRNM', 'LazyDeveloperr')
MAIN_CHANNEL_USRNM = environ.get('MAIN_CHANNEL_USRNM', 'LazyDeveloper')
DEV_CHANNEL_USRNM = environ.get('DEV_CHANNEL_USRNM', 'LazyDeveloper')
LAZY_YT_HANDLE = environ.get('LAZY_YT_HANDLE', 'LayDeveloperr')
MOVIE_GROUP_USERNAME = environ.get('MOVIE_GROUP_USERNAME', "+tl1Ll8L8TbQwMjdl")

# Url Shortner
URL_MODE = is_enabled(environ.get("URL_MODE", "True"), False)
URL_SHORTENR_WEBSITE = environ.get('URL_SHORTENR_WEBSITE', 'atglinks.com')
URL_SHORTNER_WEBSITE_API = environ.get('URL_SHORTNER_WEBSITE_API', 'b22588b960e9ed29dad0f068cfb69dbd844662e2')
lazy_groups = environ.get('LAZY_GROUPS', '')
LAZY_GROUPS = [int(lg) for lg in lazy_groups.split()] if lazy_groups else None
my_users = [int(mu) if id_pattern.search(mu) else mu for mu in environ.get('MY_USERS', '').split()]
MY_USERS = my_users if my_users else []

# Online Stream and Download
PORT = int(environ.get('PORT', 8080))
NO_PORT = is_enabled(environ.get('NO_PORT', 'False'), False)
APP_NAME = None
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = environ.get('APP_NAME')
else:
    ON_HEROKU = False
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else str(APP_NAME) + '.herokuapp.com'
URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else "http://{}:{}/".format(FQDN, PORT)
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
WORKERS = int(environ.get('WORKERS', '4'))
SESSION_NAME = str(environ.get('SESSION_NAME', 'LazyBot'))
MULTI_CLIENT = False
name = str(environ.get('name', 'CutePrincess'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(getenv('APP_NAME'))
else:
    ON_HEROKU = False
HAS_SSL = is_enabled(getenv('HAS_SSL', 'False'), False)
if HAS_SSL:
    URL = "https://{}/".format(FQDN)
else:
    URL = "http://{}/".format(FQDN)
BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001987654567")).split()))
OWNER_USERNAME = "LazyDeveloper"

PRIME_DOWNLOADERS = PRIME_USERS

# URL UPLOADING
BANNED_USERS = set(int(x) for x in environ.get("BANNED_USERS", "").split() if x.isdigit())
DOWNLOAD_LOCATION = "./DOWNLOADS"
MAX_FILE_SIZE = 4194304000
TG_MAX_FILE_SIZE = 4194304000
FREE_USER_MAX_FILE_SIZE = 4194304000
CHUNK_SIZE = int(environ.get("CHUNK_SIZE", 128))
HTTP_PROXY = environ.get("HTTP_PROXY", "")
OUO_IO_API_KEY = ""
MAX_MESSAGE_LENGTH = 4096
PROCESS_MAX_TIMEOUT = 0
DEF_WATER_MARK_FILE = ""
LOGGER = logging

# Adding Language Feature : 
LANGUAGES = ["hindi", "hin", "english", "eng", "korean", "kor", "urdu", "urd", "chinese", "chin", "tamil", "tam", "malayalam", "mal", "telugu", "tel", "kannada", "kan"]
SEASONS = ["season 1", "season 2", "season 3", "season 4", "season 5", "season 6", "season 7", "season 8", "season 9", "season 10"]
QUALITIES = ["360P", "", "480P", "", "720P", "", "1080P", "", "1440P", "", "2160P", ""]

MAX_B_TN = environ.get("MAX_B_TN", "10")
MAX_BTN = is_enabled(environ.get('MAX_BTN', "True"), True)

# Auto Delete For Group Message (Self Delete) #
SELF_DELETE_SECONDS = int(environ.get('SELF_DELETE_SECONDS', 300))
SELF_DELETE = is_enabled(environ.get('SELF_DELETE', 'True'), True)

DISCUSSION_TITLE = "Click Here"
DISCUSSION_CHAT_USRNM = "Discusss_Here"

# Download Tutorial Button #
DOWNLOAD_TEXT_NAME = "📥 HOW TO DOWNLOAD 📥"
DOWNLOAD_TEXT_URL = "https://t.me/real_MoviesAdda3"

# Custom Caption Under Button #
CAPTION_BUTTON = "Get Updates"
CAPTION_BUTTON_URL = "https://t.me/real_MoviesAdda3"

LOG_STR = "Current Customized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
