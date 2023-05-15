from django.db import models

# Create your models here.


class Student(models.Model):
    sname=models.CharField(max_length=30)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)

    def __str__(self):
        return self.sname