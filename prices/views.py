import datetime as dt


from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action


from prices.serializers import PricesSerializer
from prices.models import IdDB



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
            if (iddb.date_created - dt.date.today()).days <= -3:
                iddb.delete()
                iddb = IdDB.objects.create_record(kinopoisk_id)
        print(iddb.price)

        data = {
            "kinopoisk_id": iddb.kinopoisk_id,
            "title": iddb.title,
            "title_en": iddb.title_en,
            "year": iddb.year,
            "detail": iddb.detail,
            "price": iddb.price,
        }

        return Response(data, 200)