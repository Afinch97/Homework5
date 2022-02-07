import requests
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

BASE_URL = 'https://api.themoviedb.org/3/trending/movie/week?api_key='+ os.getenv('TMBD_KEY')

def get_trending():
    response = requests.get(BASE_URL)
    return response
