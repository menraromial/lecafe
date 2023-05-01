# Generated by Django 4.1.5 on 2023-04-30 07:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0003_alter_cartorder_options_alter_cartorderitems_options_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ItemIngredients",
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
            ],
            options={
                "verbose_name_plural": "Item Ingredients",
            },
        ),
        migrations.AlterModelOptions(
            name="item",
            options={"ordering": ["title"]},
        ),
        migrations.RenameField(
            model_name="item",
            old_name="nom",
            new_name="title",
        ),
        migrations.RemoveField(
            model_name="item",
            name="cout",
        ),
        migrations.RemoveField(
            model_name="item",
            name="ingredients",
        ),
        migrations.AddField(
            model_name="item",
            name="available",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="item",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="item",
            name="price",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="item",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="item",
            name="ancien_cout",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AddIndex(
            model_name="item",
            index=models.Index(fields=["id", "slug"], name="app_item_id_d3ea0c_idx"),
        ),
        migrations.AddIndex(
            model_name="item",
            index=models.Index(fields=["title"], name="app_item_title_ae2bab_idx"),
        ),
        migrations.AddIndex(
            model_name="item",
            index=models.Index(fields=["-created"], name="app_item_created_b106bd_idx"),
        ),
        migrations.AddField(
            model_name="itemingredients",
            name="Ingredient",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="app.ingredient",
            ),
        ),
        migrations.AddField(
            model_name="itemingredients",
            name="item",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app.item"
            ),
        ),
    ]
