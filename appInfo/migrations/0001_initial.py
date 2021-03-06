# Generated by Django 2.2.1 on 2019-06-04 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='appInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appid', models.IntegerField(max_length=6)),
                ('name', models.CharField(max_length=25)),
                ('male', models.FloatField()),
                ('female', models.FloatField()),
                ('age_24', models.FloatField()),
                ('age_25_30', models.FloatField()),
                ('age_31_35', models.FloatField()),
                ('age_36_40', models.FloatField()),
                ('age_40', models.FloatField()),
            ],
        ),
    ]
