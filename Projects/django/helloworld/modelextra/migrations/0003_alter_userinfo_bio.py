# Generated by Django 3.2.5 on 2021-08-12 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelextra', '0002_alter_userinfo_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='bio',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]