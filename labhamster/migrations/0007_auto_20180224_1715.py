# Generated by Django 1.11.10 on 2018-02-24 14:15
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labhamster', '0006_auto_20180224_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='manufacturer_catalog',
            field=models.CharField(
                blank=True, help_text=b'manufacturer catalogue number', max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='catalog',
            field=models.CharField(
                help_text=b'vendor catalogue number', max_length=30),
        ),
    ]
