# Generated by Django 2.0.6 on 2018-06-19 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docfinder', '0004_auto_20180618_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.TextField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.TextField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.TextField(max_length=50, null=True),
        ),
    ]
