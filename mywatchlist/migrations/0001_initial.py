# Generated by Django 4.1 on 2022-09-22 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyWatchList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watched', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('rating', models.IntegerField(blank=True, default=None, null=True)),
                ('release_date', models.DateField()),
                ('review', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
