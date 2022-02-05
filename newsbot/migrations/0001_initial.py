# Generated by Django 3.1.2 on 2020-11-04 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleExample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_text', models.TextField()),
                ('bias_score', models.FloatField()),
                ('bias_class', models.IntegerField()),
                ('quality_score', models.FloatField()),
                ('quality_class', models.IntegerField()),
                ('origin_url', models.TextField()),
                ('origin_source', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DictEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('canonWord', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entryURL', models.URLField(verbose_name='URL of news article')),
            ],
        ),
    ]
