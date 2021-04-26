from django.db import models

# Create your models here.


class Lekcja(models.Model):
    nazwa = models.CharField(max_length=1024)

    def __str__(self):
        return self.nazwa


class Pytanie(models.Model):
    tresc = models.CharField(max_length=1024)
    lekcja = models.ForeignKey(Lekcja, on_delete=models.CASCADE)

    def __str__(self):
        return self.tresc
