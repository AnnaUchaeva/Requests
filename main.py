from pprint import pprint

import requests

URL = 'https://akabab.github.io/superhero-api/api/all.json'

def test_request(URL):
    response = requests.get(URL)
    pprint(response.json())
    return response.json()

if __name__ == '__main__':
    test_request(URL)
