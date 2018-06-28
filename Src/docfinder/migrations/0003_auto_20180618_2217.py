# Generated by Django 2.0.6 on 2018-06-19 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('docfinder', '0002_auto_20180613_2129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=200, null=True)),
                ('value', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(max_length=50, null=True)),
                ('last_name', models.TextField(max_length=50, null=True)),
                ('age', models.TextField(max_length=3, null=True)),
                ('gender', models.TextField(max_length=5, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='preference',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docfinder.User'),
        ),
    ]
