import os

from notifiers.email import *
from notifiers.telegram import *


def notify_service(notification):
    if os.environ.get('EMAIL_NOTIFICATION'):
        send_email(notification)

    if os.environ.get('TELEGRAM_NOTIFICATION'):
        send_telegram(notification)
