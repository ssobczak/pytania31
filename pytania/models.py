from django.db import models


# Create your models here.
class Pytanie(models.Model):
    tresc = models.CharField(max_length=1024)

    def __str__(self):
        return self.tresc
