# Generated by Django 5.1.1 on 2024-12-29 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_alter_profile_social_links"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="post1",
            field=models.ImageField(blank=True, null=True, upload_to="profile_posts/"),
        ),
    ]
