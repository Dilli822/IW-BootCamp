# Generated by Django 3.2.5 on 2021-08-12 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelrelation', '0002_auto_20210812_0514'),
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('info', models.CharField(max_length=100)),
                ('bio', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
