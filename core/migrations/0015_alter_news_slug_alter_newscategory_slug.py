# Generated by Django 5.1.7 on 2025-04-08 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_alter_news_slug_alter_newscategory_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(default='default-slug', unique=True),
        ),
        migrations.AlterField(
            model_name='newscategory',
            name='slug',
            field=models.SlugField(default='default-slug', unique=True),
        ),
    ]
