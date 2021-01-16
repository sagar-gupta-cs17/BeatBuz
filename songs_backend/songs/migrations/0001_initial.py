# Generated by Django 3.0.5 on 2020-12-11 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=255)),
                ('image', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=255)),
                ('album', models.CharField(default='', max_length=255)),
                ('views', models.CharField(default='0', max_length=20)),
                ('language', models.CharField(default='', max_length=255)),
                ('genere', models.CharField(default='', max_length=255)),
                ('mood', models.CharField(default='', max_length=255)),
                ('lyrics', models.TextField(default='hi\nbro')),
                ('video', models.CharField(default='', max_length=255)),
                ('audio', models.CharField(default='', max_length=255)),
                ('poster', models.CharField(default='', max_length=255)),
                ('release_date', models.CharField(default='', max_length=255)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='art', to='songs.Artist')),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='', max_length=255)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('song_id', models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='song_id', to='songs.Songs')),
            ],
        ),
    ]
