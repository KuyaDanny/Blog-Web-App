# Generated by Django 4.1.3 on 2022-11-10 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default="John's Big Blog", max_length=255),
        ),
    ]
