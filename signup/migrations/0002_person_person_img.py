# Generated by Django 3.2.8 on 2021-10-26 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='person_img',
            field=models.ImageField(blank=True, null=True, upload_to='signup/images'),
        ),
    ]
