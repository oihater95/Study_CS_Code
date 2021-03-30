from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    image = ProcessedImageField(
        upload_to='article/',
        blank=True,
        processors=[Thumbnail(300, 300)],
        format='JPEG',
        options={'quality': 90},

    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)