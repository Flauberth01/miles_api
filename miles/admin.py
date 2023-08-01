from django.contrib import admin
from miles.models import Depoimento

class Depoimentos(admin.ModelAdmin):
    list_display = ('id', 'foto', 'depoimento', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 3

admin.site.register(Depoimento, Depoimentos)