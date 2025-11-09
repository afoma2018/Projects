from django.contrib import admin
from .models import Movie, Genere
# Register your models here.


class GenereAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'number_in_stock', 'release_year', 'daily_rate')
    exclude = ('date_created',)


admin.site.register(Movie, MovieAdmin)
admin.site.register(Genere, GenereAdmin)
