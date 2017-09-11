from django.shortcuts import render
import requests


def index(request):
    url = 'https://swapi.co/api/vehicles/'
    req = requests.get(url)

    # if json response is coming
    response = req.json()

    context = {
        'hello': "Hello World!!!",
        'responses': response['results'],
    }
    return render(request, 'sw_api/vehicles.html', context)


def detail(request, id):
    url = 'https://swapi.co/api/vehicles/'+id+'/'
    req = requests.get(url)

    # if json response is coming
    response = req.json()

    context = {
        'hello': "Hello World!!!",
        'responses': response,
    }
    return render(request, 'sw_api/vehicles_detail.html', context)
