# Generated by Django 2.0 on 2019-10-11 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_customuser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='password',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
