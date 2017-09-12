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
    response = requests.get(url).json()
    i = 0
    response_vehicle = [None]*99
    response_people = [None]*99
    response_starship = [None]*99
    response_planet = [None]*99
    response_species = [None]*99

    for people in response['characters']:
        response_people[i] = requests.get(people).json()
        i = i + 1

    i = 0
    for vehicles in response['vehicles']:
        response_vehicle[i] = requests.get(vehicles).json()
        i = i + 1

    i = 0
    for starships in response['starships']:
        response_starship[i] = requests.get(starships).json()
        i = i + 1

    i = 0
    for planets in response['planets']:
        response_planet[i] = requests.get(planets).json()
        i = i + 1

    i = 0
    for species in response['species']:
        response_species[i] = requests.get(species).json()
        i = i + 1

    context = {
        'hello': "Hello World!!!",
        'responses': response,
        'response_people': response_people,
        'response_vehicle': response_vehicle,
        'response_starship': response_starship,
        'response_planet': response_planet,
        'response_species': response_species,
    }
    return render(request, 'sw_api/films_detail.html', context)
