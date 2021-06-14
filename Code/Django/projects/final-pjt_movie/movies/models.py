from django.db import models
from django.conf import settings
import requests

API_KEY = '667342fb43a1ef1f79a62f2757d03682'

class Genre(models.Model):
    genre_num = models.IntegerField()
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

#     @classmethod
#     def save_genres(cls):
#         url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}'
#         genrelist = requests.get(url).json().get('genres')
#         for genre in genrelist:
#             cls.objects.create(
#                 genre_num=genre.get('id'),
#                 name=genre.get('name'),
#             )

# Genre.save_genres()


class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    poster_path = models.CharField(max_length=500)
    user_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='movie_like')
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

#     @classmethod
#     def save_movie(cls):
#         category, feature = 'movie', 'popular'
#         for i in range(1, 6):
#             url = f'https://api.themoviedb.org/3/{category}/{feature}?api_key={API_KEY}&page={i}'
#             movies = requests.get(url).json().get('results')
#             for movie in movies:
#                 m = cls.objects.create(
#                     title=movie.get('title'),
#                     overview=movie.get('overview'),
#                     poster_path='https://image.tmdb.org/t/p/w500'+movie.get('poster_path'),
#                 )
                
#                 for genreid in movie.get('genre_ids'):
#                     g = Genre.objects.get(genre_num=genreid)
#                     m.genres.add(g)  # M:N 추가
    
# Movie.save_movie()


class Rate(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField()
