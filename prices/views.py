import datetime as dt
import logging

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from prices.serializers import PricesSerializer
from prices.models import IdDB


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.FileHandler('bot.log', mode='w'))


@api_view(['GET'])
def get_film(request, kinopoisk_id):
    try:
        if not IdDB.objects.filter(kinopoisk_id=kinopoisk_id).exists():
            iddb = IdDB.objects.create_record(kinopoisk_id)
        else:
            iddb = IdDB.objects.filter(kinopoisk_id=kinopoisk_id).get()
            if (iddb.date_created - dt.date.today()).days <= -3:
                iddb.delete()
                iddb = IdDB.objects.create_record(kinopoisk_id)
        serializer = PricesSerializer(iddb)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        error_message = (f'Произошла ошибка ({e}) при создании записи для'
                         f' {kinopoisk_id}')
        logger.error(error_message)
        return Response(status=status.HTTP_400_BAD_REQUEST)
