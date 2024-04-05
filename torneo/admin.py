from django.contrib import admin

from .models import Evento

class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha', 'juego')
    search_fields = ('titulo', 'juego')
    list_filter = ('fecha',)

admin.site.register(Evento, EventoAdmin)

