import jsonfield
import datetime as dt
import logging
from django.db import models

from ParsingAndScraping.kinopoisk.kinopoiskAPI import KinopoiskAPI
from prices import cached_info

# Create your models here.
logging.basicConfig(
    level=logging.DEBUG,
    filename='bot.log',
    format='(asctime)s, %(levelname)s, %(message)s, %(name)s'
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.FileHandler('bot.log', mode='w'))


class IdDBManager(models.Manager):
    def create_record(self, kinopoisk_id):
        try:
            api = KinopoiskAPI()
            js = api.get_by_id(kinopoisk_id)
            title = js['data']['nameRu']
            year = js['data']['year']
            title_en = js['data']['nameEn']
            title_request = f'{title} {year}'
            prices_json = cached_info.parse_all(title_request)

            iddb_record = self.create(
                kinopoisk_id=kinopoisk_id,
                title=title,
                title_en=title_en,
                year=year,
                price=prices_json
            )

            return iddb_record
        except Exception as e:
            error_message = f'При создании записи произошла ошибка ({e})'
            logger.error(error_message)
            raise


class IdDB(models.Model):
    kinopoisk_id = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    year = models.IntegerField()
    date_created = models.DateField(default=dt.date.today())

    price = jsonfield.JSONField()

    objects = IdDBManager()
