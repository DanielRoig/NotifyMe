import os
import requests


def fetch_api_data():
    headers = {'Authorization': os.environ.get('BEARER_TOKEN')}
    response = requests.get(os.environ.get('API_URL'), headers=headers).json()

    return response
