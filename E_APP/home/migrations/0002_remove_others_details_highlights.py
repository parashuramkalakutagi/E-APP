# Generated by Django 4.1.7 on 2023-09-07 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='others_details',
            name='highlights',
        ),
    ]
