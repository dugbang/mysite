from django.contrib import admin

# Register your models here.

from .models import Bbs


class BbsAdmin(admin.ModelAdmin):
    list_display=('title','author','created',)


admin.site.register(Bbs, BbsAdmin)
