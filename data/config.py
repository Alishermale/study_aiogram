import os
from dotenv import load_dotenv


load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
admin_id = os.getenv('ADMIN_ID')
PROVIDER_TOKEN = os.getenv('PROVIDER_TOKEN')
