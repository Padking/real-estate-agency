# Generated by Django 2.2.20 on 2021-10-10 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_add_relation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner_pure_phone',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
    ]