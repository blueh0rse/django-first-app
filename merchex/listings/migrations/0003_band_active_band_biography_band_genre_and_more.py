# Generated by Django 4.1.6 on 2023-02-27 17:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("listings", "0002_listing"),
    ]

    operations = [
        migrations.AddField(
            model_name="band",
            name="active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="band",
            name="biography",
            field=models.CharField(default="bio1", max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="band",
            name="genre",
            field=models.CharField(
                choices=[
                    ("HH", "Hip Hop"),
                    ("SP", "Synth Pop"),
                    ("AR", "Alternative Rock"),
                ],
                default="HH",
                max_length=5,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="band",
            name="official_homepage",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="band",
            name="year_formed",
            field=models.IntegerField(
                default=1950,
                validators=[
                    django.core.validators.MinValueValidator(1900),
                    django.core.validators.MaxValueValidator(2021),
                ],
            ),
            preserve_default=False,
        ),
    ]
