from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=15)
    registration = models.SmallIntegerField()
    course = models.CharField(max_length=15)

    def __str__(self):
        return self.name