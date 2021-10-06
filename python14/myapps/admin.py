from django.contrib import admin
from .import models
# Register your models here.

admin.site.register(models.Colleges)
admin.site.register(models.Provinces)
admin.site.register(models.Majors)
admin.site.register(models.Category)
admin.site.register(models.Firstlevel)
admin.site.register(models.Rankings)