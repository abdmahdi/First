# Generated by Django 4.0 on 2022-01-02 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0005_teacher_pic'),
        ('student', '0010_delete_subscripe'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscripeTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.groupe')),
                ('postteacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.postteacher')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]