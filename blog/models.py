from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.title}'

    content = models.TextField(max_length=1000)

    # 특정 지역 기준으로 작성 시각을 설정하기 위해서는 settings.py에서 설정한다.
    created_at = models.DateTimeField(auto_now_add=True) #처음 레코드가 생성된 시점을 저장하는 기능
    updated_at = models.DateTimeField(auto_now=True) #다시 저장할 때마다 그 시각이 저장되게 하는 기능