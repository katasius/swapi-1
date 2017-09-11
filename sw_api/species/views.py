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
    url = 'https://swapi.co/api/species/'+id+'/'
    response = requests.get(url).json()

    url_people = response['people'][0]
    response_people = requests.get(url_people).json()

    for film in response['films']:
        response_film[0] = requests.get(film).json()

    context = {
        'hello': "Hello World!!!",
        'responses': response,
        'response_people': response_people,
    }
    return render(request, 'sw_api/species_detail.html', context)
