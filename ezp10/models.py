from django.db import models

# Create your models here.


class Plant(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def dic(self):
        fields = ('id', 'name')
        result = {}
        for field in fields:
            result[field] = self.__dict__[field]

        return result
