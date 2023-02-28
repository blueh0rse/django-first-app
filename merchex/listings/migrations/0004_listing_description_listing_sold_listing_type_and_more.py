# Generated by Django 4.1.6 on 2023-02-27 17:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("listings", "0003_band_active_band_biography_band_genre_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="listing",
            name="description",
            field=models.CharField(default="", max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="listing",
            name="sold",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="listing",
            name="type",
            field=models.CharField(
                choices=[
                    ("RECORDS", "Records"),
                    ("CLOTHING", "Clothing"),
                    ("POSTERS", "Posters"),
                    ("OTHERS", "Others"),
                ],
                default="RECORDS",
                max_length=10,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="listing",
            name="year",
            field=models.IntegerField(
                default=1951,
                validators=[
                    django.core.validators.MinValueValidator(1900),
                    django.core.validators.MaxValueValidator(2021),
                ],
            ),
            preserve_default=False,
        ),
    ]
