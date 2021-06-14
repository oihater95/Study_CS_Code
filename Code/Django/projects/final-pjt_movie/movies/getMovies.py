import requests

# import sys
# from os import path
# sys.path.append(path.dirname(path.abspath(path.dirname(__file__))))

from .models import Movie


class URLMaker:    
    url = 'https://api.themoviedb.org/3'

    def __init__(self, key):
        self.key = key

    def get_url(self, category='movie', feature='popular', **kwargs):
        url = f'{self.url}/{category}/{feature}'
        url += f'?api_key={self.key}'

        for k, v in kwargs.items():
            url += f'&{k}={v}'

        return url
        

    def movie_id(self, title):
        url = self.get_url('search', 'movie', region='KR', language='ko', query=title)
        res = requests.get(url)
        movie = res.json()

        if len(movie.get('results')):
            return movie.get('results')[0].get('id')
        else:
            return None
    

# if __name__ == '__main__':
key = '667342fb43a1ef1f79a62f2757d03682'
results = []
for i in range(1,4):
    url = URLMaker(key).get_url(page='i')
    data = requests.get(url).json().get('results')
    for j in range(len(data)):
        Movie(title = data[j].get('title'), 
            overview = data[j].get('overview'), 
            poster_path = 'https://image.tmdb.org/t/p/w500' + data[j].get('poster_path'),
            genre_ids = data[j].get('genre_ids')
        ).save()