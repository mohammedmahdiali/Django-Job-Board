# Generated by Django 5.0.1 on 2024-01-04 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='published_at',
            field=models.DateField(),
        ),
    ]