# Generated by Django 5.1.7 on 2025-03-29 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_news_view_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='ads/')),
                ('link', models.URLField(blank=True, null=True)),
                ('columns', models.CharField(choices=[('main', 'Main Ad'), ('others', 'Other Ads')], default='main', max_length=10)),
            ],
        ),
    ]
