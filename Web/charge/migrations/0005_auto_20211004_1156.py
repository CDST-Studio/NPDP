# Generated by Django 3.2.7 on 2021-10-04 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charge', '0004_auto_20211003_2312'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='user_name',
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, upload_to='Orders/'),
        ),
    ]
