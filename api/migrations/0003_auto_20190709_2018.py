# Generated by Django 2.2.3 on 2019-07-09 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190709_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(default='Name', max_length=10),
        ),
    ]
