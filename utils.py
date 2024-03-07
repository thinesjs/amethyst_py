import requests


def get_random_name():
    request = requests.get(f'https://randomuser.me/api/')
    full_name = request.json()['results'][0]['name']['first'] + " " + request.json()['results'][0]['name']['last']
    return full_name
