# Generated by Django 2.0 on 2019-10-11 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20191011_0930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='passport',
        ),
    ]
