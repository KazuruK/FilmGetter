from django.contrib import admin


# Register your models here.
from prices.models import IdDB


class IdDBAdmin(admin.ModelAdmin):
    list_display = (
        'kinopoisk_id',
        'title',
        'title_en',
        'year',
        'detail',
        'date_created',
        'price',)
    search_fields = ('kinopoisk_id', 'title',)
    list_filter = ('year',)
    empty_value_display = '-пусто-'


admin.site.register(IdDB, IdDBAdmin)
