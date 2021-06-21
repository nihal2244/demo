from rest_framework.response import Response
from rest_framework import generics
from . import service


class GetCountriesList(generics.ListAPIView):
    """ API for getting all countries details"""

    def list(self, request, *args, **kwargs):
        data = service.get_all_countries()
        return Response({"response": data})


class GetCountry(generics.RetrieveAPIView):
    """ API for getting country by name"""

    def get_object(self, *args, **kwargs):
        return service.get_county(self.kwargs['country_name'])

    def retrieve(self, request, *args, **kwargs):
        return Response({"response": self.get_object()})
