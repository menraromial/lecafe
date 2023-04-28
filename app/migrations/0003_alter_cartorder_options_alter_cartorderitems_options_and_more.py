# Generated by Django 4.1.5 on 2023-04-28 12:09

import app.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("app", "0002_cartorder_alter_ingredient_ancien_cout_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="cartorder",
            options={"verbose_name": "Commande", "verbose_name_plural": "Commandes"},
        ),
        migrations.AlterModelOptions(
            name="cartorderitems",
            options={"verbose_name_plural": "Cart Order Items"},
        ),
        migrations.AlterField(
            model_name="item",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name="ItemReview",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("review", models.TextField()),
                (
                    "rating",
                    models.SmallIntegerField(
                        choices=[
                            (1, "★☆☆☆☆"),
                            (2, "★★☆☆☆"),
                            (3, "★★★☆☆"),
                            (4, "★★★★☆"),
                            (5, "★★★★★"),
                        ],
                        default=None,
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "item",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="app.item",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Item Reviews",
            },
        ),
        migrations.CreateModel(
            name="ItemImages",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "images",
                    models.ImageField(
                        default="item.png", upload_to=app.models.get_image_path
                    ),
                ),
                (
                    "item",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="app.item",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Item Images",
            },
        ),
    ]
