# Generated by Django 2.2.3 on 2019-07-09 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_userprofile_years_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='years_experience',
            field=models.IntegerField(default=0),
        ),
    ]
