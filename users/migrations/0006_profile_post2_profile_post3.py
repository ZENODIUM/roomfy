# Generated by Django 5.1.1 on 2024-12-30 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_profile_post1"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="post2",
            field=models.ImageField(blank=True, null=True, upload_to="profile_posts/"),
        ),
        migrations.AddField(
            model_name="profile",
            name="post3",
            field=models.ImageField(blank=True, null=True, upload_to="profile_posts/"),
        ),
    ]
