from django.contrib import admin

from .models import (
    Claim,
    Flat,
    Owner
)


@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat', )


class OwnerFlatInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ('owner', 'flat', )


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    inlines = [
        OwnerFlatInline
    ]

    list_display = ('address', 'price', 'new_building',
                    'construction_year', 'town', )

    list_editable = ('new_building', )
    list_filter = ('new_building', 'rooms_number', 'has_balcony', )
    raw_id_fields = ('liked_by', )
    readonly_fields = ('created_at', )
    search_fields = ('town', 'address', )


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    inlines = [
        OwnerFlatInline
    ]

    exclude = ('flats', )

    raw_id_fields = ('flats', )
    search_fields = ('owner', 'owner_pure_phone', )
