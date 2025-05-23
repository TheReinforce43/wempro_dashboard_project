# Generated by Django 4.2.20 on 2025-05-12 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("category", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductModel",
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
                    "product_name",
                    models.CharField(db_index=True, max_length=255, unique=True),
                ),
                ("product_description", models.TextField(blank=True, null=True)),
                ("product_price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("product_image", models.ImageField(upload_to="product_images/")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "product_category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="category_products",
                        to="category.categorymodel",
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
                "unique_together": {("product_name", "product_category")},
            },
        ),
    ]
