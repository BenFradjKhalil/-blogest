# Generated by Django 3.2.8 on 2021-12-03 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='date_de_publication',
            new_name='date_publication',
        ),
    ]