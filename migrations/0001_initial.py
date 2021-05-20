# Generated by Django 3.1 on 2020-08-18 15:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=101)),
                ('num', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('lecture_course', models.CharField(blank=True, max_length=150)),
                ('course_length', models.IntegerField(default=0)),
                ('job_type', models.CharField(max_length=101)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('date_employed', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('age', models.IntegerField(blank=True, default=0)),
                ('level', models.IntegerField(default=1)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('matric_number', models.CharField(max_length=20)),
                ('date_admitted', models.DateTimeField(default=django.utils.timezone.now)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager_app.courses')),
            ],
        ),
    ]
