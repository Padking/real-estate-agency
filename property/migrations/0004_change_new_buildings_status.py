# Generated by Django 2.2.20 on 2021-10-07 16:29

from django.db import migrations


def update_new_buildings_status(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')

    flats = Flat.objects.all()
    for flat in flats:
        flat.new_building = flat.construction_year >= 2015
        flat.save()


def set_new_buildings_to_null(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')

    Flat.objects.all().update(new_building=None)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_add_field_in_flat_model'),
    ]

    operations = [
        migrations.RunPython(update_new_buildings_status,
                             set_new_buildings_to_null)
    ]
