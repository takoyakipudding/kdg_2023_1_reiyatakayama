# Generated by Django 4.2.6 on 2024-01-29 03:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("agendapp", "0005_information_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="information",
            name="category",
            field=models.CharField(choices=[(1, "写真"), (2, "お題")], max_length=100),
        ),
    ]
