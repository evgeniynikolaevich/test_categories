# Generated by Django 2.2.10 on 2020-02-08 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='name',
            field=models.CharField(default='Category', max_length=30),
        ),
    ]
