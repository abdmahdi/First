# Generated by Django 4.0 on 2022-01-06 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0005_teacher_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupe',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]