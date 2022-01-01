# Generated by Django 4.0 on 2021-12-26 13:34

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groupe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('N_groupe', models.IntegerField()),
                ('starttime', models.TimeField()),
                ('endstime', models.TimeField()),
                ('nombredeplace', models.IntegerField(default=None)),
                ('Days', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Home.days')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Home.user')),
                ('first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True, unique=True)),
                ('adress', models.CharField(default=None, max_length=200)),
                ('pic', models.ImageField(blank=True, default='/user.png', null=True, upload_to='images')),
                ('phone', models.IntegerField(null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('level', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='Home.level')),
                ('matier', models.ManyToManyField(to='Home.Matier')),
                ('wilaya', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='Home.wilaya')),
            ],
        ),
        migrations.CreateModel(
            name='PostTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, default='/images/placeholder.png', null=True, upload_to='images')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('Annee', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='Home.annee')),
                ('division', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Home.division')),
                ('groups', models.ManyToManyField(to='teacher.Groupe')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Home.level')),
                ('matier', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Home.matier')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher')),
            ],
        ),
        migrations.AddField(
            model_name='groupe',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher'),
        ),
    ]