from django.db import models

# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=100)
    student_sex = models.CharField(max_length=10)
    student_age = models.CharField(max_length=10)

class Comment(models.Model):
    comment_content = models.CharField(max_length=100)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
