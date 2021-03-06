# Generated by Django 2.0.2 on 2018-02-03 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foia', '0002_auto_20180203_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='name',
            field=models.CharField(default='tasty', max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='redaction',
            name='foia_exemption',
            field=models.CharField(default='tasty', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='document',
            name='image',
            field=models.ImageField(unique=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='redaction',
            name='redaction_id',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
