from django.db import models

# Create your models here.


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField(null=True)
    createDate = models.DateTimeField(auto_now_add=True)

