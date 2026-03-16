import os
from dotenv import load_dotenv
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN').strip()  #text.strip("abc") - удаляет по бокам не подстроку, а именно такие символы
print(BOT_TOKEN)