# Generated by Django 5.1.2 on 2024-11-03 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chai", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="chaivarity",
            name="description",
            field=models.TextField(default=""),
        ),
    ]
