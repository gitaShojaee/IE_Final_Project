# Generated by Django 4.0 on 2022-01-01 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cinema',
            name='image',
            field=models.ImageField(null=True, upload_to='cinema_images/'),
        ),
        migrations.AddField(
            model_name='movie',
            name='poster',
            field=models.ImageField(default='temporary value', upload_to='movie_posters/'),
            preserve_default=False,
        ),
    ]
