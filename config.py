# config.py

# To run this project, set the environment variables or directly set TOKEN and NGROK_URL below.
# Replace 'YOUR_TELEGRAM_TOKEN' with your actual Telegram Bot token and 'YOUR_NGROK_URL' with your ngrok URL.

import os

# Use environment variables or default to empty strings
TOKEN = os.getenv('TELEGRAM_TOKEN', 'YOUR_TELEGRAM_TOKEN')
NGROK_URL = os.getenv('NGROK_URL', 'YOUR_NGROK_URL')

BASE_TELEGRAM_URL = 'https://api.telegram.org/bot{}'.format(TOKEN)
LOCAL_WEBHOOK_ENDPOINT = '{}/webhook'.format(NGROK_URL)
TELEGRAM_INIT_WEBHOOK_URL = '{}/setWebhook?url={}'.format(BASE_TELEGRAM_URL, LOCAL_WEBHOOK_ENDPOINT)
TELEGRAM_SEND_MESSAGE_URL = BASE_TELEGRAM_URL + '/sendMessage?chat_id={}&text={}'
