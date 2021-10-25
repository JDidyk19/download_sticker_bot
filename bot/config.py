import os

from dotenv import load_dotenv


if os.path.exists(os.path.join(os.getcwd(), '.env')):
    load_dotenv()

# Telegram token
TOKEN = os.getenv('TOKEN')
# Path to project folder
BASE_DIR = os.getcwd()
# Path to stickers folder
STICKERS_FOLDER = os.path.join(BASE_DIR, 'stickers')
