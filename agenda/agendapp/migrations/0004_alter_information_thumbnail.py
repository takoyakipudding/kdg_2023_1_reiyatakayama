# Generated by Django 4.2.6 on 2024-01-29 01:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("agendapp", "0003_information_user_answer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="information",
            name="thumbnail",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
