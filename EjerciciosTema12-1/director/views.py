from django.shortcuts import render
# from django.http import HttpResponse
from .models import Director


def index(request):

    count_directores = Director.objects.all().count()
    directores = Director.objects.all()

    return render(
        request,
        'director/index.html',
        context={
            'count_directores': count_directores,
            'directores': directores,
        }
    )
