# Generated by Django 2.0 on 2022-01-05 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iq', '0002_auto_20220105_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question_sets',
            name='set',
            field=models.CharField(max_length=20),
        ),
    ]