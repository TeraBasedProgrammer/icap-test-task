# Generated by Django 4.2.5 on 2023-10-03 07:40

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("title", models.CharField(max_length=150)),
                ("photo", models.URLField()),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("PR", "Процесор"),
                            ("GC", "Відеокарта"),
                            ("KB", "Клавіатура"),
                            ("MS", "Миша"),
                            ("SD", "SSD"),
                            ("MB", "Материнська плата"),
                        ],
                        max_length=2,
                    ),
                ),
                ("month_offer", models.BooleanField()),
                ("is_available", models.BooleanField()),
                ("is_self_delivered", models.BooleanField()),
                ("description", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=11)),
            ],
        ),
    ]
