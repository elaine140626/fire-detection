# login/admin.py
from django.contrib import admin
from . import models
admin.site.register(models.User)
admin.site.register(models.Device)
admin.site.register(models.Message)
admin.site.register(models.User_Message)
admin.site.register(models.Video)
