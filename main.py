import os
import time

from dotenv import load_dotenv

from notifiers.notify_service import *
from api_scraper.fetch_api_data import *
from api_scraper.parse_data import *


def main():
    load_dotenv()

    while True:
        raw_data = fetch_api_data()
        notification = parse_data(raw_data)

        if notification:
            notify_service(notification)

        time.sleep(60*int(os.environ.get('CHECK_PERIOD_MIN')))


if __name__ == "__main__":
    main()
