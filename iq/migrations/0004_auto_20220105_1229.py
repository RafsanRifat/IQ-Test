# Generated by Django 3.2 on 2022-01-05 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iq', '0003_auto_20220105_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question_sets',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
