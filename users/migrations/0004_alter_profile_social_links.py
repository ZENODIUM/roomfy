# Generated by Django 5.1.1 on 2024-12-29 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_profile_room_background"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="social_links",
            field=models.JSONField(blank=True, default=list, null=True),
        ),
    ]
