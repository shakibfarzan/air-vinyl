# Generated by Django 4.1.3 on 2022-12-31 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_remove_artist_id_alter_artist_auth_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='monthly_listeners',
        ),
        migrations.AlterField(
            model_name='album',
            name='album_cover',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]