from django.contrib import admin

# Register your models here.
from .models import Memo


class MemoAdmin(admin.ModelAdmin):
    list_display = ('u_id', 'content', 'modify_date')


admin.site.register(Memo, MemoAdmin)
