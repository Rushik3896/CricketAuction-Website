# Generated by Django 3.0.2 on 2020-03-13 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cricketer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('BOWLER', 'BOWLER'), ('BATSMAN', 'BATSMAN'), ('ALL_ROUNDER', 'ALL_ROUNDER')], default='BATSMAN', max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('cricketer_name', models.CharField(max_length=100)),
                ('matches', models.IntegerField(default=0)),
                ('runs', models.IntegerField(default=0)),
                ('highest', models.IntegerField(default=0)),
                ('average', models.FloatField(default=0.0)),
                ('strike_rate', models.FloatField(default=0.0)),
                ('hundreds', models.IntegerField(default=0)),
                ('fifeties', models.IntegerField(default=0)),
                ('wickets', models.IntegerField(default=0)),
                ('economy', models.FloatField(default=0.0)),
            ],
        ),
    ]
