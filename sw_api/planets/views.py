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
    i = 0
    response_people = [5, 9]

    url = 'https://swapi.co/api/planets/'+id+'/'
    response = requests.get(url).json()

    for people in response['residents']:
        response_people[i] = requests.get(people).json()
        i = i + 1

    context = {
        'hello': "Hello World!!!",
        'responses': response,
        'response_people': response_people,
    }
    return render(request, 'sw_api/planets_detail.html', context)
