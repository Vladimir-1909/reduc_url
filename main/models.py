from django.db import models
from django.contrib.auth.models import User


class LinkReduc(models.Model):
    link = models.TextField(unique=True)
    reducLink = models.CharField(max_length=120, unique=True)
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)

    def __str__(self):
        # return f'{self.reducLink} от {self.author} '
        return self.link