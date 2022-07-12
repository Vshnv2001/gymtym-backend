# Generated by Django 3.0.14 on 2022-07-07 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeslots', '0003_auto_20220625_1121'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(max_length=256)),
                ('mods_link', models.TextField(max_length=400)),
                ('days', models.TextField(default='mon, tue, wed, thu, fri', max_length=500)),
                ('day_time', models.TextField(default='All', max_length=256)),
            ],
        ),
    ]