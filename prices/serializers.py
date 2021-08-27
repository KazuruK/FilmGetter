from rest_framework.serializers import ModelSerializer

from prices.models import IdDB


class PricesSerializer(ModelSerializer):
    class Meta:
        model = IdDB
        fields = [
            'kinopoisk_id',
            'title',
            'title_en',
            'year',
            'price'
        ]
        lookup_field = 'kinopoisk_id'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
