# Generated by Django 4.0 on 2021-12-30 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='pic',
            field=models.ImageField(default='/user.png', upload_to='images'),
        ),
    ]
