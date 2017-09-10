from django.shortcuts import render
import requests


def index(request):
    url = 'https://swapi.co/api/planets/'
    req = requests.get(url)

    # if json response is coming
    response = req.json()

    context = {
        'hello': "Hello World!!!",
        'responses': response['results'],
    }
    return render(request, 'sw_api/planets.html', context)


def detail(request, id):
    url = 'https://swapi.co/api/planets/'+id
    req = requests.get(url)

    # if json response is coming
    response = req.json()

    context = {
        'hello': "Hello World!!!",
        'responses': response['results'],
    }
    return render(request, 'sw_api/planets_detail.html', context)
