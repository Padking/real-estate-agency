from django.contrib import admin

from .models import Flat


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    list_display = ('address', 'price', 'new_building',
                    'construction_year', 'town', )

    list_editable = ('new_building', )
    readonly_fields = ('created_at', )
    search_fields = ('town', 'address', )
