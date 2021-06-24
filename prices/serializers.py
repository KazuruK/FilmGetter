from rest_framework.serializers import ModelSerializer

from prices.models import IdDB


class PricesSerializer(ModelSerializer):
    class Meta:
        model = IdDB
        fields = ['title', 'title_en', 'year', 'price']