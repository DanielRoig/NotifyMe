from notification.notification import *


def parse_data(data):
    notification = Notification('New message!', str(data))
    return notification
