from django.shortcuts import render
import requests


def index(request):
    url = 'https://swapi.co/api/species/'
    req = requests.get(url)

    # if json response is coming
    response = req.json()

    context = {
        'hello': "Hello World!!!",
        'responses': response['results'],
    }
    return render(request, 'sw_api/species.html', context)


def detail(request, id):
    i = 0
    response_film = [5, 9]
    response_people = [5, 9]
    url = 'https://swapi.co/api/species/'+id+'/'
    response = requests.get(url).json()

    for people in response['people']:
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
        'response_planets': requests.get(response['homeworld']).json(),
    }
    return render(request, 'sw_api/species_detail.html', context)
