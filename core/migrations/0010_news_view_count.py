# Generated by Django 5.1.7 on 2025-03-29 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_news_featured_type_alter_news_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='view_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
