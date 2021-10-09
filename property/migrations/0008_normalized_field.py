# Generated by Django 2.2.20 on 2021-10-08 17:22

from django.db import migrations

from ..utils import get_normalized_phone_number


def update_owner_pure_phone(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    db_alias = schema_editor.connection.alias

    flats = Flat.objects.using(db_alias).all()
    for flat in flats:
        normalized_phone_number = get_normalized_phone_number(
            flat.owners_phonenumber
        )
        if normalized_phone_number:
            flat.owner_pure_phone = normalized_phone_number
            flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_add_normalize_phone_field'),
    ]

    operations = [
        migrations.RunPython(update_owner_pure_phone,
                             migrations.RunPython.noop)
    ]
