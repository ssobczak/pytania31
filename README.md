Pytania31
===========

Aplikacja do zadawania pytań przez uczniów w czasie lekcji.

Instrukcja:
-----------

`pip install django` - zainstaluj Django
`django-admin startproject pytania31` - utwórz nowy projekt

Następnie wchodzimy do folderu `pytania31` i pracujemy w nim.

`python manage.py startapp pytania` - tworzy moduł "pytania"
`python manage.py runserver 8080` - uruchamia serwer i aplikację

Do pliku `pytania31/settings.py`, do listy `INSTALLED_APPS` dodajemy `'pytania'`.

W pliku `pytania/models.py` dodajemy klasę `Pytanie` - Model.

`python manage.py makemigrations` - towrzy migracje. 
Migracja to "instrukcja" opisująca potrzebne zmiany w bazie danych.

Wykonaj potrzebne zmiany w bazie:
`python manage.py migrate`

Utwórz pierwszego administratora w systemie:
`python manage.py createsuperuser`

Żeby wyświetlić model `Pytanie` w panelu admina, 
w pliku `pytania/admin.py` dopisujemy linijkę:
`admin.site.register(Pytanie)`

Nastepnie tworzymy widok - klasę która będzie wyświetlała
wszystkie pytania w systemie.
W pliku `pytania/views.py` dopisujemy:
```
class PytaniaListView(ListView):
    model = Pytanie
```

Potrzebujemy również "strony" w HTML którą będzie widział
użytkownik. Tworzymy plik HTML pod ścieżką:
`pytania/templates/pytania/pytanie_list.html`

Ostatni element widoku to adres URL.
Dodajemy go w pliku `pytania31/urls.py`.