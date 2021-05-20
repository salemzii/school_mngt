from django.db import models
from django.utils import timezone


class Courses(models.Model):
    course = models.CharField(max_length=101)
    num = models.IntegerField(default=0)

    def __str__(self):
        return self.course


class Students(models.Model):
    name = models.CharField(max_length=60, blank=False)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    age = models.IntegerField(default=0, blank=True)
    level = models.IntegerField(default=1)
    email = models.EmailField(blank=False)
    phone_number = models.IntegerField()
    matric_number = models.CharField(max_length=20)
    date_admitted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Staff(models.Model):
    name = models.CharField(max_length=60, blank=False)
    lecture_course = models.ForeignKey(Courses, on_delete=models.CASCADE, blank=True)
    course_length = models.IntegerField(default=0)
    job_type = models.CharField(max_length=101)
    email = models.EmailField(blank=False)
    phone_number = models.IntegerField()
    date_employed = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


