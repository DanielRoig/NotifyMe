import os

from notifiers.email import *
from notifiers.telegram import *


def notify_service(notifications):

    for notification in notifications:
        if eval(os.environ.get('EMAIL_NOTIFICATION')):
            send_email(notification)

        if eval(os.environ.get('TELEGRAM_NOTIFICATION')):
            send_telegram(notification)
