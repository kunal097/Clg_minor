# Generated by Django 2.1.1 on 2018-09-27 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_auto_20180927_0352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='criminal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Criminal'),
        ),
    ]
