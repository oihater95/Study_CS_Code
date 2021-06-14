from django.contrib import admin
from .models import Movie, Genre

class MovieAdmin(admin.ModelAdmin):
    fields = ['title', 'overview', 'poster_path', 'genres']

admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre)
