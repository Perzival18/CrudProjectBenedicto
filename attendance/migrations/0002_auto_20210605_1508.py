# Generated by Django 3.2.4 on 2021-06-05 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='section',
        ),
        migrations.AlterField(
            model_name='student',
            name='date',
            field=models.DateTimeField(max_length=100),
        ),
    ]
