# Generated by Django 4.1.6 on 2023-02-10 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training_data', '0003_auto_20230209_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]