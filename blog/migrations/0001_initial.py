# Generated by Django 5.0.6 on 2024-06-26 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
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
                ("title", models.CharField(max_length=100, verbose_name="название")),
                ("content", models.TextField(verbose_name="содержимое")),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="", verbose_name="изображение"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="дата и время создания"
                    ),
                ),
                (
                    "is_published",
                    models.BooleanField(default=True, verbose_name="опубликовано"),
                ),
                (
                    "views_count",
                    models.IntegerField(default=0, verbose_name="просмотры"),
                ),
            ],
            options={
                "verbose_name": "Блог",
                "verbose_name_plural": "Блоги",
            },
        ),
    ]
