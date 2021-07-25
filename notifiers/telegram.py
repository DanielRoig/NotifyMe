import os
import requests


def send_telegram(notification):
    requests.post('https://api.telegram.org/bot' + os.environ.get('TELEGRAM_BOT_TOKEN') + '/sendMessage', data={
                  'chat_id':  os.environ.get('TELEGRAM_CHAT_ID'),
                  'text': '*' + notification.subject + '*' + '\n' + notification.message,
                  'parse_mode': 'MarkdownV2'})
