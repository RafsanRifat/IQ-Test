# Generated by Django 2.0 on 2022-01-05 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iq', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question_sets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('set', models.TextField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='questions',
            name='question',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='questions',
            name='question_sets',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='iq.Question_sets'),
        ),
    ]
