# Generated by Django 3.2.7 on 2021-10-03 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charge', '0002_auto_20211002_1943'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=30)),
                ('content', models.TextField(blank=True)),
                ('head_image', models.ImageField(blank=True, upload_to='testhuk/media/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_at',
        ),
        migrations.AddField(
            model_name='order',
            name='image',
            field=models.ImageField(null=True, upload_to='Video/'),
        ),
        migrations.AlterField(
            model_name='order',
            name='content',
            field=models.TextField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='user_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]