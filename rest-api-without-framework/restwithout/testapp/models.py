# https://realpython.com/setting-up-sublime-text-3-for-full-stack-python-development/
from django.db import models

# Create your models here.

class Student(models.Model):
	name = models.CharField(max_length=40)
	rollno = models.IntegerField()
	marks = models.IntegerField()