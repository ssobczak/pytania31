from django.contrib import admin

# Register your models here.
from pytania.models import Pytanie, Lekcja

admin.site.register(Lekcja)
admin.site.register(Pytanie)
