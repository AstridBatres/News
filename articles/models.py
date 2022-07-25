from django.db import models
from django.urls import reverse

class Article(models.Model):
    title=models.CharField(max_length=128)
    subtitle=models.CharField(max_length=128)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

def __str__(self):
    return self.title

def get_absolute_url(self):
    return revere('article_detail', args=[self.id])