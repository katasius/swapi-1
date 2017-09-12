from django.shortcuts import render
import requests


def index(request):
    url = 'https://swapi.co/api/people/'
    req = requests.get(url)

    # if json response is coming
    response = req.json()

    context = {
        'hello': "Hello World!!!",
        'responses': response['results'],
    }
    return render(request, 'sw_api/people.html', context)


def detail(request, id):
    i = 0
    response_vehicle = [None]*99
    response_starship = [None]*99
    response_film = [None]*99
    response_species = [None]*99

    url = 'https://swapi.co/api/people/'+id+'/'
    response = requests.get(url).json()

    for species in response['species']:
        response_species[i] = requests.get(species).json()
        i = i + 1

    i = 0
    for film in response['films']:
        response_film[i] = requests.get(film).json()
        i = i + 1

    i = 0
    for vehicle in response['vehicles']:
        response_vehicle[i] = requests.get(vehicle).json()
        i = i + 1

    i = 0
    for starships in response['starships']:
        response_starship[i] = requests.get(starships).json()
        i = i + 1

    context = {
        'hello': "Hello World!!!",
        'responses': response,
        'response_species': response_species,
        'response_films': response_film,
        'response_vehicle': response_vehicle,
        'response_starship': response_starship,
        'response_planets': requests.get(response['homeworld']).json(),
    }
    return render(request, 'sw_api/people_detail.html', context)
