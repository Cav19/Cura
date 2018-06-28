# Generated by Django 2.0.6 on 2018-06-24 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docfinder', '0007_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='age',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='specialty',
        ),
        migrations.AddField(
            model_name='doctor',
            name='phone_number',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='specialty',
            name='doctor',
            field=models.ManyToManyField(to='docfinder.Doctor'),
        ),
    ]
