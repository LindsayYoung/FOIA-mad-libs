# Generated by Django 2.0.2 on 2018-02-03 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foia', '0003_auto_20180203_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='description',
            field=models.TextField(default='doc'),
            preserve_default=False,
        ),
    ]
