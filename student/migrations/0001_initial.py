# Generated by Django 4.0 on 2021-12-26 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Home.user')),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('phone', models.IntegerField(null=True)),
                ('pic', models.ImageField(default='/user.png', null=True, upload_to='images')),
                ('annee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Home.annee')),
                ('division', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Home.division')),
                ('level', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Home.level')),
                ('matier', models.ManyToManyField(related_name='preferer', to='Home.Matier')),
                ('wilaya', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Home.wilaya')),
            ],
        ),
    ]
