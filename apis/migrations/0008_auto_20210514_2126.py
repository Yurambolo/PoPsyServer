# Generated by Django 3.2.1 on 2021-05-14 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0007_alter_user_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]