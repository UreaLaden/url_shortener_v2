# Generated by Django 4.1 on 2022-08-26 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='urlModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.CharField(max_length=255)),
                ('short_url', models.CharField(max_length=7)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
    ]
