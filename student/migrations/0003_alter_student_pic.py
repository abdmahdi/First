# Generated by Django 4.0 on 2021-12-30 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_student_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='pic',
            field=models.ImageField(blank=True, default='/images/user.png', null=True, upload_to='images'),
        ),
    ]
