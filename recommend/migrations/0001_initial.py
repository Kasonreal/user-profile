# Generated by Django 2.2.1 on 2019-06-04 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('tel', models.IntegerField()),
                ('appid', models.IntegerField()),
                ('time', models.IntegerField()),
                ('count', models.IntegerField()),
            ],
        ),
    ]
