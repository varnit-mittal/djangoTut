# Generated by Django 4.2.3 on 2023-07-29 01:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0002_rename_articles_article"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="title",
            field=models.CharField(max_length=200),
        ),
    ]
