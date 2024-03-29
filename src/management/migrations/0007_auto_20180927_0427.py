# Generated by Django 2.1.1 on 2018-09-27 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0006_auto_20180927_0411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='criminal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Criminal'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_activated',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_authorised',
            field=models.BooleanField(default=False),
        ),
    ]
