# Generated by Django 3.1 on 2020-08-18 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='lecture_course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager_app.courses'),
        ),
    ]