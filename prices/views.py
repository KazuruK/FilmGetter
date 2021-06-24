import json

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from prices import cached_info
from prices.serializers import PricesSerializer
from prices.models import IdDB
from ParsingAndScraping.kinopoisk.kinopoiskAPI import KinopoiskAPI


def get_data(request, kinopoisk_id):
    pass


class PricesView(ModelViewSet):
    queryset = IdDB.objects.all()
    serializer_class = PricesSerializer
    lookup_field = 'kinopoisk_id'

    @action(
        detail=False,
        methods=['get'],
        name="Get film",
        url_path=r'get/(?P<kinopoisk_id>\w+)',
        url_name="film"
    )
    def get_price(self, request, kinopoisk_id):
        if not IdDB.objects.filter(kinopoisk_id=kinopoisk_id).exists():
            iddb = IdDB.objects.create_record(kinopoisk_id)
        else:
            iddb = IdDB.objects.filter(kinopoisk_id=kinopoisk_id).get()

        print(iddb.price)

        data = {
            "kinopoisk_id": iddb.kinopoisk_id,
            "title": iddb.title,
            "title_en": iddb.title_en,
            "year": iddb.year,
            "price": iddb.price,
        }

        return Response(data, 200)