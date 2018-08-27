from django.db import models

# Create your models here.
from photo.fields import ThumbnailImageField


class Plant(models.Model):
    name = models.CharField(max_length=100, unique=True)
    # note = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Capture(models.Model):
    plant_id = models.ForeignKey(Plant, on_delete=models.DO_NOTHING)
    # control_id = models.ForeignKey(Plant, on_delete=models.DO_NOTHING)

    name = models.CharField(max_length=255)

    # image = ThumbnailImageField(upload_to='photo_{}/{}/%Y/%m'.format(plant_id.name, control_id.serial))
    # image = ThumbnailImageField(upload_to='photo_{}/%Y/%m'.format(plant_id.name))

    # create_date = models.DateTimeField('Create Date', null=True)
    # '{}'.format(datetime.now())[:19]
    create_date = models.CharField('Create Date', max_length=19, null=True)

    class Meta:
        ordering = ('plant_id', 'name', 'create_date', )

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     pass
        # return reverse('photo:photo_detail', args=(self.id,))

