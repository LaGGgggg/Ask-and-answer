# Generated by Django 3.2.9 on 2022-04-27 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='likes_value',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='questions',
            name='likes_value',
            field=models.IntegerField(default=0),
        ),
    ]
