# Generated by Django 3.0.6 on 2020-05-14 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='description',
        ),
    ]