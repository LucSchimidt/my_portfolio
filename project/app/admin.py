from django.contrib import admin
from . import models


class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'created_at')
    search_fields = ['title', 'type']

class TechAdmin(admin.ModelAdmin):
    list_display = ('title', 'type')
    search_fields = ['title', 'type']

admin.site.register(models.Item, ItemAdmin)  # Registrando o modelo Item com a classe ItemAdmin
admin.site.register(models.Tech, TechAdmin)
admin.site.register(models.Resume)
