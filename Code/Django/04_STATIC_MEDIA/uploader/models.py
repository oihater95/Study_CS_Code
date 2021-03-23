from django.db import models
from imagekit.models import ProcessedImageField  # django.db models랑 안겹치게 imagekit.models를 from으로
from imagekit.processors import Thumbnail

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # blank => ORM이 빈 것을 허용함, DB는 자동으로 ''가 저장됨 => 비어있을 때도 is_valid() 통과
    # image = models.ImageField(blank=True) 
    
    image = ProcessedImageField(  # 사진 크기 조절
        upload_to='article/',  # 저장경로지정
        blank=True,
        processors=[Thumbnail(200, 300)],
        format='JPEG',  # 확장자
        options={'quality': 90},  # 화질
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

