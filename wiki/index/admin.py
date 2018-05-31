from django.contrib import admin
from . models import SomeObject

# Register your models here.
class SomeObjectAdmin(admin.ModelAdmin):
    list_display = ('args', 'user')

admin.site.register(SomeObject, SomeObjectAdmin)
