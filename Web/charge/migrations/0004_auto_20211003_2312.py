# Generated by Django 3.2.7 on 2021-10-03 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charge', '0003_auto_20211003_2134'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.RemoveField(
            model_name='post',
            name='head_image',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='Orders/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]