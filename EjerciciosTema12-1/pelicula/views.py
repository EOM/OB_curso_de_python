from django.shortcuts import render
# from director.models import Director
from .models import Pelicula


def index(request):
    count_peliculas = Pelicula.objects.all().count()
    peliculas = Pelicula.objects.all()

    return render(
        request,
        'pelicula/index.html',
        context={
            'count_peliculas': count_peliculas,
            'peliculas': peliculas,
        }
    )
