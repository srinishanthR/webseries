# Generated by Django 4.0.3 on 2022-04-02 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seriesapp1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seriestab',
            name='image',
            field=models.ImageField(default='default', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
