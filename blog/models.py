from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(max_length= 1000)

    created_at = models.DateTimeField()

    def __str__(self):
        return f'{self.title}'


