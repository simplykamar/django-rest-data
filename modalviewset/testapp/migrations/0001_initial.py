# Generated by Django 4.1.5 on 2023-04-15 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('sal', models.IntegerField()),
                ('city', models.CharField(max_length=30)),
            ],
        ),
    ]
