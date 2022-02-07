import os

import requests
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

BASE_URL = 'https://api.themoviedb.org/3/trending/movie/week?api_key='+ os.getenv('TMBD_KEY')
POSTER_PATH = 'https://image.tmdb.org/t/p/w185'

def get_trending():
    response = requests.get(BASE_URL)
    data = response.json()
    movies = data['results']
    
    def get_title(movies):
        return movies['title']
    
    def get_poster(movies):
        return (POSTER_PATH +movies['poster_path'])
    
    def get_ov(movies):
        return movies['overview']
    
    titles = map(get_title, movies)
    posters = map(get_poster, movies)
    overviews = map(get_ov, movies)
    
    return {
        'titles': list(titles),
        'overviews': list(overviews),
        'posters': list(posters),
    }