# Generated by Django 3.2.4 on 2021-06-25 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BooksManager', '0003_booktype'),
    ]

    operations = [
        migrations.AddField(
            model_name='booktype',
            name='interesting_level',
            field=models.CharField(default='None', max_length=50),
        ),
        migrations.AddField(
            model_name='booktype',
            name='subject',
            field=models.CharField(default='None', max_length=50),
        ),
    ]