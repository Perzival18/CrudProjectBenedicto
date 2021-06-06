from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=10)
    course = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    date = models.CharField(max_length=100)

    class Meta:
        db_table = "student"