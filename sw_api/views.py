from django.shortcuts import render
import requests


def index(request):
    url = 'https://swapi.co/api/'
    req = requests.get(url)

    # if json response is coming
    response = req.json()

    context = {
        'r': response,
    }
    return render(request, 'sw_api/index.html', context)


def people(request):
    url = 'https://swapi.co/api/people/'
    req = requests.get(url)

    # if json response is coming
    response = req.json()

    context = {
        'hello': "Hello World!!!",
        'responses': response['results'],
    }
    return render(request, 'sw_api/people.html', context)


def starships(request):
    url = 'https://swapi.co/api/starships/'
    req = requests.get(url)

    # if json response is coming
    response = req.json()

    context = {
        'hello': "Hello World!!!",
        'responses': response['results'],
    }
    return render(request, 'sw_api/starships.html', context)


def vehicles(request):
    url = 'https://swapi.co/api/vehicles/'
    req = requests.get(url)

    # if json response is coming
    response = req.json()

    context = {
        'hello': "Hello World!!!",
        'responses': response['results'],
    }
    return render(request, 'sw_api/vehicles.html', context)


def films(request):
    url = 'https://swapi.co/api/films/'
    req = requests.get(url)

    # if json response is coming
    response = req.json()

    context = {
        'hello': "Hello World!!!",
        'responses': response['results'],
    }
    return render(request, 'sw_api/films.html', context)


def species(request):
    url = 'https://swapi.co/api/species/'
    req = requests.get(url)

    # if json response is coming
    response = req.json()

    context = {
        'hello': "Hello World!!!",
        'responses': response['results'],
    }
    return render(request, 'sw_api/species.html', context)
