# Generated by Django 5.1.3 on 2024-11-22 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ballot',
            name='total_votes',
            field=models.IntegerField(default=0),
        ),
    ]