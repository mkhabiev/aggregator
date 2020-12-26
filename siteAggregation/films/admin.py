from django.contrib import admin
from .models import Film, TVShow, Comment
# Register your models here.

admin.site.register(Film)
admin.site.register(TVShow)
admin.site.register(Comment)