import requests
import os
from dotenv import load_dotenv


env_variables = load_dotenv()

FICTIONAL_CHARACTERS_API_KEY = os.getenv('FICTIONAL_CHARACTERS_API_KEY')
FICTIONAL_CHARACTERS_URL = os.getenv('FICTIONAL_CHARACTERS_URL')
FICTIONAL_CHARACTERS_HOST = os.getenv('FICTIONAL_CHARACTERS_HOST')


class InvalidHeroValue(Exception):
    pass


def call_data_from_api(character_name: str, alignment: str) -> dict:
    """ 
            Function takes the name of characters and its alignment (hero or villain)
            It attempts to retrieve the characters data which is returned as a dictionary
    """
    if alignment not in ['hero', 'villain']:
        raise InvalidHeroValue

    querystring = {alignment: character_name}

    headers = {
        "X-RapidAPI-Key": FICTIONAL_CHARACTERS_API_KEY,
        "X-RapidAPI-Host": FICTIONAL_CHARACTERS_HOST
    }

    response = requests.request(
        "GET", FICTIONAL_CHARACTERS_URL, headers=headers, params=querystring)

    return response.json()


def format_data(data) -> dict:
    return {

        'name': data['name'],
        'intelligence': data['powerstats']['intelligence'],
        'strength': data['powerstats']['strength'],
        'speed': data['powerstats']['speed'],
        'durability': data['powerstats']['durability'],
        'power': data['powerstats']['power'],
        'combat': data['powerstats']['combat'],
        'image': data['images']['md']
    }


def get_character_stats(name: str) -> dict:

    response = call_data_from_api(character_name=name, alignment='hero')
    return format_data(response)
