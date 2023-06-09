# Generated by Django 4.1.5 on 2023-05-05 13:19

import app.models
from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0005_remove_cartorderitems_order_remove_item_ancien_cout_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="categorie",
            name="image",
            field=django_resized.forms.ResizedImageField(
                crop=None,
                force_format=None,
                keep_meta=True,
                quality=-1,
                scale=None,
                size=[299, 117],
                upload_to=app.models.get_image_path,
            ),
        ),
    ]
