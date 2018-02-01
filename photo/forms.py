from photo.models import Album, Photo
from django.forms.models import inlineformset_factory # 1


PhotoInlineFormset = inlineformset_factory(Album, Photo, fields= ['image', 'title', 'description'], extra=2)
