# Generated by Django 2.1.7 on 2019-03-04 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0003_auto_20190304_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='current',
            field=models.BooleanField(default=False),
        ),
    ]
