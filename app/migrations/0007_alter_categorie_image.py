# Generated by Django 4.1.5 on 2023-05-05 13:56

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0006_alter_categorie_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="categorie",
            name="image",
            field=models.ImageField(
                default="cat.png", null=True, upload_to=app.models.get_image_path
            ),
        ),
    ]