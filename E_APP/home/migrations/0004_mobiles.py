# Generated by Django 4.1.7 on 2023-10-19 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_laptops'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mobiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Name', models.CharField(max_length=100000)),
                ('Product_Price', models.CharField(max_length=100)),
                ('Product_Reviews', models.CharField(max_length=100)),
            ],
        ),
    ]