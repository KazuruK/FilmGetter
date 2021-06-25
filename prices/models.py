from django.db import models
import jsonfield
import datetime as dt

# Create your models here.
from ParsingAndScraping.kinopoisk.kinopoiskAPI import KinopoiskAPI
from prices import cached_info


class IdDBManager(models.Manager):
    def create_record(self, kinopoisk_id):
        api = KinopoiskAPI()
        js = api.get_by_id(kinopoisk_id)
        title = js['data']['nameRu']
        year = js['data']['year']
        title_en = js['data']['nameEn']
        title_request = title + ' ' + year
        prices_json = cached_info.parse_all(title_request)

        iddb_record = self.create(
            kinopoisk_id=kinopoisk_id,
            title=title,
            title_en=title_en,
            year=year,
            price=str(prices_json)
        )

        return iddb_record


class IdDB(models.Model):

    kinopoisk_id = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    year = models.IntegerField()
    date_created = models.DateField(default=dt.date.today())
    detail = models.CharField(max_length=20, default='Found')

    price = jsonfield.JSONField()

    objects = IdDBManager()
