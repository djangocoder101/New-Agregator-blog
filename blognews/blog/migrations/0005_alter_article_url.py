# Generated by Django 4.1.7 on 2023-05-18 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_article_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='url',
            field=models.URLField(unique=True),
        ),
    ]
