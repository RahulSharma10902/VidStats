# Generated by Django 5.1 on 2024-08-23 16:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Movie", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
