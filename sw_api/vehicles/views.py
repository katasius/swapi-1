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
    response = requests.get(url).json()

    i = 0
    response_people = [None]*99
    response_film = [None]*99

    for people in response['pilots']:
        response_people[i] = requests.get(people).json()
        i = i + 1

    i = 0
    for film in response['films']:
        response_film[i] = requests.get(film).json()
        i = i + 1

    context = {
        'hello': "Hello World!!!",
        'responses': response,
        'response_people': response_people,
        'response_films': response_film,
    }
    return render(request, 'sw_api/vehicles_detail.html', context)
