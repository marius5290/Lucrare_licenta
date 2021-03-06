# Generated by Django 3.0.5 on 2020-05-03 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='anime_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anime_id', models.IntegerField()),
                ('title', models.CharField(max_length=50)),
                ('title_english', models.CharField(max_length=50)),
                ('title_synonyms', models.CharField(max_length=50)),
                ('image_url', models.CharField(max_length=300)),
                ('type', models.CharField(max_length=10)),
                ('source', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=30)),
                ('airing', models.BooleanField(default=False)),
                ('aired', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=30)),
                ('score', models.FloatField()),
                ('scored_by', models.IntegerField()),
                ('rank', models.IntegerField()),
                ('popularity', models.IntegerField()),
                ('members', models.IntegerField()),
                ('favorites', models.IntegerField()),
                ('background', models.CharField(max_length=1000)),
                ('premiered', models.CharField(max_length=15)),
                ('producer', models.CharField(max_length=100)),
                ('licensor', models.CharField(max_length=50)),
                ('studio', models.CharField(max_length=30)),
                ('genre', models.CharField(max_length=100)),
                ('duration_min', models.FloatField()),
            ],
        ),
    ]
