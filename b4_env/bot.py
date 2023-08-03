import os
import dotenv
dotenv.load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN_ID = os.getenv('ADMIN_ID')

print(type(BOT_TOKEN))
print(type(ADMIN_ID))
