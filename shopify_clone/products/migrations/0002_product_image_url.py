# Generated by Django 3.2.16 on 2022-11-28 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_url',
            field=models.CharField(default=1, max_length=400),
            preserve_default=False,
        ),
    ]
