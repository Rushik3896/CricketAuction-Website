# Generated by Django 3.0.4 on 2020-03-24 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricketer', '0003_cricketer_bid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cricketer_name', models.CharField(max_length=100)),
                ('bid', models.IntegerField(default=0)),
            ],
        ),
    ]
