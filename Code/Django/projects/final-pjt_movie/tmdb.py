import requests


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
