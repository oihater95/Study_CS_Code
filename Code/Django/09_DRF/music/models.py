from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=50)
    

class Music(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='musics')
    title = models.CharField(max_length=100)
