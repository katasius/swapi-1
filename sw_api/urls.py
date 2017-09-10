from django.conf.urls import url, include

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^people/', include('sw_api.people.urls', namespace='people')),
    url(r'^starships/', include('sw_api.starships.urls', namespace='starships')),
    url(r'^vehicles/', include('sw_api.vehicles.urls', namespace='vehicles')),
    url(r'^species/', include('sw_api.species.urls', namespace='species')),
    url(r'^films/', include('sw_api.films.urls', namespace='films')),
    url(r'^planets/', include('sw_api.planets.urls', namespace='planets')),
]
