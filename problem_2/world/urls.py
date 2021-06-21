from django.urls import path
from rest_framework import routers

from . import views


urlpatterns = [
    path("countries", views.GetCountriesList.as_view(), name='get-countries-list'),
    path("country/<str:country_name>/", views.GetCountry.as_view(), name='get-country'),
    ]


