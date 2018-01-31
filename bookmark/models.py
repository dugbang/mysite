from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Bookmark(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField('url', unique=True)
    owner = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)  # models.CASCADE

    def __str__(self):
        return self.title
