# Generated by Django 5.2.3 on 2025-07-01 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quotes", "0002_rename_title_quote_text"),
    ]

    operations = [
        migrations.AlterField(
            model_name="quote",
            name="author",
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name="quote",
            unique_together={("text", "author")},
        ),
    ]
