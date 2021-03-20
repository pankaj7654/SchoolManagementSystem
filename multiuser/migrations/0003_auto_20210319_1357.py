# Generated by Django 3.1.7 on 2021-03-19 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multiuser', '0002_auto_20210319_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='studentId',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacherId',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]