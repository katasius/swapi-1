from django.shortcuts import render
import requests


def index(request):
    url = 'https://swapi.co/api/films/'
    req = requests.get(url)

    # if json response is coming
    response = req.json()

    context = {
        'hello': "Hello World!!!",
        'responses': response['results'],
    }
    return render(request, 'sw_api/films.html', context)


def detail(request, id):
    url = 'https://swapi.co/api/films/'+id+'/'
    req = requests.get(url)

    # if json response is coming
    response = req.json()

    context = {
        'hello': "Hello World!!!",
        'responses': response,
    }
    return render(request, 'sw_api/films_detail.html', context)
