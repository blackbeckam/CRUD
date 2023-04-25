from django.db import models


# Create your models here.
class Student(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    Email = models.EmailField()

    class Meta:
        db_table = 'student'
