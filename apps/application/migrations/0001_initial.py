# Generated by Django 4.2 on 2023-06-30 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Application",
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
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                ("title", models.CharField(max_length=256, verbose_name="Title")),
                (
                    "course_name",
                    models.CharField(max_length=256, verbose_name="Course Name"),
                ),
                (
                    "study_type",
                    models.CharField(max_length=256, verbose_name="Study Type"),
                ),
                (
                    "course_year",
                    models.CharField(max_length=256, verbose_name="Course Year"),
                ),
                (
                    "course_language",
                    models.CharField(max_length=256, verbose_name="Course Language"),
                ),
            ],
            options={
                "verbose_name": "Application",
                "verbose_name_plural": "Applications",
            },
        ),
        migrations.CreateModel(
            name="ApplicationDocument",
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
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                ("title", models.CharField(max_length=256, verbose_name="Title")),
                ("file", models.FileField(upload_to="applications/%Y/%m/%d")),
                (
                    "application",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="documents",
                        to="application.application",
                    ),
                ),
            ],
            options={
                "verbose_name": "ApplicationDocument",
                "verbose_name_plural": "ApplicationDocuments",
            },
        ),
    ]