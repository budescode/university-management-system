# Generated by Django 2.0 on 2019-10-11 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20191011_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='dept',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='administrator.Department'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='faculty',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='administrator.Faculty'),
        ),
    ]
