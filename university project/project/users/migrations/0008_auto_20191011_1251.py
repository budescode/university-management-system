# Generated by Django 2.0 on 2019-10-11 11:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_customuser_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='mode_of_entry',
            field=models.CharField(choices=[('', 'Mode Of Enter'), ('UTME', 'UTME'), ('D.E', 'D.E')], max_length=15),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]