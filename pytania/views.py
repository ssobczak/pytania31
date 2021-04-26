# Create your views here.
from django.views.generic import ListView, CreateView

from pytania.models import Pytanie


class PytaniaListView(ListView):
    model = Pytanie


class PytanieCreate(CreateView):
    model = Pytanie
    fields = ['tresc']
    success_url = '/pytania/'
