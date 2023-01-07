# Generated by Django 4.1.3 on 2022-12-31 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_authuser_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='role',
            field=models.IntegerField(choices=[(1, 'Super Admin'), (2, 'Normal User'), (3, 'Artist')]),
        ),
    ]