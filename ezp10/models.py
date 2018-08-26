from django.db import models

# Create your models here.


class Plant(models.Model):
    name = models.CharField(max_length=100, unique=True)
    # note = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    #
    # def dic(self):
    #     fields = ('name', )
    #     result = {}
    #     for field in fields:
    #         result[field] = self.__dict__[field]
    #
    #     return result
