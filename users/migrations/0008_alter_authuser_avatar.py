# Generated by Django 4.1.3 on 2022-12-01 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_normaluser_id_remove_superadmin_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='avatar',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]