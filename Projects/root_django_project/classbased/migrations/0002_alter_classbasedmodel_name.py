# Generated by Django 3.2.7 on 2021-09-14 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classbased', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classbasedmodel',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]