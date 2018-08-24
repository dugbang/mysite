from django.forms import ModelForm
from .models import Photo


class PhotoForm(ModelForm):
    model = Photo

    class Meta:
        exclude = ('filtered_image',)
