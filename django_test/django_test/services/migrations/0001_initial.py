# Generated by Django 3.1.5 on 2021-01-04 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.TextField()),
                ('Year', models.TextField()),
                ('imdbID', models.TextField()),
                ('Type', models.TextField()),
                ('Poster', models.TextField()),
            ],
        ),
    ]