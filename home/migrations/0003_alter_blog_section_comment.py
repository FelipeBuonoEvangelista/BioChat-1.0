# Generated by Django 5.0.7 on 2024-07-21 16:11

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0002_alter_blog_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="section",
            field=models.CharField(
                choices=[
                    ("Popular", "Popular"),
                    ("Recent", "Recent"),
                    ("Trending", "Trending"),
                ],
                max_length=100,
            ),
        ),
        migrations.CreateModel(
            name="Comment",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("website", models.URLField(blank=True, null=True)),
                ("comment", models.TextField()),
                ("date", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="replies",
                        to="home.comment",
                    ),
                ),
            ],
        ),
    ]
