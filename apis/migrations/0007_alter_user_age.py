# Generated by Django 3.2.1 on 2021-05-14 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0006_useremotions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(blank=True),
        ),
    ]