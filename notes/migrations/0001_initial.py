# Generated by Django 5.1.3 on 2025-02-03 16:58

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("jury", "0001_initial"),
        ("questionnaires", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Notes",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("value", models.DecimalField(decimal_places=2, max_digits=5)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "jury",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="jury.jury"
                    ),
                ),
                (
                    "questionnaire",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="questionnaires.questionnaires",
                    ),
                ),
            ],
        ),
    ]
