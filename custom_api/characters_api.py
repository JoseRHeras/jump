import requests
import os
from dotenv import load_dotenv


env_variables = load_dotenv()

FICTIONAL_CHARACTERS_API_KEY = os.getenv('FICTIONAL_CHARACTERS_API_KEY')
FICTIONAL_CHARACTERS_URL = os.getenv('FICTIONAL_CHARACTERS_URL')
FICTIONAL_CHARACTERS_HOST = os.getenv('FICTIONAL_CHARACTERS_HOST')


def call_data_from_api(character_name: str) -> dict:
    """ 
            Function takes the name of characters as parameter
            It attempts to retrieve the characters data from API endpoint
    """
    querystring = {'hero': character_name}

    headers = {
        "X-RapidAPI-Key": FICTIONAL_CHARACTERS_API_KEY,
        "X-RapidAPI-Host": FICTIONAL_CHARACTERS_HOST
    }

    response = requests.request(
        "GET", FICTIONAL_CHARACTERS_URL, headers=headers, params=querystring)

    return response


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
    """
        Takes character name as parameter:
        If found returns a dictionary representing character:
        If not found then it returns an empty dictionary.
    """
    try:
        response = call_data_from_api(character_name=name)
        return format_data(response.json())
    except Exception:
        return {}

    


